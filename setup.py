from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "3.26.1"
readme = open('README.rst').read()

setup(
    name="dtool",
    packages=["dtool"],
    version=version,
    description="dtool command line client for managing data",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@gmail.com",
    url=url,
    install_requires=[
        "dtoolcore==3.18.0",
        "dtool-cli==0.7.1",
        "dtool-create==0.23.4",
        "dtool-info==0.16.2",
        "dtool-symlink==0.3.1",
        "dtool-http==0.5.1",
        "dtool-config==0.4.1",
        "dtool-overlay==0.3.1",
        "dtool-annotation==0.1.1",
        "dtool-tag==0.1.1",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
