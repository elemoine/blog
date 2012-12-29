Fanstatic
#########
:date: 2011-10-15 21:08
:author: Erilem
:category: Uncategorized

A Pyramid-based framework we work on at Camptocamp uses
`pyramid\_formalchemy`_ and its companion module, `fa.jquery`_. The
latter relies on `Fanstatic`_.

Fanstatic is basically a WSGI middleware that can inject script and link
tags in HTML pages, produced deeper in the WSGI stack. Any WSGI
application or middleware wrapped by a Fanstatic middleware can call
``need()`` on Fanstatic resources to instruct Fanstatic to inject script
or link tags for these resources. Fanstatic is simple, easy to use, and
well documented.

But I've been wondering what you can do with Fanstatic that you can't
with `Mako`_ or any other template engine. With Fanstatic you can insert
scripts and styles based on some request-dependent conditions. You can
also have a single place in the code where resources are inserted,
thereby avoiding duplications in the HTML files composing your web site.
But these are things you can also do with a template engine. One of the
goals of template engines is indeed to avoid duplicating (HTML) code, by
placing common code in template pieces, and having the template engine
put them together to form the actual HTML page.

I actually see one case where Fanstatic could be particularly useful:
one needs to extend/decorate pages that you don't create yourself,
because they're produced by a library you rely on. (fa.jquery is one of
these libraries.) With Fanstatic you can let the library create the
page, and have Fanstatic inject scripts and styles in the page for you.
But, if the lib doesn't use Fanstatic for inserting its own scripts and
styles you won't be able to control where Fanstatic will insert your
scripts and styles - Fanstatic will insert them either at the very top
or at the very bottom of the page, which can be a problem. Fanstatic
could provide options to give the application developer more control on
where resources are inserted, but it would never provide the needed
flexibility. If the lib you rely on uses Fanstatic you can create
Fanstatic resources that depend on the lib's resources, and thereby have
Fanstatic inject resources in the desired order.

As a conclusion I still have some doubts about the actual usefullness of
Fanstatic, but they're mitigated by the aforementioned "uncontrolled
pages" case. And I may discover other use cases as I go.

.. _pyramid\_formalchemy: http://docs.formalchemy.org/pyramid_formalchemy/
.. _fa.jquery: http://www.gawel.org/docs/fa.jquery/
.. _Fanstatic: http://www.fanstatic.org
.. _Mako: http://www.makotemplates.org/
