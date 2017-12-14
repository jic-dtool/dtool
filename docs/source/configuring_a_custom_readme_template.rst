Configuring a custom README template
====================================

When running the ``dtool interactive readme`` command one is prompted to enter
the default descriptive metadata shown below.

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

It is possible to configure the required metadata prompted for by the
``dtool readme interactive`` command. This requires the creation of a
README file making use of the YAML file format.

The default template is shown below.

.. code-block:: yaml

    ---
    description: Dataset description
    project: Project name
    confidential: False
    personally_identifiable_information: False
    owners:
      - name: {DTOOL_USER_FULL_NAME}
        email: {DTOOL_USER_EMAIL}
        username: {username}
    creation_date: {date}
    # links:
    #  - http://doi.dx.org/your_doi
    #  - http://github.com/your_code_repository
    # budget_codes:
    #  - E.g. CCBS1H10S

To create a custom template that also prompted for a species definition one
could create the file ``~/custom_dtool_readme.yml`` with the content below.

.. code-block:: yaml

    ---
    description: Dataset description
    project: Project name
    species: A. thaliana
    confidential: False
    personally_identifiable_information: False
    owners:
      - name: {DTOOL_USER_FULL_NAME}
        email: {DTOOL_USER_EMAIL}
        username: {username}
    creation_date: {date}

To enable this template one can make use of the ``DTOOL_README_TEMPLATE_FPATH`` environment variable::

    $ export DTOOL_README_TEMPLATE_FPATH=~/custom_dtool_readme.yml

Re-running the previous ``dtool readme interacitve`` command now includes a prompt for the species and the default value ``A. thaliana``::

    $ dtool readme interactive my_dataset
    description [Dataset description]:
    project [Project name]:
    species [A. thaliana]:
    confidential [False]:
    personally_identifiable_information [False]:
    name [Your Name]:
    email [you@example.com]:
    username [olssont]:
    creation_date [2017-12-14]:

Alternatively, one can add the ``DTOOL_README_TEMPLATE_FPATH`` key to the
``~/.config/dtool/dtool.json`` file.  For example,

.. code-block:: json

    {
       "DTOOL_README_TEMPLATE_FPATH": "/Users/olssont/custom_dtool_readme.yml"
    }

If the ``~/.config/dtool/dtool.json`` file does not exist one may need to
create it.
