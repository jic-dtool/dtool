Publishing a dataset
====================

It is possible to publish a datasets hosted in AWS S3 and Microsoft Azure
Storage. A dataset is published by making it accessible via the HTTP(S)
protocol.

.. warning:: A published dataset is accessible by anyone in the world with an
             internet connection!

.. code-block:: none

    $ dtool publish s3://dtool-demo/ba92a5fa-d3b4-4f10-bcb9-947f62e652db
    Dataset accessible at https://dtool-demo.s3.amazonaws.com/ba92a5fa-d3b4-4f10-bcb9-947f62e652db

The URL retuned by the ``dtool publish`` command can be used to interact with the dataset.

.. code-block:: none

    $ dtool summary https://dtool-demo.s3.amazonaws.com/ba92a5fa-d3b4-4f10-bcb9-947f62e652db
    name: hypocotyl3
    uuid: ba92a5fa-d3b4-4f10-bcb9-947f62e652db
    creator_username: olssont
    number_of_items: 339
    size: 86.7MiB
    frozen_at: 2018-09-12

