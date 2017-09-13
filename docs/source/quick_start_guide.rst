Quick start guide
=================

This quick start guide shows how the ``dtool`` command line tool can be used to
accomplish some common data management tasks.

Organising files into a dataset on local disk
---------------------------------------------

In this scenario one simply wants to organise one or more files into a dataset
in the file system on the local computer.

When working on local disk a dataset is simply a standardised directory layout
combined with some hidden files used to annotate the dataset and its items.

The first step is to create a "proto" dataset. The command below creates a
dataset named ``fishers-iris-data`` in the current working directory.

.. code-block:: none

    dtool create fishers-iris-data

One can now add files to the dataset by moving/copying them to the
``fisher-iris-data/data`` directory, or by using the built in ``dtool add
item`` command. In the example below the file ``iris.csv`` is added to the
proto dataset.

.. code-block:: none

    dtool add item iris.csv fishers-iris-data

Metadata describing the data is as important as the data itself. Metadata
describing the dataset is stored in the file ``fisers-iris-data/README.yml``.
An easy way to add content to this file is to use the ``dtool readme
interactive``, which will prompt for input regarding the dataset.

.. code-block:: none

    dtool readme interactive fishers-iris-data

Finally, to convert the proto dataset into a dataset one uses the ``dtool
freeze`` command.

.. code-block:: none

    dtool freeze fishers-iris-data


Copying data from an external hard drive to remote storage as a dataset
-----------------------------------------------------------------------

Genome sequencing generates large volumes of data, which are often sent from
the sequencing company to the user by posting an external hard drive. When
backing up such data on a remote storage system one does not want to have to
reorganise the data before copying it to the remote storage system.

In this case one can create a "symlink" dataset and copy that to the remote
storage. A symlink dataset is a dataset where the data directory is a symlink
to another location, for example the data directory on the external hard drive.
The command below opens a file browser prompting the user to select the
directory to use for the symlink and creates a proto dataset named
``bgi-sequencing-12345`` in the current working directory (``.``).

.. code-block:: none

    dtool create bgi-sequencing-12345 . symlink

Again, adding metadata to the dataset is vital.

.. code-block:: none

    dtool readme interactive bgi-sequencing-12345

One can then convert the proto dataset into a dataset by "freezing" it.

.. code-block:: none

    dtool freeze bgi-sequencing-12345

It is now time to copy the dataset to the remote storage. The command below
assumes that one has a working `iRODS <https://irods.org/>`_ server with a zone
named ``/data_raw`` and the `iCommands <https://irods.org/download/>`_
installed on the local machine. The command copies the local dataset to the
iRODS ``/data_raw`` zone.

.. code-block:: none

    dtool copy bgi-sequencing-12345 /data_raw irods

The command above returns feedback on the URI used to identify the dataset in
the remote storage. In this case
``irods:///data_raw/1e47c076-2eb0-43b2-b219-fc7d419f1f16``.

The URI used to identify the dataset in iRODS uses the UUID of the dataset
rather than the dataset's name. This is to avoid name clashes in the iRODS zone
that may be used by more than one person.

Finally, one may want to confirm that the data transfer was successful. This
can be achieved using the ``dtool diff`` command, which should show no
differences if the transfer was successful.

.. code-block:: none

    dtool diff bgi-sequencing-12345 irods:///data_raw/1e47c076-2eb0-43b2-b219-fc7d419f1f16

.. warning:: When comparing datasets identifiers, sizes and hashes are
             compared. When checking that the hashes are identical the hashes
             for the first dataset are recalculated using the hashing algorithm
             of the reference dataset (the second). If the dataset in iRODS had
             been specified as the first argument then all the files would have
             had to have been downloaded to the local disk before calculating
             their hashes, which would have made the command slower. 


Copying a dataset from remote storage to local disk
---------------------------------------------------

After having copied a dataset to a remote storage system one may have deleted
the copy on the local disk. In this case one may want to be able to get the
dataset back onto the local disk.

This can be achieved using the ``dtool copy`` command. The command below copies
the dataset in iRODS to the current working directory.

.. code-block:: none

    dtool copy irods:///data_raw/1e47c076-2eb0-43b2-b219-fc7d419f1f16

Note that on the local disk the dataset will use the name of the dataset rather
than the UUID, in this example ``bgi-sequencing-12345``.

Again one can verify the data transfer using the ``dtool diff`` command.

.. code-block:: none

    dtool diff bgi-sequencing-12345 irods:///data_raw/1e47c076-2eb0-43b2-b219-fc7d419f1f16
