Creating plugins
================

It is possible to create plugins to the ``dtool`` command line tool. There are
two different types of plugins: command line tools and backend storage brokers.
The former allows a developer to add custom extensions to the ``dtool``
command. The latter allows a developer to create an interface for talking to a
new type of storage. One could for example create a storage broker to interface
with `Amazon S3 <https://aws.amazon.com/s3/>`_ object storage.


Extending the ``dtool`` command line tool
-----------------------------------------

Information on how to extend the ``dtool`` command line tool is available in
the README file of `dtool-cli <https://github.com/jic-dtool/dtool-cli>`_.

Concrete examples making use of this plugin system are:

- `dtool-create <https://github.com/jic-dtool/dtool-create>`_
- `dtool-info <https://github.com/jic-dtool/dtool-info>`_


Creating an interface to a new type of storage
----------------------------------------------

Below are the steps required to create a storage broker for allowing ``dtool``
to interact with a new backend. A concrete example making use of this plugin
system is `dtool-irods <https://github.com/jic-dtool/dtool-info>`_.

1. Examine the code in ``dtoolcore.storagebroker.DiskStorageBroker``.
2. Create a Python class for your storage, e.g. ``MyStorageBroker``
3. Add a ``MyStorageBroker.key``` attribute to the class, this key is used to
   lookup an appropriate storage broker when interacting with a dataset
4. Add a ``dtoolcore.FileHasher`` instance that matches the hashing algorithm
   used by your storage to your ``MyStorageBroker.hasher`` attribute
5. Add implementations for all the public functions in
   ``dtoolcore.storagebroker.DiskStorageBroker`` class to ``MyStorageBroker``
6. Expose the ``MyStorageBroker`` class as a ``dtool.storage_broker``
   entrypoint, e.g. add a section along the lines of the below to the
   ``setup.py`` file::

        entry_points={
            "dtool.storage_brokers": [
                "MyStorageBroker=my_dtool_storage_plugin:MyStorageBroker",
            ],
        },
