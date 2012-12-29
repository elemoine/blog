MapFish 1.0
###########
:date: 2008-10-17 07:58
:author: Erilem
:category: Uncategorized

MapFish 1.0 is out!

The things I really like in MapFish 1.0:

-  The PDF Printing Library. Everyone wants to print maps, `Patrick`_
   has turned everyone's dream into reality. The PDF Printing Library is
   great, it supports fancy stuff like vector rendering, map rotation,
   legend, etc. See this `page`_ to know more. And there's more to come,
   `support`_ for printing map annotations is about to make it into
   trunk.
-  MapFish Server implementation of the `MapFish Protocol`_ for
   creating, reading, updating and deleting features. We still need to
   add a feature editing widget to MapFish Client, the feature editing
   panel, currently demo'ed `here`_, will probably make it into trunk
   soon.
-  MapFish Client relying on the OpenLayers protocol abstraction. With
   that every MapFish Searcher component can work with the MapFish
   Protocol as well as with any other protocols supported by OpenLayers
   (e.g. Gears, WFS).
-  The feature reader, and mediator components we have added to
   `widgets/data`_. These are core classes to bridge OpenLayers and Ext.
   And by the way, these classes will probably represent the first bits
   put in GeoExt; more on that later...
-  The `API doc`_ that covers both MapFish Client and OpenLayers.

.. raw:: html

   </p>

There are other stuff in MapFish 1.0, the above are just the ones I care
the most about.

.. _Patrick: http://patrick.blog.thus.ch/
.. _page: https://trac.mapfish.org/trac/mapfish/wiki/PrintModuleDoc
.. _support: https://trac.mapfish.org/trac/mapfish/ticket/197
.. _MapFish
Protocol: https://trac.mapfish.org/trac/mapfish/wiki/MapFishProtocol
.. _here: http://dev.mapfish.org/sandbox/camptocamp/MapFishUnhcr/client/examples/editing/editing-panel.html
.. _widgets/data: https://trac.mapfish.org/trac/mapfish/browser/trunk/MapFish/client/mfbase/mapfish/widgets/data
.. _API doc: http://www.mapfish.org/apidoc/1.0
