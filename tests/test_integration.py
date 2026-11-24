"""Integration tests: the pinned packages work together as one ``dtool``.

The plugin repositories test themselves in isolation. These tests check
the combination that this meta-package pins: that every plugin loads into
the ``dtool`` command, and that a typical workflow works across packages,
including over HTTP.
"""

import functools
import json
import re
import threading
from importlib.metadata import entry_points, requires, version

import pytest
from click.testing import CliRunner

# Commands registered under the ``dtool.cli`` entry point by the pinned
# plugin packages.
EXPECTED_COMMANDS = {
    # dtool-create
    "create", "name", "readme", "add", "freeze", "cp", "publish",
    # dtool-info
    "ls", "summary", "item", "identifiers", "verify", "diff", "inventory",
    "status", "uri", "uuid",
    # dtool-config
    "config",
    # dtool-overlay
    "overlays",
    # dtool-annotation
    "annotation",
    # dtool-tag
    "tag",
}

EXPECTED_STORAGE_BROKERS = {"file", "symlink", "http", "https"}

EXPECTED_CONSOLE_SCRIPTS = {
    "dtool",
    # dtool-http
    "dtool_serve_directory",
    "dtool_publish_dataset",
}


def pinned_requirements():
    """Return {distribution name: pinned version} for this package."""
    pins = {}
    for req in requires("dtool"):
        if ";" in req:  # optional extras such as test or docs
            continue
        m = re.fullmatch(r"\s*([A-Za-z0-9_.-]+)\s*==\s*([^\s,]+)\s*", req)
        assert m, f"dtool dependency is not pinned exactly: {req}"
        pins[m.group(1)] = m.group(2)
    return pins


def run(*args, input=None):
    """Invoke ``dtool`` with ``args``; fail with its output on error."""
    from dtool_cli.cli import dtool

    result = CliRunner().invoke(dtool, [str(a) for a in args], input=input)
    assert result.exit_code == 0, (
        f"dtool {' '.join(map(str, args))} failed with exit code "
        f"{result.exit_code}:\n{result.output}"
        + (f"\n{result.exception!r}" if result.exception else ""))
    return result.output


@pytest.fixture
def cache_dir(tmp_path, monkeypatch):
    """Keep the dtool cache (used for HTTP downloads) inside tmp_path."""
    cache = tmp_path / "cache"
    cache.mkdir()
    monkeypatch.setenv("DTOOL_CACHE_DIRECTORY", str(cache))
    return cache


@pytest.fixture
def dataset(tmp_path, cache_dir):
    """Create and freeze a small dataset through the CLI; return its URI."""
    base = tmp_path / "datasets"
    base.mkdir()
    data = tmp_path / "data"
    data.mkdir()
    (data / "a.txt").write_text("hello\n")
    (data / "b.csv").write_text("x,y\n1,2\n")

    uri = run("create", "-q", "integration", base).strip()
    run("add", "item", data / "a.txt", uri)
    run("add", "item", data / "b.csv", uri, "sub/b.csv")
    run("add", "metadata", uri, "a.txt", "kind", "text")
    run("add", "metadata", uri, "sub/b.csv", "kind", "table")
    run("readme", "write", uri, "-",
        input="description: dtool integration test\n")
    run("freeze", uri)
    return uri


# --- The packages fit together --------------------------------------------

def test_installed_versions_match_pins():
    pins = pinned_requirements()
    assert pins, "no pinned dependencies found"
    mismatches = {name: (pinned, version(name))
                  for name, pinned in pins.items() if version(name) != pinned}
    assert not mismatches, f"installed != pinned: {mismatches}"


def test_all_plugins_load():
    from click_plugins.core import BrokenCommand
    from dtool_cli.cli import dtool

    broken = sorted(name for name, cmd in dtool.commands.items()
                    if isinstance(cmd, BrokenCommand))
    assert not broken, f"plugins that failed to load: {broken}"
    missing = EXPECTED_COMMANDS - set(dtool.commands)
    assert not missing, f"commands not registered: {sorted(missing)}"


def test_storage_brokers_registered():
    import dtoolcore

    brokers = set(dtoolcore._generate_storage_broker_lookup())
    missing = EXPECTED_STORAGE_BROKERS - brokers
    assert not missing, f"storage brokers not registered: {sorted(missing)}"


def test_console_scripts_registered():
    scripts = {ep.name for ep in entry_points(group="console_scripts")}
    missing = EXPECTED_CONSOLE_SCRIPTS - scripts
    assert not missing, f"console scripts not installed: {sorted(missing)}"


def test_version_lists_pinned_packages():
    output = run("--version")
    for name, pinned in pinned_requirements().items():
        assert f"{name}, version {pinned}" in output, (
            f"'{name}, version {pinned}' missing from dtool --version:\n"
            f"{output}")


# --- A workflow across packages --------------------------------------------

def test_dataset_workflow(dataset, tmp_path):
    # dtool-info
    listing = run("ls", dataset)
    assert "a.txt" in listing and "sub/b.csv" in listing
    summary = json.loads(run("summary", "--format", "json", dataset))
    assert summary["name"] == "integration"
    assert summary["number_of_items"] == 2
    run("verify", dataset)
    assert len(run("identifiers", dataset).split()) == 2

    # dtool-create (readme) and dtool-overlay (per-item metadata)
    assert "dtool integration test" in run("readme", "show", dataset)
    overlays = run("overlays", "show", dataset)
    assert "kind" in overlays
    assert "text" in overlays and "table" in overlays

    # dtool-annotation
    run("annotation", "set", dataset, "project", "dtool")
    assert run("annotation", "get", dataset, "project").strip() == "dtool"
    run("annotation", "delete", dataset, "project")
    assert "project" not in run("annotation", "ls", dataset)

    # dtool-tag
    run("tag", "set", dataset, "integration")
    assert run("tag", "ls", dataset).split() == ["integration"]
    run("tag", "delete", dataset, "integration")
    assert run("tag", "ls", dataset).split() == []

    # dtool-create (copy) and dtool-info (diff)
    copies = tmp_path / "copies"
    copies.mkdir()
    copy = run("cp", "-q", dataset, copies).strip()
    assert run("uuid", copy) == run("uuid", dataset)
    run("diff", "--full", dataset, copy)


def test_dataset_over_http(dataset, tmp_path):
    """Serve the dataset with dtool-http and read it back through dtool."""
    from dtool_http.server import DtoolHTTPRequestHandler, DtoolHTTPServer

    class QuietHandler(DtoolHTTPRequestHandler):
        # The request log goes to stderr, which the CLI runner mixes into
        # the output that the commands below are parsed from.
        def log_message(self, *args):
            pass

    base = tmp_path / "datasets"
    handler = functools.partial(QuietHandler, directory=str(base))
    server = DtoolHTTPServer(("localhost", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address[:2]
        http_uri = f"http://{host}:{port}/integration"

        listing = run("ls", http_uri)
        assert "a.txt" in listing and "sub/b.csv" in listing
        assert "dtool integration test" in run("readme", "show", http_uri)

        copies = tmp_path / "http-copies"
        copies.mkdir()
        copy = run("cp", "-q", http_uri, copies).strip()
        run("diff", "--full", dataset, copy)
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
