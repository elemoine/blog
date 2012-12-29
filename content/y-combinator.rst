Y Combinator
############
:date: 2009-07-02 19:08
:author: Erilem
:category: Uncategorized
:tags: functional programming, python

I've been reading "The Little Schemer" from Daniel P. Friedman and
Matthias Felleisen. Very interesting reading.

.. raw:: html

   </p>

The nineth chapter introduces the Y Combinator function, a pretty
interesting beast! Quoting `Crockford`_: "one of the most strange and
wonderful artifacts of Computer Science". As a primer, here's how the Y
Combinator looks like (in Python):

.. raw:: html

   <p>

::

    def Y(func):    return (lambda f : f(f))     (lambda f : func(          lambda x : (f(f))(x)))

.. raw:: html

   </p>

Looks scary, doesn't it? (It did scare me when I first saw it at least.)

.. raw:: html

   </p>

The Y Combinator creates a recursive function from a non-recursive
function that looks like the recursive function one wants to create. The
Y Combinator can for example be used to obtain recursive functions from
anonymous functions, which, with most programming languages, cannot be
recursive.

.. raw:: html

   </p>

This blog post proposes defining the Y Combinator function in Python.

.. raw:: html

   </p>

Goal: find the function Y (the Y Combinator) such that

.. raw:: html

   <p>

::

    fact = Y(like_fact)

.. raw:: html

   </p>

where:

-  fact is the factorial function
-  like\_fact is defined as follows:

.. raw:: html

   </p>

.. raw:: html

   <p>

::

    def like_fact(r):    def f(n):        if n < 2:            return 1        else:            return n * r(n - 1)    return f

.. raw:: html

   </p>

So Y takes a non-recursive function (which can theoritically be
expressed as an anonymous function) that looks like the recursive
factorial function and returns the factorial function.

.. raw:: html

   </p>

You may have noticed thay our like\_fact function is not expresed as an
anonymous function. This is because Python does not allow us to do it:
the inner function f cannot be defined with lambda because it includes
conditional statements, the outer function like\_fact cannot be defined
with lambda because it includes an inner function that isn't defined
with lambda. Using JavaScript the like\_fact function would be:

.. raw:: html

   <p>

::

    function(r) {    return function(n) {        return n < 2 ? 1 : n * r(n - 1);    };}

.. raw:: html

   </p>

.. raw:: html

   </p>

We start our demonstration from the following statement:

.. raw:: html

   <p>

::

    fact = notlike_fact(notlike_fact)

.. raw:: html

   </p>

where notlike\_fact is:

.. raw:: html

   <p>

::

    def notlike_fact(r):    def f(n):        if n < 2:            return 1        else:            return n * (r(r))(n - 1)    return f

.. raw:: html

   </p>

.. raw:: html

   </p>

Now we rewrite the above statement using lambda:

.. raw:: html

   <p>

::

    fact = (lambda f : f(f))          (notlike_fact)

.. raw:: html

   </p>

.. raw:: html

   </p>

Now we can extract like\_fact and rewrite the statement as (maybe the
most difficult step):

.. raw:: html

   <p>

::

    (lambda f : f(f)) (lambda f : like_fact(      lambda x : (f(f)(x)))

.. raw:: html

   </p>

.. raw:: html

   </p>

We can now write the Y function:

.. raw:: html

   <p>

::

    def Y(func):    return (lambda f : f(f))     (lambda f : func(          lambda x : (f(f))(x)))

.. raw:: html

   </p>

And we have:

.. raw:: html

   <p>

::

    fact = Y(like_fact)assert fact(1) == 1assert fact(2) == 2assert fact(3) == 6assert fact(4) == 24assert fact(5) == 120

.. raw:: html

   </p>

Cool, no?

.. raw:: html

   </p>

Obviously Y applies to other recursive functions, as an example let's
apply it to Fibonacci:

.. raw:: html

   <p>

::

    def like_fibo(r):    def f(n):        if n <= 2:            return 1        else:            return r(n - 1) + r(n - 2)    return ffibo = Y(like_fibo)assert fibo(1) == 1assert fibo(2) == 1assert fibo(3) == 2assert fibo(4) == 3assert fibo(5) == 5assert fibo(6) == 8

.. raw:: html

   </p>

.. raw:: html

   </p>

.. _Crockford: http://www.crockford.com/javascript/little.html
