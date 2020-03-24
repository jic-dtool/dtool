Tagging datasets
================

It is possible to tag datasets with labels.

To tag a dataset with the label "rnaseq" one would use the command below::

    $ dtool tag set <DS_URI> rnaseq

It is possible to add more than one tag to a dataset. The command below
adds the tag "A.thaliana"::

    $ dtool tag set <DS_URI> A.thaliana

To list tags one would use the command below:

    $ dtool tag ls <DS_URI>

This would produce the output::

    A.thalina
    rnaseq

It is possible to delete a tag that has been added to a dataset::


    $ dtool tag delete <DS_URI> A.thaliana
