Python API
==========

The ``dtool`` command line tool is built using the Python API in `dtoolcore
<https://github.com/jic-dtool/dtoolcore>`_. This API can also be used to create
and interact with datasets directly.

Below is an example showing how to load a dataset from a URI and use it to
print out a list of all the data item identifiers in the dataset.

.. code-block:: python

    >>> from dtoolcore import DataSet
    >>> dataset = DataSet.from_uri("bgi-sequencing-12345")
    >>> for i in dataset.identifiers:
    ...     print(i)
    ...
    1c10766c4a29536bc648260f456202091e2f57b4
    fbcc24bed36128535a263b74b2e138d7cc43e90c
    9ca330a84f3dbbdd457a860b5e3c21c917743dd6
    3dce23b901709a24cfbb974b70c1ef132af10a67
    78e7f1507da598e9f6a02810c1f846cfc24fb8ad
    42f43f49b74ef7f901010965aae71170c9fd3ef6
    ab069337b0f86cdad899d57e8de63d5b2b680c85
    b55ae3fbe6081eb2ed4ed2c4ea316dbeb943ea2c

More information on how to make use of the Python API can be found in the
`dtoolcore documentation <http://dtoolcore.readthedocs.io/en/latest/>`_.
