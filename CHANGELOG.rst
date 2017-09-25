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
