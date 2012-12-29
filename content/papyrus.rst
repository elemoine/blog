Papyrus
#######
:date: 2011-07-09 07:25
:author: Erilem
:category: Uncategorized
:tags: papyrus, pyramid

A few days ago I pushed `papyrus\_mapproxy`_ on Github. The objective of
papyrus\_mapproxy is to make it easy to embed `MapProxy`_ in `Pyramid`_
apps.

This new module is a good opportunity for me to describe what I've been
up to with Papyrus.

I have developed five Papyrus modules: papyrus, papyrus\_tilecache,
papyrus\_mapproxy, papyrus\_ogcproxy, and papyrus\_mapnik. The last four
are companion modules for the first one.

I wrote these modules to learn Pyramid, and assess its extensibility,
with the goal to eventually provide extensions that will ease the work
of Pyramid developers working on mapping apps.

The main module, `papyrus`_, provides conveniences for creating feature
web services. For example, it provides a GeoJSON renderer, and a full
implementation of the `MapFish Protocol`_.

The`papyrus\_tilecache`_ and `pyramid\_mapproxy`_ modules make it easy
to embed `TileCache`_ and MapProxy in Pyramid apps, respectively.

The `papyrus\_mapnik`_ module aims to ease using `Mapnik`_ in Pyramid
apps. This module is experimental, and would need some work to be
actually useful.

The `papyrus\_ogcproxy`_ provides a proxy service for OGC protocols. It
was developed for working around the Same Origin Policy implemented in
browsers.

I believe there's high value in embedding services, like tile rendering
and caching services, in the web application. That can greatly ease
deployment. It also allows leveraging transverse layers of the
application, like the security layer.

Building a consistent, well integrated, and scalable application that
requires external independent services is, to say the least, a big
challenge I think. Assembling different types of services within a
single application, relying on horizontal scaling, is much more
appealing to me.

Anyway, any feedback on Papyrus is welcome!

.. _papyrus\_mapproxy: https://github.com/elemoine/papyrus_mapproxy
.. _MapProxy: http://mapproxy.org/
.. _Pyramid: http://docs.pylonsproject.org/docs/pyramid.html
.. _papyrus: https://github.com/elemoine/papyrus
.. _MapFish
Protocol: http://trac.mapfish.org/trac/mapfish/wiki/MapFishProtocol
.. _papyrus\_tilecache: https://github.com/elemoine/papyrus_tilecache
.. _pyramid\_mapproxy: https://github.com/elemoine/papyrus_mapproxy
.. _TileCache: http://tilecache.org/
.. _papyrus\_mapnik: https://github.com/elemoine/papyrus_mapnik
.. _Mapnik: http://mapnik.org/
.. _papyrus\_ogcproxy: https://github.com/elemoine/papyrus_ogcproxy
