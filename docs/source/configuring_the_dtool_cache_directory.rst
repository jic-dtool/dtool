Configuring the dtool cache directory
=====================================

When fetching a dataset item from a dataset stored in object storage the file
get stored in a cache directory. The default cache directory is::

    ~/.cache/dtool

You may want to configure this cache to be in a different location. This can be achieved using the ``dtool config cache`` command::

    $ mkdir /tmp/dtool
    $ dtool config cache /tmp/dtool

It is also possible to override both the default and the configured cache
directory by exporting the environment variable ``DTOOL_CACHE_DIRECTORY``.
This can be useful when using local SSD on a compute cluster::


    $ mkdir /local/ssd/dtool
    $ export DTOOL_CACHE_DIRECTORY=/local/ssd/dtool


.. warning:: There is no automatic mechanism built into dtool to clear up the
             cache. It can therefore grow very large if you are working with
             lots of datasets in object storage.
