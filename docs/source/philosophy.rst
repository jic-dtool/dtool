Philosophy - what is a dtool dataset?
=====================================

What is a "dtool dataset"?
--------------------------

Briefly, a dtool dataset consists of:

- The files added to the dataset, known as the dataset "items"
- Metadata used to describe the dataset as a whole
- Metadata describing the items in the dataset

The exact details of how this data and metadata is stored depends on the
"backend" (the type of storage used).  In other words a dataset is stored
differently on local file system disk to how it is stored in Amazon S3 object
store. However, the ``dtool`` commands and the Python API for interacting with
datasets are the same for all backends.


What does a dtool dataset look like on local disk?
--------------------------------------------------

Below is the structure of a fictional dataset containing three items from an
RNA sequencing experiment.

.. code-block:: none

    $ tree ~/my_dataset
    /Users/olssont/my_dataset
    ├── README.yml
    └── data
        ├── rna_seq_reads_1.fq
        ├── rna_seq_reads_2.fq
        └── rna_seq_reads_3.fq

The ``README.yml`` file is where metadata used to describe the whole dataset is
stored. The items of the dataset are stored in the directory named ``data``.

There is also hidden metadata, stored as plain text files, in a directory named
``.dtool``. This should not be edited directly by the user.


How does one create a dtool dataset?
------------------------------------

This happens in stages:

1. One creates a so called "proto dataset"
2. One adds data and metadata to this proto dataset
3. One converts the proto dataset into a dataset by "freezing" it

Once a proto dataset is "frozen" it is simply referred to as a dataset and it
is no longer possible to modify it. In other words it is not possible to add or
remove items from a dataset or to alter any of the items in a dataset.
