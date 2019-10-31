Annotating datasets
===================

It is possible to annotate a dataset with so called key/value pairs. Such
key/value annotations are intended to make it easy to add and access specific
metadata at a per dataset level.

The difference between annotations and the descriptive metadata is that the
former is easier to work with in a programmatic fashion. The descriptive
metadata, stored in the dataset's README content, is more free form. It is
non-trivial to access specific pieces of information from the descriptive
metadata in the dataset's README content, whereas a dtool annotation can be
easily accessed by its name (key).

To create an annotation using the dtool CLI one would use the ``dtool annotation
set`` command. For example to annotate a dataset with a "project" one would use
the command::

    $ dtool annotation set <DS_URI> project world-peace

To access the "project" annotation one would use the ``dtool annotation get`` command::

    $ dtool annotation get <DS_URI> project
    world-peace

Annotations set using ``dtool annotation set`` are strings by default. It is possible
to set the type to ``int``, ``float``, and ``bool`` using the ``--type`` option. For
example to annotate a dataset with a "stars" rating one could use the command::

    $ dtool annotation set --type int <DS_URI> stars 3

For more complex data structures one can set the type to ``json``. For example::

    $ dtool annotation set --type json <DS_URI> params '{"x": 3.4, "y": 5.6}'

It is possible to list all the annotations of a dataset::

    $ dtool annotation ls
    params  {"x": 3.4, "y": 5.6}
    project world-peace
    stars   3

To update an annotation one can use the ``dtool annotation set`` command again.
For example to show that a dataset is really fantastic one could increase its
star rating to 5::

    $ dtool annotation set <DS_URI> stars 5 --type int
    $ dtool annotation get <DS_URI> stars
    5

.. warning::
    There are restrictions on the characters and the length of the keys. They have to
    match the regular expression ``^[a-zA-Z.-_]*$`` and it must be 80 characters or less.
