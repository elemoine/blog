Hacking
#######
:author: Éric Lemoine

Some of the open-source stuff I've worked on.

Sungem
------

For my Phd I developed a thread-based networking subsystem for Linux. I also
developed drivers and firmware for Myricom/Myrinet network devices. After my
Phd, I worked on the Sungem network interface driver (Sungem was the network
interface of the iBook G3 I was using at that time). I added `NAPI
<http://en.wikipedia.org/wiki/New_API>`_ and NETPOLL support to the driver.
I must confess that I'm happy to see that the `sungem driver
<https://github.com/torvalds/linux/blob/master/drivers/net/ethernet/sun/sungem.c>`_
is still in Linux, and that I still have my name listed in the file!

OpenLayers
----------

`OpenLayers <http://www.openlayers.org>`_ is a JavaScript library for adding
*slippy* maps to web pages. This is an open-source alternative to the Google
Maps API. I'm a core developer of OpenLayers. I've contributed many bug fixes,
and enhancements, and introduced a number of new features. In particular,
I actively worked on `Vector Behavior
<http://openlayers.org/blog/2008/04/15/vector-behavior/>`_, which, I think, is
one of the coolest pieces of OpenLayers.

I'm currently working on OpenLayers 3, One of the goals of OpenLayers 3 is
exploring using WebGL for creating *3D maps*. My `"Why are we building
OpenLayers 3" blog post
<http://openlayers.org/blog/2012/11/14/why-are-we-building-openlayers-3/>`_ 
provides more information on OpenLayers 3.

GeoExt
------

`GeoExt <http://www.geoext.org>`_ is a JavaScript library that brings
OpenLayers and `ExtJS <http://www.sencha.com/products/js/>`_ together. Its goal
is to help build desktop-style GIS applications for the web with JavaScript.
I participated in the creation of the project in 2008, and I've been a core
developer of the library since then. I've contributed lots of features,
enhancements and bug fixes. I, for example, created ``GeoExt.Action``, for
coupling OpenLayers controls and Ext buttons or menu items, and had a lot of
fun with it.

GeoAlchemy
----------

`GeoAlchemy <http://www.geoalchemy.org>`_ extends `SQLAlchemy
<http://www.sqlalchemy.org>`_ with geospatial features.  GeoAlchemy is
wonderful! And one of the reasons it's wonderful is because SQLAlchemy is
wonderful. I mentored the talented `Tobias Sauerwein
<http://twitter.com/tsauerwein>`_ in his work on GeoAlchemy, and contributed
a number of enhancements and fixes.

I've recently started working on `GeoAlchemy
2 <https://groups.google.com/forum/#!topic/geoalchemy/-xHBYZCUaDk>`_.
GeoAlchemy 2 aims to provide a simpler implementation and improved APIs.

MapFish
-------

`MapFish <http://www.mapfish.org>`_ extends the `Pylons <http://pylonshq.com>`_
web framework with geospatial functionality. In addition to Pylons, MapFish is
based on GeoAlchemy, and the Shapely, and geojson packages from `Sean Gillies'
<http://sgillies.net>`_ `GIS-Python Lab <http://trac.gispython.org/lab>`_. I'm
one of the creators and main developers of MapFish.  Working on MapFish has
made me discover the Pylons framework, and its ecosystem. I even had the
chance to contribute a `patch
<http://pylonshq.com/project/pylonshq/ticket/632>`_ to Pylons.


gTranslate
----------

`gTranslate <https://addons.mozilla.org/en-US/firefox/addon/918/>`_ is
a FireFox add-on for translating text in web pages with the Google translation
services.  I discovered gTranslate while learning about the development of
FireFox add-ons. I refactored the code, set up the test harness, and wrote unit
tests.
