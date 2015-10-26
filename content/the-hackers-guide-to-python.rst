Things learned from "The Hacker's Guide To Python"
##################################################
:date: 2015-10-25 10:39
:author: Erilem
:tags: Python, Book

I just finished reading Julien Danjou's "The Hacker's Guide To Python" book,
which I enjoyed a lot. This blog post is not a book review, just a summary on
things I learned from the book.

Distribution
------------

The "Distribution" chapter mentions the `pbr
<http://docs.openstack.org/developer/pbr/>`_ tool. ``pbr`` was inspired by
``distutils2``, which is now abandonned.

Using ``pbr`` the package developer describes the package in a ``setup.cfg``
file and the use the following in ``setup.py``:

.. code-block:: python

    import setuptools

    setuptools.setup(setup_requires=['pbr'], pbr=True)

But ``pbr`` offers more features than this, including reading dependencies from
``requirements.txt``,  generating ``autodoc`` stub files, generating
``AUTHORS`` and ``ChangeLog`` files from ``git log``, reading the
``long_description`` from the project's ``README`` file, managing version
numbers based on Git tags and revisions.

``pbr`` was initially developed inside the OpenStack project, but it sounds
like it can be useful for other Python projects. I'll consider it in the
future.

Unit Testing
------------

The "Unit Testing" chapter covers well-known test-related tools and libraries
like `unittest <https://docs.python.org/3/library/unittest.html>`_ , `mock
<https://docs.python.org/dev/library/unittest.mock.html>`_, `nose
<http://nose.readthedocs.org/en/latest/>`_, and `fixtures
<https://pypi.python.org/pypi/fixtures>`_.  It also covers other interesting
tools that I didn't know before, namely `subunit
<https://pypi.python.org/pypi/python-subunit>`_ and `testrepository
<http://testrepository.readthedocs.org/en/latest/>`_.

``subunit`` is a Python module that provides a streaming protocol for test
results. Using ``subunit`` test results may be aggregated from different from
different machines. Test runs may be recorded and replayed later.

The ``testrepository`` package makes it possible to store a ``subunit`` stream
and then manipulate it using the ``testr`` command. Here is a quick example:

.. code-block:: shell

    $ cd my_python_package
    $ testr init
    $ touch .testr.conf
    $ python -m subunit.run tests.test_functions | testr load
    Ran 4 tests in 0.002s
    PASSED (id=0)
    $ testr failing
    PASSED (id=0)
    $ testr last
    Ran 4 tests in 0.002s
    PASSED (id=0)
    $ testr stats
    runs=1

This only scratches the surface of what can be done with ``subunit`` and
``testrepository``. For example ``testrepository`` has support for running
tests in parallel, in isolated environments such as chroots, containers or
separate machines. I need to do more research to fully understand the
benefits of using ``subunit`` and ``testrepository``.

Methods and decorators
----------------------

Bound/Unbound methods
~~~~~~~~~~~~~~~~~~~~~

The "Methods and decorators" chapter of the book includes a section explaining
"how methods work in Python".

I've learned from this section that, in contrast to Python 2, Python 3 allows
passing any object to an *unbound* method. Let's consider this simple class for
example:

.. code-block:: python

    class Python(object):
        def __init__(self, version):
            self.version = version
        def get_version(self):
            return self.version

The following works both with Python 2 and 3:

.. code-block:: python

    Python.get_version(Python(3))

But the following only works with Python 3:

.. code-block:: python

    from collections import namedtuple
    PythonLike = namedtuple('PythonLike', ['version'])

    Python.get_version(PythonLike(3))

With Python 2 the (unbound) ``get_version`` function must be called with
a ``Python`` instance as its first argument. While with Python 3 the
``get_version`` function may be called with any object with a ``version``
property. So Python 3 is more permissive and flexible here.

``super()`` is your friend
~~~~~~~~~~~~~~~~~~~~~~~~~~

The "Methods and decorators" chapter also includes a section "The truth about
**super**" that I found… intriguing. So I went back to the roots, and (re-)read
the official docs for `super()
<https://docs.python.org/3/library/functions.html#super>`_. The official docs
include a link to a very informative `blog post
<https://rhettinger.wordpress.com/2011/05/26/super-considered-super/>`_ about
``super()``. Read that blog post and you'll understand that the type to which
``super()`` delegates is computed at runtime.  This will explain why you should
always use ``super()``.

The AST
-------

The "The AST" chapter talks about Python's Abstract Syntax Tree, and presents
the ``ast`` module, which applications may use to create and process trees of
the Python abstract syntax grammar.

Two practical cases are presented.

First the author teaches us how to use ``ast`` to create an a `flake8
<https://flake8.readthedocs.org/en/2.4.1/>`_ extension. The extension checks
that each method not decorated with ``@staticmethod`` has at least of one
argument, and that the method actually uses its first argument. If the first
argument is not used then it means that function should be decorated with
``@staticmethod``. Check out this `blog post from Julien
<https://julien.danjou.info/blog/2015/python-ast-checking-method-declaration>`_
if you want to know more about that extension. The blog post covers it all.

The other practical case presented is nothing more than the `Hy Programming
Language <http://docs.hylang.org/en/latest/language/index.html>`_. Hy is a Lisp
dialect that parses a Lisp-like language and converts it to a standard Python
AST. Hy is very cool! It's a good way for Python developers to discover Lisp.

Guess what the following Hy program does:

.. code-block:: lisp

    (list-comp
      (, x y)
      (x (range 8)
       y "ABCDEFGH"))

Performances and optimizations
------------------------------

The "Performance and optimizations" chapter includes a section discussing
*slots* and ``Namedtuple``.

You may know that you can use *slots* to save memory:

.. code-block:: python

    class Point(object):
        __slots__ = ('x', 'y')
        def __init__(self, x, y):
            self.x = x
            self.y = y

``__slots__`` lists the properties allowed for instances of the class. When
slots are defined the object attributes are stored in a list instead of the
``__dict__`` dictionary, which saves memory.

I knew all this already. What I didn't know is that types created with the
``namedtuple()`` factory have ``__slots__`` set to ``()`` (the empty tuple).
So using a named tuple type is almost as efficient as using a class with
``__slots__`` in terms of memory usage.

.. code-block:: python

    from collections import namedtuple

    Point = namedtuple('Point', ['x', 'y'])
    assert Point.__slots__ is ()

RDBMS and ORM
-------------

The "RDBMS and ORM" shows how to "stream data with Flask and PostgreSQL".  More
specifically this demonstrates how to use PostgreSQL's `NOTIFY
<http://www.postgresql.org/docs/current/static/sql-notify.html>`_ and `LISTEN
<http://www.postgresql.org/docs/current/static/sql-listen.html>`_ commands
together with `server-sent events
<https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events>`_
(SSE) in a `Flask <http://flask.pocoo.org/>`_ project to push data to the browser.
What's nice is to see how PostgreSQL, SSE and Flask make this easy and
straightforward!
