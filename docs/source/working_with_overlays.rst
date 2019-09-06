Working with overlays
=====================

Overlays provide a means to store and access per item metadata.

Display table with all per item metadata
----------------------------------------

It is possible to display all the per item metadata as a CSV table using the
command ``dtool overlays show``.

.. code-block:: none

    $ dtool overlays show http://bit.ly/Ecoli-reads-minified
    identifiers,pair_id,is_read1,useful_name,relpaths
    8bda245a8cd526673aab775f90206c8b67d196af,9760280dc6313d3bb598fa03c5931a7f037d7ffc,False,ERR022075,ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc,8bda245a8cd526673aab775f90206c8b67d196af,True,ERR022075,ERR022075_1.fastq.gz

The dataset above has three overlays named: ``pair_id``, ``is_read1``, and
``useful_name``. The columns named ``identifiers`` and ``relpaths`` are
reported for bookkeeping purposes.

Creating overlays
-----------------

Overlay creation happens in two steps.

1. Create a template overlay CSV file using the format above
2. Use the template to write all overlays in the template to the dataset

Creating overlay templates
^^^^^^^^^^^^^^^^^^^^^^^^^^

A starting template can be created using the ``dtool overlays show`` command.
For a dataset with no overlays this will result in a table with the columns
``identifiers`` and ``relpaths``. The table will have one row for each item in
the dataset. One can then add columns for the overlays one would wish to
create.

However, in many cases one would want to use metadata in the items' relapths to
generate a starting CSV template. This can be achieved using the commands:

- ``dtool overlays template parse``
- ``dtool overlays template glob``
- ``dtool overlays template pairs``

Consider for example the dataset below::

    $ dtool ls http://bit.ly/Ecoli-reads-minified
    8bda245a8cd526673aab775f90206c8b67d196af  ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc  ERR022075_1.fastq.gz

The command below could be used to generate a template for the overlays
"useful_name" and "read"::

    $ dtool overlays template parse  \
        http://bit.ly/Ecoli-reads-minified  \
        '{useful_name}_{read:d}.fastq.gz'

Results in the CSV output below::

    identifiers,read,useful_name,relpaths
    8bda245a8cd526673aab775f90206c8b67d196af,2,ERR022075,ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc,1,ERR022075,ERR022075_1.fastq.gz

To ignore a variable element when parsing one can use unnamed curly braces. The
command below for example only generates the overlay "useful_name"::

    $ dtool overlays template parse  \
        http://bit.ly/Ecoli-reads-minified  \
        '{useful_name}_{:d}.fastq.gz'
    identifiers,useful_name,relpaths
    8bda245a8cd526673aab775f90206c8b67d196af,ERR022075,ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc,ERR022075,ERR022075_1.fastq.gz


Sometimes one simply wants to create a boolean overlay based on weather or not
a particular file matches a glob pattern. The command below can be used to
create a CSV template for an overlay named ``is_read1``::

    
    $ dtool overlays template glob  \
        http://bit.ly/Ecoli-reads-minified  \
        is_read1  \
        '*1.fastq.gz'
    identifiers,is_read1,relpaths
    8bda245a8cd526673aab775f90206c8b67d196af,False,ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc,True,ERR022075_1.fastq.gz
 
Sometimes it is useful to be able to find pairs of items. For example when
dealing with genomic sequencing data that has forward and reverse reads.

One can create a "pair_id" overlay CSV template for this dataset using the
command below::

    $  dtool overlays template pairs http://bit.ly/Ecoli-reads-minified .fastq.gz
    identifiers,pair_id,relpaths
    8bda245a8cd526673aab775f90206c8b67d196af,9760280dc6313d3bb598fa03c5931a7f037d7ffc,ERR022075_2.fastq.gz
    9760280dc6313d3bb598fa03c5931a7f037d7ffc,8bda245a8cd526673aab775f90206c8b67d196af,ERR022075_1.fastq.gz

In the above the suffix ".fastq.gz" is used to extract the prefix ``ERR022075_``
that is used to find matching pairs.


Writing an overlay template to a dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once one has a overlay template CSV file one can write this to a dataset::

    $ dtool overlays write <DS_URI> overlays.csv


Further reading
---------------

For more information see the at https://github.com/jic-dtool/dtool-overlay
