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
