Configuring storage brokers
===========================

Some remote storage brokers require extra configuration to enable
authentication.

The command below configures access to a Azure storage container named
``jicinformatics``::

    $ dtool config azure set jicinformatics the-secret-token
    the-secret-token

For information on other storage brokers have a look at their documentation
and/or use ``dtool config --help`` to get more information.
