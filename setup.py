from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "3.15.0"
readme = open('README.rst').read()

setup(
    name="dtool",
    packages=["dtool"],
    version=version,
    description="Dtool command line client for managing data",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[
        "dtoolcore==3.10.0",
        "dtool-cli==0.7.0",
        "dtool-create==0.22.0",
        "dtool-info==0.13.0",
        "dtool-symlink==0.3.0",
        "dtool-http==0.3.0",
        "dtool-config==0.2.0",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
