Working with datasets
=====================

Listing datasets
----------------

It is possible to list all datasets in a directory or in an iRODS zone 
using the ``dtool ls`` command.

.. code-block:: none

    $ dtool ls ~/my_datasets
    469ca967-4239-4eb8-880b-4741a882b2c4 - bgi-sequencing-12345 - file:///Users/olssont/my_datasets/bgi-sequencing-12345
    c2542c2b-d149-4f73-84bc-741bf9af918f - drone-images         - file:///Users/olssont/my_datasets/drone-images
    f416ded6-2f9a-4909-ab43-2447d0d1a0d4 - fishers-iris-data    - file:///Users/olssont/my_datasets/fishers-iris-data
    6847e637-a61c-4043-a9e2-bbf4ff6f6baa - my_rnaseq_data       - file:///Users/olssont/my_datasets/my_rnaseq_data

.. info:: When using this command proto datasets are highlighted in red.


Verifying a dataset has not been modified since freezing it
-----------------------------------------------------------

A dtool dataset has metadata listing its items and their hashes. This
information can be used to verify that a dataset is in the same state as it was
when it was frozen.

In the example below the dataset has been corrupted in three ways.

1. The file ``rna_seq_reads_4.fq`` has been added to it
2. The file ``rna_seq_reads_3.fq`` has been deleted from it
3. The content of the file ``rna_seq_reads_1.fq`` has been modified

.. code-block:: none

    $ dtool verify ~/my_datasets/my_rnaseq_data
    Unknown item: 49919bdae83011b96bf54d984735e24c4419feb5 rna_seq_reads_4.fq
    Missing item: 72b24007759c0086a316d13838021c2571853a16 rna_seq_reads_3.fq
    Altered item: d4e065787eab480e9cbd2bac6988bc7717464c83 rna_seq_reads_1.fq


Reporting summary information about a dataset
---------------------------------------------

One often wants to find out how many items are in a dataset and what their
total size is. This can be achieved using the ``dtool summary`` command.

.. code-block:: none

    $ dtool summary ~/my_datasets/drone-images
    {
      "name": "drone-images",
      "uuid": "c2542c2b-d149-4f73-84bc-741bf9af918f",
      "creator_username": "olssont",
      "number_of_items": 59,
      "size_in_bytes": 159915554
    }


Listing the item identifiers in a dataset
-----------------------------------------


Getting information about an item in a dataset
----------------------------------------------


Accessing the content of an item in a dataset
---------------------------------------------


Processing all the items in a dataset
-------------------------------------
