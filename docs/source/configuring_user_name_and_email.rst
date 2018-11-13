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

These defaults can be configuring the user name and email address.

::

    $ dtool config user name "Care A. Bout-Data"
    Care A. Bout-Data
    $ dtool config user email researcher@famous.uni.ac.uk
    researcher@famous.uni.ac.uk

    

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
