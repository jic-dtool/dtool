from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "2.0.0"
readme = open('README.rst').read()

setup(
    name="dtool",
    packages=["dtool"],
    version=version,
    description="Manage scientific data",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[
        "dtoolcore",
        "dtool-cli",
        "dtool-create",
        "dtool-info",
        "dtool-symlink",
        "dtool-irods",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
