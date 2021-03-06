Working with datasets
=====================

Listing datasets
----------------

It is possible to list all datasets in a directory or in a S3 bucket
using the ``dtool ls`` command.

.. code-block:: none

    $ dtool ls ~/my_datasets
    bgi-sequencing-12345
      file:///Users/olssont/my_datasets/bgi-sequencing-12345
    drone-images
      file:///Users/olssont/my_datasets/drone-images
    fishers-iris-data
      file:///Users/olssont/my_datasets/fishers-iris-data
    my_rnaseq_data
      file:///Users/olssont/my_datasets/my_rnaseq_data

.. tip:: When using this command proto datasets are highlighted in red.

.. tip:: The ``dtool ls`` command takes a URI. As such it can be used to list
         the datasets in remote storage locations. The example below lists all
         the datasets in the S3 bucket named ``dtool-demo``::

            $ dtool ls s3://dtool-demo/


Generating an inventory of datasets
-----------------------------------

It is possible to generate CSV/TSV/HTML inventories of datasets in a directory
or in another base URI such as an Amazon S3 bucket. For example, the command
below is used to generate a HTML report of all the datasets in the
s3://dtool-demo/ bucket.

.. code-block:: none

    $ dtool inventory --format html s3://dtool-demo/ > inventory.html


Verifying a dataset has not been modified since freezing it
-----------------------------------------------------------

A dtool dataset has metadata listing its items and their hashes. This
information can be used to verify that a dataset is in the same state as it was
when it was frozen.

In the example below the dataset has been corrupted in three ways.

1. The file ``rna_seq_reads_4.fq.gz`` has been added to it
2. The file ``rna_seq_reads_3.fq.gz`` has been deleted from it
3. The content of the file ``rna_seq_reads_1.fq.gz`` has been modified

.. code-block:: none

    $ dtool verify ~/my_datasets/my_rnaseq_data
    Unknown item: 49919bdae83011b96bf54d984735e24c4419feb5 rna_seq_reads_4.fq.gz
    Missing item: 72b24007759c0086a316d13838021c2571853a16 rna_seq_reads_3.fq.gz

By default only identifiers and file sizes are compared. To check file hashes
make use of the ``--full`` option.

.. code-block:: none

    $ dtool verify --full ~/my_datasets/my_rnaseq_data
    Unknown item: 49919bdae83011b96bf54d984735e24c4419feb5 rna_seq_reads_4.fq.gz
    Missing item: 72b24007759c0086a316d13838021c2571853a16 rna_seq_reads_3.fq.gz
    Altered item: d4e065787eab480e9cbd2bac6988bc7717464c83 rna_seq_reads_1.fq.gz


Displaying the README descriptive metadata
------------------------------------------

To display the README metadata used to describe the dataset one can make use of
the ``dtool readme show`` command.

.. code-block:: none

    $ dtool readme show ~/my_datasets/chrX-rna-seq
    ---
    description: RNA-seq sample data
    creation_date: 2017-11-20
    ftp: "ftp://ftp.ccb.jhu.edu/pub/RNAseq_protocol/"
    doi: "10.1038/nprot.2016.095"


Reporting summary information about a dataset
---------------------------------------------

One often wants to find out how many items are in a dataset and what their
total size is. This can be achieved using the ``dtool summary`` command.

.. code-block:: none

    $ dtool summary ~/my_datasets/drone-images
    name: drone-images
    uuid: c2542c2b-d149-4f73-84bc-741bf9af918f
    creator_username: hartleym
    number_of_items: 59
    size: 152.5MiB
    frozen_at: 2017-09-19



Listing the item identifiers in a dataset
-----------------------------------------

To list all the item identifiers in a dataset one can use the ``dtool
identifiers`` command.

.. code-block:: none

    $ dtool identifiers ~/my_datasets/my_rnaseq_data
    b0f92a668d24a3015692b0869e2b7590a62a380c
    72b24007759c0086a316d13838021c2571853a16
    d4e065787eab480e9cbd2bac6988bc7717464c83


.. tip:: Using ``dtool ls`` on a dataset URI results in a list of item
         identifiers and relapths::

            $ dtool ls ~/my_datasets/my_rnaseq_data
            b0f92a668d24a3015692b0869e2b7590a62a380c - rna_seq_reads_2.fq.gz
            72b24007759c0086a316d13838021c2571853a16 - rna_seq_reads_3.fq.gz
            d4e065787eab480e9cbd2bac6988bc7717464c83 - rna_seq_reads_1.fq.gz


Finding out the size of an item in a dataset
--------------------------------------------

To find the size of a specific item in a dataset one can use the ``dtool item
properties`` command. The command below accesses the properties of the item
with the identifier ``58f50508c42a56919376132e36b693e9815dbd0c``.

.. code-block:: none

    $ dtool item properties ~/my_datasets/drone-images 58f50508c42a56919376132e36b693e9815dbd0c
    {
      "relpath": "IMG_8585.JPG",
      "size_in_bytes": 2716446,
      "utc_timestamp": 1505818439.0,
      "hash": "dbcb0d6f22ec660fa4ac33b3d74556f3"
    }


Accessing the content of an item in a dataset
---------------------------------------------

When all files are on local disk getting access to them is trivial.  However,
when files are located in some object storage system in the cloud, access may
be less trivial.

dtool solves this problem by providing a call to a method that returns an
absolute path on local disk with a promise that the file requested will be
available from there when the call returns the path.

The dtool command line interface makes this call available as the command
``dtool item fetch``.

Below is an example of this command being used on a local disk file storage.

.. code-block:: none

    $ dtool item fetch ~/my_datasets/drone-images 58f50508c42a56919376132e36b693e9815dbd0c
    /Users/olssont/my_datasets/drone-images/data/IMG_8585.JPG

Below is an example of this command being used on a dataset in the S3 bucket
``dtool-demo``.

.. code-block:: none

    $ dtool item fetch s3://dtool-demo/1e47c076-2eb0-43b2-b219-fc7d419f1f16 3dce23b901709a24cfbb974b70c1ef132af10a67
    /Users/olssont/.cache/dtool/s3/1e47c076-2eb0-43b2-b219-fc7d419f1f16/3dce23b901709a24cfbb974b70c1ef132af10a67.txt


Processing all the items in a dataset
-------------------------------------

By combining the use of ``dtool identifiers`` and ``dtool item fetch`` it is
possible to create basic Bash scripts to process all the items in a dataset.

.. code-block:: none

    $ DS_URI=~/my_datasets/my_rnaseq_data
    $ for ITEM_ID in `dtool identifiers $DS_URI`;
    > do ITEM_FPATH=`dtool item fetch $DS_URI $ITEM_ID`;
    > echo $ITEM_FPATH;
    > done
    /Users/olssont/my_datasets/my_rnaseq_data/data/rna_seq_reads_2.fq.gz
    /Users/olssont/my_datasets/my_rnaseq_data/data/rna_seq_reads_3.fq.gz
    /Users/olssont/my_datasets/my_rnaseq_data/data/rna_seq_reads_1.fq.gz
