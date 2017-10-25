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
