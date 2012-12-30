Y Combinator
############
:date: 2009-07-02 19:08
:author: Erilem
:tags: functional programming, python

I've been reading "The Little Schemer" from Daniel P. Friedman and
Matthias Felleisen. Very interesting reading.

The nineth chapter introduces the Y Combinator function, a pretty
interesting beast! Quoting `Crockford`_: "one of the most strange and
wonderful artifacts of Computer Science". As a primer, here's how the Y
Combinator looks like (in Python):

.. code-block:: python

    def Y(func):
        return (lambda f : f(f))(lambda f : func(lambda x : (f(f))(x)))

Looks scary, doesn't it? (It did scare me when I first saw it at least.)

The Y Combinator creates a recursive function from a non-recursive
function that looks like the recursive function one wants to create. The
Y Combinator can for example be used to obtain recursive functions from
anonymous functions, which, with most programming languages, cannot be
recursive.

This blog post proposes defining the Y Combinator function in Python.

Goal: find the function Y (the Y Combinator) such that::

    fact = Y(like_fact)

where:

-  ``fact`` is the factorial function
-  ``like_fact`` is defined as follows:

.. code-block:: python

    def like_fact(r):
        def f(n):
            if n < 2:
                return 1
            else:
                return n * r(n - 1)
        return f

So ``Y`` takes a non-recursive function (which can theoritically be expressed
as an anonymous function) that looks like the recursive factorial function and
returns the factorial function.

You may have noticed thay our ``like_fact`` function is not expresed as an
anonymous function. This is because Python does not allow us to do it: the
inner function ``f`` cannot be defined with ``lambda`` because it includes
conditional statements, the outer function ``like_fact`` cannot be defined with
``lambda`` because it includes an inner function that isn't defined with
``lambda``.

Using JavaScript the ``like_fact`` function would be:


.. code-block:: javascript

    function(r) {
        return function(n) {
            return n < 2 ? 1 : n * r(n - 1);
        };
    }


We start our demonstration from the following statement:

.. code-block:: python

    fact = notlike_fact(notlike_fact)

where ``notlike_fact`` is:

.. code-block:: python

    def notlike_fact(r):
        def f(n):
            if n < 2:
                return 1
            else:
                return n * (r(r))(n - 1)
        return f

Now we rewrite the above statement using ``lambda``:

.. code-block:: python

    fact = (lambda f : f(f))(notlike_fact)

Now we can extract ``like_fact`` and rewrite the statement as (maybe the
most difficult step):

.. code-block:: python

    (lambda f : f(f)) (lambda f : like_fact(lambda x : (f(f)(x)))

We can now write the Y function:

.. code-block:: python

    def Y(func):
        return (lambda f : f(f))(lambda f : func(lambda x : (f(f))(x)))

And we have:

.. code-block:: python

    fact = Y(like_fact)
    assert fact(1) == 1
    assert fact(2) == 2
    assert fact(3) == 6
    assert fact(4) == 24
    assert fact(5) == 120

Cool, no?

Obviously ``Y`` applies to other recursive functions, as an example let's apply
it to Fibonacci:

.. code-block:: python

    def like_fibo(r):
        def f(n):
            if n <= 2:
                return 1
            else:
                return r(n - 1) + r(n - 2)
        return f
    
    fibo = Y(like_fibo)
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(3) == 2
    assert fibo(4) == 3
    assert fibo(5) == 5
    assert fibo(6) == 8

.. _Crockford: http://www.crockford.com/javascript/little.html
