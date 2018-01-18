from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "3.0.0"
readme = open('README.rst').read()

setup(
    name="dtool",
    packages=["dtool"],
    version=version,
    description="Package files and metadata into self contained datasets",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@jic.ac.uk",
    url=url,
    install_requires=[
        "dtoolcore==3.0.0",
        "dtool-cli==0.6.0",
        "dtool-create==0.12.0",
        "dtool-info==0.8.0",
        "dtool-symlink==0.1.2",
        "dtool-irods==0.5.0",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
