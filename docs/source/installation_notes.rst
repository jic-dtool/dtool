Installation notes
==================

Dtool is a Python package that is pip installable.

Make sure that ``pip``, ``setputools`` and ``wheel`` are up to date.
This is a requirement of one of the dependencies (``ruamel.yaml``).

.. code-block:: none

    pip install -U pip setuptools wheel

Dtool can then be installed using ``pip``.

.. code-block:: none

    pip install dtool

.. warning:: In order to be able to use the iRODS backend storage
             you will need to install the iCommands. Linux packages
             can be downloaded from `irods.org/download
             <https://irods.org/download/>`_. On Mac OSX these can
             be installed using the brew package manager::

                    brew install irods
