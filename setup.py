from setuptools import setup

url = "https://github.com/jic-dtool/dtool"
version = "2.0.1"
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
        "dtoolcore==2.8.0",
        "dtool-cli==0.5.0",
        "dtool-create==0.7.0",
        "dtool-info==0.4.1",
        "dtool-symlink==0.1.0",
        "dtool-irods==0.3.1",
    ],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
