CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^

[3.23.0] - 2020-02-28
---------------------

Added
^^^^^

- Add ``dtool readme validate`` command
- Ability to update descriptive metadata in README of frozen datasets
  when using ``dtool redme write``

Fixed
^^^^^

- Fixed several defects in how URIs were parsed and generated on Windows.


[3.22.0] - 2020-02-06
---------------------

Improved Python API for creating datasets.

Added
^^^^^

- dtoolcore.create_proto_dataset() helper function
- dtoolcore.create_derived_proto_dataset() helper function
- dtoolcore.DataSetCreator helper context manager class
- dtoolcore.DerivedDataSetCreator helper context manager class

Fixed
^^^^^

- Fixed defect where using ``DTOOL_NUM_PROCESSES`` > 1 resulted in
  a cPickle.PicklingError on some storage brokers. Multiprocessing
  is now only used if the storage broker supports it.


[3.21.1] - 2020-01-23
---------------------

- Fixed defect where 'dtool verify' calculated hashes even when the '-f/--full'
  option was not specified. The 'dtool verify' command now runs more quickly.


[3.21.0] - 2020-01-21
---------------------

Added
^^^^^

- Ability to use multiple processes (cores) to generate item properties for
  manifest files in parallel.  Set the environment variable
  ``DTOOL_NUM_PROCESSES`` to specify the number of processes to use.

Fixed
^^^^^

- Included .dtool/annotations directory in DiskStorageBroker self description file


[3.20.0] - 2019-10-31
---------------------

*New feature: Dataset annotation*

Dataset annotations are intended to make it easy to add and access specific
metadata at a per dataset level.

The difference between annotations and the descriptive metadata is that the
former is easier to work with in a programmatic fashion. The descriptive
metadata, stored in the dataset's README content, is more free form. It is
non-trivial to access specific pieces of information from the descriptive
metadata in the dataset's README content, whereas a dtool annotation can be
easily accessed by its name.

Added
^^^^^

- Added ``dtool annotation set`` command
- Added ``dtool annotation get`` command
- Added ``dtool annotation ls`` command


[3.19.0] - 2019-09-12
---------------------

Added
^^^^^

- Added sorting of items by relpath to 'dtool ls <DS_URI>'

Fixed
^^^^^

- Fixed formatting of 'dtool ls <DS_URI>' from using two whitespaces to using
  one tab to make it easier to work with command line tools such as ``cut``
- Fixed ordering of lines in overlay CSV template from being sorted by the
  identifier to being ordered by the relpath


[3.18.0] - 2019-09-06
---------------------

Added
^^^^^

- Added 'dtool overlays show' command
- Added 'dtool overlays write' command
- Added 'dtool overlays template parse' command
- Added 'dtool overlays template glob' command
- Added 'dtool overlays template pairs' command


Deprecated
^^^^^^^^^^

- Deprecated 'dtool overlay ls'
- Deprecated 'dtool overlay show'


[3.17.0] - 2019-08-06
---------------------

Added
^^^^^

- Added support for host name in file URI.
- Added ``dtool status`` command for working out if a dataset is frozen or not
- Added ``dtool uri`` command for expanding absolute and relative paths into
  proper URIs


[3.16.0] - 2019-07-12
---------------------

Added
^^^^^

- Added more debug logging
- Added ``dtool config ecs ls`` command to list ECS base URIs that have been
- Added support for configuring access to ECS buckets in multiple namespaces

Fixed
^^^^^

- The ``dtool config azure ls`` command now returns base URIs rather than
  container names


[3.15.0] - 2019-04-26
---------------------

Added
^^^^^

- ``dtool config readme-template`` CLI command for configuring the path to a
  custom readme template
- ``dtoolcore._BaseDataSet.base_uri`` property
- ``dtoolcore.storagebroker.BaseStorageBroker.generate_base_uri`` method
- ``dtoolcore.utils.DEFAULT_CACHE_PATH`` global helper variable
- ``dtoolcore.utils.get_config_value_from_file`` helper function
- ``dtoolcore.utils.write_config_value_to_file`` helper function


Changed
^^^^^^^

- ``dtool config cache`` now works with one unified cache directory for all
  storage brokers
- Started using unified environment variable to specify the cache directory
  ``DTOOL_CACHE_DIRECTORY``
- Default cache directory changed set to ``~/.cache/dtool``

Fixed
^^^^^

- Fixed defect  when username was supplied as two separate strings to
  ``dtool config user name`` in CLI


[3.14.1] - 2018-12-12
---------------------

Fixed
^^^^^

- Fixed the ``dtool config azure set`` help text


[3.14.0] - 2018-11-21
---------------------

Added
^^^^^

- Added ``dtool publish`` command
- Added ``-f/--format`` option to ``dtool summary`` command to enable output in
  JSON format
- Added sorting of CSV/TSV/HTML inventories by dataset name


Changed
^^^^^^^

- Changed default output of ``dtool summary`` to be human readable YAML


[3.13.0] - 2018-11-13
---------------------

Added
^^^^^

- Added support for Windows!   :)
- Added ``dtool config`` command




[3.12.0] - 2018-09-25
---------------------

Added
^^^^^

- Added ``dtool uuid`` command
- Added ``dtool item relpath`` command


[3.11.0] - 2018-09-20
---------------------

Added
^^^^^

- ``dtool cp`` to replace ``dtool copy``
- ``dtool readme write`` to write readme from file or stdin
- ``dtool item overlay`` command


Deprecated
^^^^^^^^^^

- ``dtool copy`` in favour of ``dtool cp``


Removed
^^^^^^^

- Removed ``created_at`` field from default README template


Fixed
^^^^^

- Defect in ``dtool create`` when providing a relative path to the
  ``--symlink-path`` option
- Python 2 defect in dealing with unicode in README.yml file when using
  ``dtool readme edit``


[3.10.0] - 2018-09-11
---------------------

Added
^^^^^

- ``dtoolcore.filehasher.hashsum_digest`` helper function
- ``dtoolcore.filehasher.md5sum_digest`` helper function


Changed
^^^^^^^

- Improved name from ``dtoolcore.filehasher.hashsum`` to
  ``dtoolcore.filehasher.hashsum_hexdigest``

Fixed
^^^^^

- Deal with issue in how ruamel.yaml deals with float values



[3.9.0] - 2018-08-03
--------------------

Added
^^^^^

- Added ability to update the name of a frozen dataset from the ``dtool`` CLI
- Added ``update_name`` method to ``DataSet`` class (previously only available
  on ``ProtoDataSet`` class)


[3.8.0] - 2018-07-31
--------------------

Dataset name validation.

Added
^^^^^

- ``dtoolcore.generate_admin_metadata`` function raises
  ``dtoolcore.DtoolCoreInvalidNameError`` if invalid name is provided
- ``dtoolcore.utils.name_is_valid`` utility function for checking sanity of
  dataset names
- Validation of dataset name upon creation using dtool CLI
- Validation of dataset name when updating it using dtool CLI

Fixed
^^^^^

- Fixed defect where ``dtool ls -q`` was listing dataset names rather than URIs
  making it impossible to process datasets in a BASE_URI programatically
- Make ``SymlinkStorageBroker`` compatible with dtoolcore 3.4.0


[3.7.0] - 2018-07-26
--------------------

Storage broker base class redesign and refactoring.

Added
^^^^^

- Ability to update descriptive metadata in README of frozen datasets
- Validation that the descriptive metadata provided by the
  ``dtool readme edit`` command is valid YAML
- Added ``dtoolcore.storagebroker.BaseStorageBroker``
- Added logging to the reusable ``BaseStorageBroker`` methods
- ``get_text`` new method on ``BaseStorageBroker`` class
- ``put_text`` new method on ``BaseStorageBroker`` class
- ``get_admin_metadata_key`` new method on ``BaseStorageBroker`` class
- ``get_readme_key`` new method on ``BaseStorageBroker`` class
- ``get_manifest_key`` new method on ``BaseStorageBroker`` class
- ``get_overlay_key`` new method on ``BaseStorageBroker`` class
- ``get_structure_key`` new method on ``BaseStorageBroker`` class
- ``get_dtool_readme_key`` new method on ``BaseStorageBroker`` class
- ``get_size_in_bytes`` new method on ``BaseStorageBroker`` class
- ``get_utc_timestamp`` new method on ``BaseStorageBroker`` class
- ``get_hash`` new method on ``BaseStorageBroker`` class
- ``get_relpath`` new method on ``BaseStorageBroker`` class
- ``update_readme`` new method on ``BaseStorageBroker`` class
- ``DataSet.put_readme`` method that can be used to update descriptive metadata
   in (frozen) dataset README whilst keeping a copy of the historical README
   content
- Add ``storage_broker_version`` key to structure parameters

Fixed
^^^^^

- Stop ``copy_resume`` function calculating hashes unnecessarily
- Fixed the documentation of the ``dtool verify`` command


[3.6.2] - 2018-07-10
--------------------

Fixed
^^^^^

- Default config file now set in ``dtoolcore.utils.get_config_value`` if not provided in caller 


[3.6.1] - 2018-07-09
--------------------

Fixed
^^^^^

- Made download to DTOOL_HTTP_CACHE_DIRECTORY more robust
- Added ability to deal with redirects to enable working with shortened URLs


[3.6.0] - 2018-07-05
--------------------

Added
^^^^^

- Bundling of ``dtool-http`` package

Removed
^^^^^^^

- Bundling of ``dtool-irods`` package
- Bundling of ``dtool-s3`` package


[3.5.0] - 2018-06-06
--------------------

Added
^^^^^

- Pre-checks to 'dtool freeze' command to ensure that there is no rogue content
  in the base of disk datasets
- Added rogue content validation check to DiskStorageBroker.pre_freeze hook


[3.4.0] - 2018-05-24
--------------------

Added
^^^^^

- Pre-checks to 'dtool freeze' command to ensure that the item handles are sane, i.e. that they do not contain newline characters
- Pre-checks to 'dtool freeze' command to ensure that there are not too many items in the proto dataset, default to less than 10000


[3.3.1] - 2018-05-18
--------------------

Fixed
^^^^^

- Defect where inventory html template is not included in Python package on PyPi


[3.3.0] - 2018-05-18
--------------------

Added
^^^^^

- Add "created_at" key to the administrative metadata
- ``dtool inventory`` command for generating csv/tsv/html inventories of collections
  of datasets
- Added support for ``-h`` flag as well as ``--help``
- Added timestamp to logging output

Fixed
^^^^^

- Improved handling of URIs in validation code
- Fixed defect where running ``dtool item properties`` with an invalid identifier
  resulted in a KeyError exception being propagated to the user
- Fixed defect where ``dtool verify`` did not compare file sizes
- Fixed timestamp defect in DiskStoragBroker


[3.2.1] - 2018-05-01
--------------------

Fixed
^^^^^

- Fixed issue arising from a file being put into iRODS and the connection
  breaking before the appropriate metadata could be set on the file in iRODS.
  See also: https://github.com/jic-dtool/dtool-irods/issues/7


[3.2.0] - 2018-02-09
--------------------

Release to make it easier to create symlink datasets in an automated fashion.

Changed
^^^^^^^

- Simplified the way to specify the symbolic link path in the
  SymLinkStorageBroker
- The path to the data when creating a symlink dataset is now specified using the
  ``-s/--symlink-path`` option rather than being something that is prompted for.
  This makes it easier to create symlink datasets in an automated fashion.


[3.1.0] - 2018-02-05
--------------------

Added
^^^^^

- ``--resume`` option to ``dtool copy`` command
- ``--quite`` and ``--verbose`` options to ``dtool ls`` and improved formatting
- Add ``dtoolcore.copy_resume`` function


[3.0.0] - 2018-01-18
--------------------

This release makes use of the dtoolcore version 3.0.0 API, which improves the
handling of URIs and adds more metadata describing the structure of datasets.

Another major feature of this release is the addition of an S3 storage broker
that can be used to interact with Amazon's S3 object storage.

Added
^^^^^

- AWS S3 object storage broker
- Writing of ``.dtool/structure.json`` file to the DiskStorageBroker; a file
  for describing the structure of the dtool dataset in a computer readable format
- Writing of ``.dtool/README.txt`` file to the DiskStorageBroker; a file
  for describing the structure of the dtool dataset in a human readable format
- Writing of ``.dtool/structure.json`` file to the IrodsStorageBroker; a file
  for describing the structure of the dtool dataset in a computer readable format
- Writing of ``.dtool/README.txt`` file to the IrodsStorageBroker; a file
  for describing the structure of the dtool dataset in a human readable format


Changed
^^^^^^^

- Make use of dtoolcore version 3 API


Fixed
^^^^^

- Removed the historical ``dtool_readme`` key/value pair from the
  administrative metadata (in the .dtool/dtool file)


[2.4.0] - 2017-12-14
--------------------

Added
^^^^^

- Ability to specify a custom README.yml template file path.
- Ability to configure the full user name for the README.yml template using
  ``DTOOL_USER_FULL_NAME``

Fixed
^^^^^

- Made ``.dtool/manifest.json`` content created by DiskStorageBroker human
  readable by adding new lines and indentation to the JSON formatting.
- Made the DiskStorageBroker.list_overlay_names method more robust. It no
  longer falls over if the ``.dtool/overlays`` directory has been lost, i.e. by
  cloning a dataset with no overlays from a Git repository.
- Fixed defect where an incorrect URI would get set on the dataset when using
  ``DataSet.from_path`` class method on a relative path
- Made the YAML output more pretty by adding more indentation.
- Replaced hardcoded ``nbi.ac.uk`` email with configurable ``DTOOL_USER_EMAIL``
  in the default README.yml template.
- Fixed ``IrodsStorageBroker.generate_uri`` class method
- Made ``.dtool/manifest.json`` content created by IrodsStorageBroker human
  readable by adding new lines and indentation to the JSON formatting.
- Added rule to catch ``CAT_INVALID_USER`` string for giving a more informative
  error message when iRODS authentication times out



[2.3.2] - 2017-10-25
--------------------

Fixed
^^^^^

- Fixed issue where the symbolic link was not fully resolved when creating
  a symlink dataset that used the terminal to prompt for the data directory


[2.3.1] - 2017-10-25
--------------------

Fixed
^^^^^

- More graceful exit if one presses Cancel in file browser when creating a
  symlink dataset
- Data directory now falls back on click command line prompt if TkInter has
  issues when creating a symlink dataset


[2.3.0] - 2017-10-23
--------------------

Added
^^^^^

- ``pre_freeze_hoook`` to the stroage broker interface called at the beginning
  of ``ProtoDataSet.freeze`` method.
- ``--quiet`` flag to ``dtool create`` command
- ``dtool overlay ls`` command to list the overlays in dataset
- ``dtool overlay show`` command to show the content of a specific overlay


Changed
^^^^^^^

- Improved speed of freezing a dataset in iRODS by making use of
  caches to reduce the number of calls made to iRODS during this
  process
- ``dtool copy`` now specifies target location using URI rather than
  using the ``--prefix`` and ``--storage`` arguments


Fixed
^^^^^

- Made the ``DiskStorageBroker.create_structure`` method more robust
- More informative error message when iRODS has not been configured
- More informative error message when iRODS authentication times out
- Stopped client hanging when iRODS authentication has timed out
- storagebroker's ``put_item`` method now returns relpath
- Made the ``IrodsStorageBroker.create_structure`` method more
  robust by checking if the parent collection exists
- Made error handling in ``dtool create`` more specific
- Added propagation of original error message when ``StorageBrokerOSError``
  captures in ``dtool create``


[2.2.0] - 2017-10-09
--------------------


Added
^^^^^

- ``dtool ls`` can now be used to list the relpaths of the items in a dataset
- ``-f/--full`` flag to ``dtool diff`` command to include checking of file
  hashes  
- ``-f/--full`` flag to ``dtool verify`` command to include checking of file
  hashes  


Changed
^^^^^^^

- ``dtool ls`` now works with URIs rather than with prefix and storage arguments
- ``dtool diff`` now only compares identifiers and file sizes by default
- ``dtool verify`` now only compares identifiers and file sizes by default


Fixed
^^^^^

- Made ``DiskStorageBroker.list_dataset_uris`` class method more robust


[2.1.2] - 2017-10-05
--------------------

Fixed
^^^^^

- Set the correct dependency to actually get fix reported in 2.1.1

[2.1.1] - 2017-10-05
--------------------

Fixed
^^^^^

- Fixed defect in iRODS storage broker where files with white space resulted in
  broken identifiers


[2.1.0] - 2017-10-04
--------------------

Added
^^^^^

- ``dtool readme show`` command that returns the readme content
- ``--quiet`` flag to ``dtool copy`` command

Changed
^^^^^^^

- Improved the ``dtool readme --help`` output

Fixed
^^^^^

- Progress bar now shows information on individual items being processed
- ``dtool ls`` now works with relative paths
- Fix defect where ``IrodsStorageBroker.put_item`` raised SystemError when
  trying to overwrite an existing file


[2.0.2] - 2017-09-25
--------------------

Fixed
^^^^^

- Better validation of input in terms of base vs proto vs frozen dataset URIs
- Fixed bug where copy creates an intermediate proto dataset that self
  identifies as a frozen dataset.
- Fixed potential bug where a copy could convert a proto dataset to
  a dataset before all its overlays had been copied over
- Fixed type of "frozen_at" time stamp in admin metadata: from string to float


[2.0.1] - 2017-09-20
--------------------

Fixed
^^^^^

- Made version requirements of dtool sub-packages explicit

[2.0.0] - 2017-09-14
--------------------

Initial release of ``dtool`` as a meta package.
