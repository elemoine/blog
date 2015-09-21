A response to Iván's "Leaflet vs OpenLayers" talk
#################################################
:date: 2015-09-21 10:36
:author: Erilem
:tags: OpenLayers 3, Leaflet, FOSS4G

This blog post is a response to Iván Sánchez Ortega's "Leaflet vs OpenLayers 3"
`talk <https://github.com/IvanSanchez/leaflet-vs-openlayers-slides>`_, which he
gave at FOSS4G Seoul. I, as an OpenLayers developer, would like to defend
OpenLayers and provide some comments that I think are important making.

Newbie Friendliness
-------------------

To compare Leaflet and OpenLayers in terms of "Newbie Friendliness" Iván took
the simplest tutorial of each lib and tried to create a basic OSM map centered
on Seoul. The OpenLayers tutorial didn't make it clear that the longitude
should come before the latitude in the array defining the view center, so Iván
ended up with a newbie-unfriendly error message at map initialization time.

The OpenLayers documentation problem has been `fixed
<https://github.com/openlayers/ol3/pull/4132>`_ since then. But in general
I agree that Leaflet is more newbie-friendly than OpenLayers. For example, the
notion of Coordinate Reference System (CRS) is explicit in OpenLayers. This is
because we want OpenLayers to work with Web Mercator, as well as with other
projection systems.

I also think one cannot judge friendliness with just one example. For example, it would be interesting to compare
Leaflet and OpenLayers in terms of easiness of creating a map in a local
projection, the Korean 2000 (``EPSG:5179``) projection for example. 

Build sizes
-----------

Iván compares the size of minified builds (126 KB for Leaflet, versus 465 KB
for OpenLayers). He also compares the number of classes and namespaces (52 for
Leaflet, versus 163 for OpenLayers). Great! What does that mean? It means two
things. (a) OpenLayers includes more built-in features than Leaflet. (b)
OpenLayers users should create custom builds of OpenLayers, with just what
their application needs. This cannot be stressed enough.

Iván does mention custom builds in his talk. He also says that creating custom
builds requires using the Closure Compiler, and that this may « not fit with
your toolchain ». In fact, if you use Node/NPM in your Javascript project,
which is what a lot of Javascript developers use these days, installing
OpenLayers will also install
`closure-util <https://github.com/openlayers/closure-util/>`_, which will
download and install the Closure Compiler for you. So if you use Node, the only
thing you need for creating custom builds is Java (a Java Runtime Environment).

And, about OpenLayers, Iván also says that « most integration tools (Angular,
React, Polymer) or toolchains won't be able to slim it down without help ».
I have to say that I have a hard time understanding what he means here. Do
Angular and React include build tools that are compatible with Leaflet and not
with OpenLayers? Sorry, I don't get it.

Iván also compares the size of unminified files (223.6 KB for Leaflet, versus
3.5 MB for OpenLayers). He's right. This is a problem, somewhat related to the
use of the Closure Library. We are considering removing our dependency to the
Closure Library, so we hope to fix that problem in the future.

For the record, we, at Camptocamp, don't use ``ol-debug.js`` at all. Instead we
use an auto-loading mechanism where the OpenLayers scripts are individually
loaded based on the dependencies tree. But this is a bit advanced.

Coding Patterns
---------------

The OpenLayers code snippet provided by Iván could be replaced by this:

.. code-block:: javascript

    var map = new ol.Map({
      target: 'ol3map'
    });
    map.addLayer(new ol.layer.Tile({
      source: new ol.source.OSM()
    });
    map.setView(new ol.View({
      center: ol.proj.fromLonLat([127, 37]),
      zoom: 8
    });

So by using a more imperative style, you can get the same indentation level as
the Leaflet code snippet. So I find Iván's arguments rather weak.

It is true that OpenLayers provides more classes, uses the Simple Features Spec
(and GeoJSON) as the feature data model, and is generally more verbose than
Leaflet. But this may also make your code more explicit. There are more
important things in my opinion.

Documentation
-------------

Iván is correct to note that the 125 (and counting) examples OpenLayers
provides are an important aspect. This is what users should look at to learn
about how to use the library. The OpenLayers development team does a good job
at adding a new example for every new feature, and maintaining all these
examples.

It also true that OpenLayers' `API documentation
<http://openlayers.org/en/master/apidoc/>`_ is verbose and imperfect, but it is
comprehensive, always in sync with the code, and it includes relevant
information. The OpenLayers team is committed to making the API documentation
nicer and more convenient to users.

Map Rotation
------------

OpenLayers has supported map rotation from day 1. It is a core concept of
OpenLayers. Leaflet doesn't support it. So Iván created patch for this. Kudos
to him! To my knowledge no pull request has been created yet. And reading this
GitHub `comment
<https://github.com/Leaflet/Leaflet/issues/268#issuecomment-1928759>`_ from
Vladimir Agafonkin I am wondering if this functionality will ever be merged in
Leaflet. Unless Vladimir has changed his mind, which would be fine!

3D
--

It's correct that OpenLayers alone doesn't support rendering 3D objects. But
OpenLayers includes a WebGL renderer at its core, which already supports Image
layers, Tile layers and Vector layers, although only Point geometries are
supported at this point. So I think OpenLayers is in a good position to display
3D objects in the future, better than Leaflet. Iván's `Leaflet.gl
<https://github.com/IvanSanchez/Leaflet.gl>`_ is just a (very nice) hack at
this point, and I don't see it being merged in Leaflet any time soon. Maybe
another challenge Iván will accept :)
