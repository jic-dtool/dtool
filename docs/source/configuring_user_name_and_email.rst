Configuring user name and email
===============================

When running the ``dtool interactive readme`` the default name and email
address are ``Your Name`` and ``you@example.com``.

::

    $ dtool readme interactive my_dataset
    description [Dataset description]:
    project [Project name]:
    confidential [False]:
    personally_identifiable_information [False]:
    name [Your Name]:
    email [you@example.com]:
    username [olssont]:
    creation_date [2017-12-14]:

These defaults can be configured by setting the ``DTOOL_USER_FULL_NAME``
``DTOOL_USER_EMAIL`` environment variables.

::

    $ export DTOOL_USER_FULL_NAME="Care A. Bout-Data"
    $ export DTOOL_USER_EMAIL=researcher@famous.uni.ac.uk

Rerunning the previous ``dtool readme interactive`` command now gives updated
defaults when prompting for input.

::

    $ dtool readme interactive my_dataset
    description [Dataset description]:
    project [Project name]:
    confidential [False]:
    personally_identifiable_information [False]:
    name [Care A. Bout-Data]:
    email [researcher@famous.uni.ac.uk]:
    username [olssont]:
    creation_date [2017-12-14]:

It may therefore be useful to add the export commands above to ones ``.bashrc``
file.

Alternatively, one can add the ``DTOOL_USER_FULL_NAME`` and
``DTOOL_USER_EMAIL`` keys to the ``~/.config/dtool/dtool.json`` file.  For
example,

.. code-block:: json

    {
       "DTOOL_USER_FULL_NAME": "Care A. Bout-Data",
       "DTOOL_USER_EMAIL": "researcher@famous.uni.ac.uk"
    }

If the ``~/.config/dtool/dtool.json`` file does not exist one may need to
create it.
