Secure TileCache With Pylons and Repoze
#######################################
:date: 2009-02-15 18:14
:author: Erilem
:category: Uncategorized

This post shows how one can secure TileCache with Pylons and Repoze.

In a Pylons application one can run a WSGI application from within a
controller action. Here is a simple example:

.. raw:: html

   <p>

::

        class MainController(BaseController)        def action(self, environ, start_response):            return wsgiApp(environ, start_response)

.. raw:: html

   </p>

`TileCache`_ is commonly run from within ``mod_python``. TileCache can
also be run as a WSGI application, therefore it can be run from within
the controller action of a Pylons application. Here's how:

.. raw:: html

   <p>

::

        from TileCache.Service import wsgiApp    class MainController(BaseController)        def tilecache(self, environ, start_response):            return wsgiApp(environ, start_response)

.. raw:: html

   </p>

Pretty cool... But it gets really interesting when *repoze.what* is
added to the picture. For those who don't know repoze.what, repoze.what
is an authorization framework for WSGI applications. repoze.what now
provides a Pylons `plugin`_, making it easy to protect controllers and
controller actions in a Pylons application. Here's how our tilecache
action can be protected:

.. raw:: html

   <p>

::

        from TileCache.Service import wsgiApp    from repoze.what.predicates import has_permission    from repoze.what.plugins.pylonshq import ActionProtector    class MainController(BaseController)        @ActionProtector(has_permission('tilecache'))        def tilecache(self, environ, start_response):            return wsgiApp(environ, start_response)

.. raw:: html

   </p>

With the above, anyone who tries to access ``/tilecache`` will have to
be granted the *tilecache* permission. Otherwise, authorization will be
denied.

TileCache is secured!

People often want finer-grained authorization, like give certain users
access to certain layers. With Pylons' routing system this can be easily
and elegantly achieved using repoze.what, I will show that in a later
post.

.. _TileCache: http://tilecache.org/
.. _plugin: http://code.gustavonarea.net/repoze.what-pylons/Manual/index.html
