Function decorators in JavaScript
#################################
:date: 2010-08-02 06:42
:author: Erilem
:category: Uncategorized

I've been looking at how to implement function decorators in JavaScript.
The FireFox Sync extension (`http://hg.mozilla.org/services/fx-sync`_)
provides a nice implementation. I'm going to describe that
implementation in this post.

So let's assume we have an application with "classes" (constructors and
prototypes, really), and we always want the same behavior when
exceptions occur in these classes' methods.

Our classes look like:

.. raw:: html

   <p>

::

    MyCtor = function() {};MyCtor.prototype = {    method: function(a, b) {        // do something with a and b    }};

.. raw:: html

   </p>

The common behavior is implemented at a single place in a decorator
function:

.. raw:: html

   <p>

::

    var decorators = {    catch: function(f) {        return function() {            try {                f();            } catch(e) {                console.log(e);            }        };    }};

.. raw:: html

   </p>

``decorators.catch`` is the decorator function. It returns a function
that executes the decorated function (``f``) in a try/catch block and
logs a message if an exception occurs.

Decorating ``method`` with decorators.catch is done as follows:

.. raw:: html

   <p>

::

    MyCtor.prototype = {    method: function(a, b)        decorators.catch(function() {            // do something with a and b        })()};

.. raw:: html

   </p>

``method`` now calls our decorator, and the actual logic of the method

is moved in an anonymous function passed to the decorator. The anonymous
function can still access the arguments ``a`` and ``b`` thanks to the
closure.

You may be wondering why ``decorators.catch`` delegates the decoration
to an inner function as opposed to doing it itself. This is to be able
to chain decoration. For example:

.. raw:: html

   <p>

::

     MyCtor.prototype = {    method: function(a, b)        decorators.lock(decorators.catch(function() {            // do something with a and b        }))()};

.. raw:: html

   </p>

where ``decorators.lock`` would be a new decorator of ours.

I guess there are other ways to implement function decorators in
JavaScript. I find this one is simple and elegant.

.. _`http://hg.mozilla.org/services/fx-sync`: http://hg.mozilla.org/services/fx-sync
