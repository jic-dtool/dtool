Installation notes
==================

Dtool is a Python package that is pip installable.

Make sure that ``pip``, ``setputools`` and ``wheel`` are up to date.
This is a requirement of one of the dependencies (``ruamel.yaml``).

.. code-block:: none

    $ pip install -U pip setuptools wheel

Dtool can then be installed using ``pip``.

.. code-block:: none

    $ pip install dtool


Adding support for S3 object storage
------------------------------------

Install the ``dtool-s3`` package using ``pip``.

.. code-block:: none

    $ pip install dtool-s3

To configure Amazon S3 credentials see the README file in the `dtool-s3
<https://github.com/jic-dtool/dtool-s3>`_ GitHub repository.


Adding support for Azure storage
--------------------------------

Install the ``dtool-azure`` package using ``pip``.

.. code-block:: none

    $ pip install dtooazures3

To configure Microsoft Azure credentials see the README file in the
`dtool-azure <https://github.com/jic-dtool/dtool-azure>`_ GitHub repository.



Adding support for iRODS storage
--------------------------------

Install the ``dtool-irods`` package using ``pip``.

.. code-block:: none

    $ pip install dtool-irods

.. warning:: In order to be able to use the iRODS backend storage
             you will need to install the iCommands. Linux packages
             can be downloaded from `irods.org/download
             <https://irods.org/download/>`_. On Mac OSX these can
             be installed using the brew package manager::

                    $ brew install irods

For more details see the `dtool-irods
<https://github.com/jic-dtool/dtool-irods>`_ GitHub repository.
