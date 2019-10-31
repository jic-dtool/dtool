dtool: Manage Scientific Data
=============================

.. image:: https://badge.fury.io/py/dtool.svg
   :target: http://badge.fury.io/py/dtool
   :alt: PyPi package

.. image:: https://readthedocs.org/projects/dtool/badge/?version=latest
   :target: https://readthedocs.org/projects/dtool?badge=latest
   :alt: Documentation Status

*Make your data more resilient, portable and easy to work with by packaging
files & metadata into self contained datasets.*

- Documentation: http://dtool.readthedocs.io
- Paper: https://doi.org/10.7717/peerj.6562
- Free software: MIT License

Overview
--------

dtool is a suite of software for managing scientific data and making it
accessible programatically. It consists of a command line interface ``dtool``
and a Python API: `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_.

The ``dtool`` command line interface allows one to organise files into datasets
and to move datasets between different storage solutions, for example from
local disk to remote object storage. Importantly it also provides methods to
verify that the transfer has been successful.

The Python API gives complete access to the data and metadata in a dataset.  It
makes it easy to create scripts for processing the items, or a subset of items,
in a dataset. The Python API also allows datasets to be constructed
programatically.

dtool is extensible, meaning that it is possible to create plugins both for
adding functionality to the command line interface and for creating interfaces
to custom storage backends.

The ``dtool`` Python package is a meta package that installs the packages:

- `dtoolcore <https://github.com/jic-dtool/dtoolcore>`_ - core API
- `dtool-cli <https://github.com/jic-dtool/dtool-cli>`_ - CLI plugin scaffold
- `dtool-annotation <https://github.com/jic-dtool/dtool-annotation>`_ - CLI commands for working with dataset annotations
- `dtool-config <https://github.com/jic-dtool/dtool-config>`_ - CLI commands for configuring dtool
- `dtool-create <https://github.com/jic-dtool/dtool-create>`_ - CLI commands for creating datasets
- `dtool-info <https://github.com/jic-dtool/dtool-info>`_ - CLI commands for getting information about datasets
- `dtool-overlay <https://github.com/jic-dtool/dtool-overlay>`_ - CLI commands for working with per item metadata stored as overlays
- `dtool-symlink <https://github.com/jic-dtool/dtool-symlink>`_ - storage broker interface allowing symlinking to data
- `dtool-http <https://github.com/jic-dtool/dtool-symlink>`_ - storage broker interface allowing read only access to datasets over HTTP


Installation::

    $ pip install dtool

There are support packages for several object storage solutions:

- `dtool-s3 <https://github.com/jic-dtool/dtool-s3>`_ - storage broker interface to S3 object storage
- `dtool-azure <https://github.com/jic-dtool/dtool-azure>`_ - storage broker interface to Azure Storage
- `dtool-ecs <https://github.com/jic-dtool/dtool-ecs>`_ - storage broker interface to ECS S3 object storage
- `dtool-irods <https://github.com/jic-dtool/dtool-irods>`_ - storage broker interface to iRODS

If you have access to Amazon S3, Microsoft Azure, ECS S3 or iRODS storage you may also want to install support for these::

    $ pip install dtool-s3 dtool-azure dtool-ecs dtool-irods

Usage::

    $ dtool create my-awesome-dataset
    Created proto dataset file:///Users/olssont/my-awesome-dataset
    Next steps:
    1. Add raw data, eg:
       dtool add item my_file.txt file:///Users/olssont/my-awesome-dataset
       Or use your system commands, e.g:
       mv my_data_directory /Users/olssont/my-awesome-dataset/data/
    2. Add descriptive metadata, e.g:
       dtool readme interactive file:///Users/olssont/my-awesome-dataset
    3. Convert the proto dataset into a dataset:
       dtool freeze file:///Users/olssont/my-awesome-dataset
