"""Test the dtool package."""


def test_version_is_string():
    import dtool
    assert isinstance(dtool.__version__, str)
