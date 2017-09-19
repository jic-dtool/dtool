Dtool
=====

.. image:: https://badge.fury.io/py/dtool.svg
   :target: http://badge.fury.io/py/dtool
   :alt: PyPi package

.. image:: https://readthedocs.org/projects/dtool/badge/?version=latest
   :target: https://readthedocs.org/projects/dtool?badge=latest
   :alt: Documentation Status

- Documentation: http://dtool.readthedocs.io
- Free software: MIT License

Overview
--------

Dtool is a suite of software for managing scientific data and making it
accessible programatically. It consists of a command line interface ``dtool``
and a Python API: `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_.

The ``dtool`` command line interface allows one to organise files into datasets
and to move datasets between different storage solutions, for example from
local disk to remote object storage. 

The Python API gives complete access to the data and metadata in a dataset. It
also allows datasets to be constructed programatically.

Dtool is extensible, meaning that it is possible to create plugins both for
adding functionality to the command line interface and for creating interfaces
to custom storage backends.

The ``dtool`` Python package is a meta package that installs the packages:

- `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_ - core API
- `dtool-cli <https://github.com/jic-dtool/dtool-cli>`_ - CLI plugin scaffold
- `dtool-create <https://github.com/jic-dtool/dtool-create>`_ - CLI commands for creating datasets
- `dtool-info <https://github.com/jic-dtool/dtool-info>`_ - CLI commands for getting information about datasets
- `dtool-symlink <https://github.com/jic-dtool/dtool-symlink>`_ - storage broker interface allowing symlinking to data
- `dtool-irods <https://github.com/jic-dtool/dtool-irods>`_ - storage broker interface to iRODS

Installation::

    $ pip install -U pip setuptools wheel
    $ pip install dtool

Usage::

    $ dtool create my-awesome-dataset
    Created proto dataset file:///Users/olssont/my-awesome-dataset
    Next steps:
    1. Add descriptive metadata, e.g:
       dtool readme interactive file:///Users/olssont/my-awesome-dataset
    2. Add raw data, eg:
       dtool add item my_file.txt file:///Users/olssont/my-awesome-dataset
       Or use your system commands, e.g:
       mv my_data_directory /Users/olssont/my-awesome-dataset/data/
    3. Convert the proto dataset into a dataset:
       dtool freeze file:///Users/olssont/my-awesome-dataset
