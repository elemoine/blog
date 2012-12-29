MapFish and GeoExt
##################
:date: 2009-04-19 20:40
:author: Erilem
:category: Uncategorized

Matt Priour recently `asked`_ about the future of the client part of
MapFish, and more specifically whether it will be replaced by `GeoExt`_.
This is actually a question that every MapFish user should be asking
:-). Anyway I thought an answer to that question could make a post on my
blog. There it is.

**The short story:** the client part of MapFish will not be replaced by
GeoExt.

**Now the longer story**. As of today the client part of MapFish
includes OpenLayers, Ext, and the MapFish JavaScript lib. The latter is
itself composed of two parts: *core* and *widgets*.

-  *core* includes classes that are independent of Ext; most of them
   extend OpenLayers classes like ``OpenLayers.Control``,
   ``OpenLayers.Protocol``, ``OpenLayers.Strategy``, etc. For example
   the client-side implementation of the `MapFish Protocol`_ is part of
   *core*.
-  *widgets* includes Ext-based classes, mostly GUI components (but not
   only, the FeatureReader and stuff are part of *widgets*). *widgets*
   also has stuff that's directly related to the server side of MapFish,
   the print widgets are a good example.

.. raw:: html

   </p>

GeoExt will not replace *core*, nor will it replace the *widgets*
components that rely on MapFish web services. But basically every new
Ext-based component that isn't tied to any server-side stuff is going
into GeoExt.

In addition to OpenLayers and Ext, MapFish will include GeoExt. We had
initially planned to integrate GeoExt into MapFish earlier, but finally
decided to let things settle down a bit in GeoExt before doing the
integration. We're currently doing that integration, and we will
gradually be deprecating classes as their equivalents are added into
GeoExt. For example, the work on FeatureRecord, FeatureReader and
FeatureStore we've been doing in GeoExt will deprecate the
FeatureReader, FeatureStore and LayerStoreMediator classes in the
MapFish JavaScript lib.

Also, MapFish, as a framework, aims to provide an integrated solution.
For client-side development, this means that the developer doesn't need
to download Ext, OpenLayers and GeoExt, install them within his
application, and think about the organization of his application.
Instead, we want that applications created with the MapFish framework
are well organized from their creations; with the Ext, OpenLayers,
GeoExt and MapFish libs ready, with the JavaScript build tool ready,
with the unit test suite ready, etc. I guess I will cover this topic in
a later post...

Wooo, two posts in two days, scarry... :-)

.. _asked: http://www.geoext.org/pipermail/users/2009-April/000045.html
.. _GeoExt: http://www.geoext.org
.. _MapFish
Protocol: http://www.mapfish.org/trac/mapfish/wiki/MapFishProtocol
