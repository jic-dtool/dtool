Configuring storage brokers
===========================

Some remote storage brokers require extra configuration, for example to enable
authentication.


The command below configures access to a Azure storage container named ``jicinformatics``::

    $ dtool config azure get jicinformatics the-secret-token
    the-secret-token


Remote storage brokers may also provide a means to alter the local cache
directory where files are fetched to, e.g. using the ``dtool item fetch``
command. The command below sets the local cache directory for all storage brokers to ``/tmp/dtool``.

    $ mkdir /tmp/dtool
    $ dtool config cache set_all /tmp/dtool
    azure     /tmp/dtool
    http      /tmp/dtool
    s3        /tmp/dtool
    ecs       /tmp/dtool
    irods     /tmp/dtool


One can override these configurations by exporting relevant environment variables.

For example::

    $ export DTOOL_AZURE_CACHE_DIRECTORY=/tmp/dtool/azure 
    $ export DTOOL_IRODS_CACHE_DIRECTORY=/tmp/dtool/irods 
    $ export DTOOL_S3_CACHE_DIRECTORY=/tmp/dtool/s3 
    $ export DTOOL_ECS_CACHE_DIRECTORY=/tmp/dtool/ecs 
