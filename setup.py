from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "3.26.0"
readme = open('README.rst').read()

setup(
    name="dtool",
    packages=["dtool"],
    version=version,
    description="dtool command line client for managing data",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[
        "dtoolcore==3.18.0",
        "dtool-cli==0.7.0",
        "dtool-create==0.23.3",
        "dtool-info==0.16.1",
        "dtool-symlink==0.3.0",
        "dtool-http==0.5.0",
        "dtool-config==0.4.0",
        "dtool-overlay==0.3.0",
        "dtool-annotation==0.1.0",
        "dtool-tag==0.1.0",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
