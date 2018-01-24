Configuring storage brokers
===========================

Some remote storage brokers require extra configuration, for example to enable
authentication. Remote storage brokers may also provide a means to alter the
local cache directory where files are fetched to, e.g. using the ``dtool item
fetch`` command.

One can provide these configurations by exporting relevant environment variables.
For example::

    $ export DTOOL_IRODS_CACHE_DIRECTORY=/tmp/dtool/irods 
    $ export DTOOL_S3_CACHE_DIRECTORY=/tmp/dtool/s3 

Alternatively, if using the ``dtool`` command line interface one can set these
variables in the file ``~/.config/dtool/dtool.json``. For example,

.. code-block:: json

    {
       "DTOOL_IRODS_CACHE_DIRECTORY": "/tmp/dtool/irods"
       "DTOOL_S3_CACHE_DIRECTORY": "/tmp/dtool/s3"
    }

One may need to create this file if it does not already exist.

See the documentation of specific storage brokers to find out what configuration
options are available.
