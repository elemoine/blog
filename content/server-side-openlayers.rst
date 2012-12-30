Server-side OpenLayers
######################
:date: 2010-03-14 10:28
:author: Erilem
:tags: javascript, node, openlayers

I've been interested in server-side JavaScript lately. As a proof of
feasibility (to myself) I've put together a node.js-based web service
that gets geographic objects from PostGIS and provides a GeoJSON
representation of these objects.

For this I've used node.js, postgres-js and OpenLayers.

`node.js`_ is a lib whose goal is "to provide an easy way to build
scalable network applications". node.js relies on an event-driven
architecture (through epoll, kqueue, /dev/poll, or select). I'd
recommend looking at the `jsconf slides`_ to know more about the
philosophy and design of node.js.

The "Hello World" node.js web service looks like that:

.. code-block:: javascript

    var sys = require('sys'),
        http = require('http');

    http.createServer(function (req, res) {
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.write('Hello World');
        res.close();
    }).listen(8000);

    sys.puts('Server running at http://127.0.0.1:8000/');

Thanks to node.js's nice interface I think the code is pretty much
self-explained.

Assuming the above code is included in a file named *file.js*, starting
the web service is done with::

    $ node file.js

Now we can use `postgres-js`_ to read data from a PostGIS table.
postgres-js sends SQL queries to PostgreSQL through TCP. postgres-js is
a node.js module, so it can be loaded with ``require()`` (just like the
built-in *sys* and *http* modules).

.. code-block:: javascript

    var sys = require('sys'),
        http = require('http'),
        Postgres = require('postgres');
    
    var db = new Postgres.Connection("dbname", "username", "password");

    http.createServer(function (req, res) {
        db.query("SELECT name, astext(geom) AS geom FROM table", function (objs) {
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write("it works");
            res.close();
        });
    }).listen(8000);

    sys.puts('Server running at http://127.0.0.1:8000/');

The last step involves using `OpenLayers`_ for deserializing from WKT
and serializing to GeoJSON. To use OpenLayers in the node.js
application, and load it with the ``require()`` function, I packaged
OpenLayers as a node.js module. It was easy enough, see the `modules
doc`_.

And here's the final code:

.. code-block:: javascript

    var sys = require('sys'),
        http = require('http'),
        Postgres = require('postgres'),
        OpenLayers = require('openlayers').OpenLayers;

    var db = new Postgres.Connection("dbname", "username", "password");

    http.createServer(function (req, res) {
        db.query("SELECT name, astext(geom) AS geom FROM table", function (objs) {
            var features = [];
            var wkt = new OpenLayers.Format.WKT();
            for(var i=0,len=objs.length; i<len; i++) {
                features.push(
                    new OpenLayers.Feature.Vector(
                        wkt.read(obj[i].geom).geometry, {name: obj[i].name}
                    )
                );
            }
            var geojson = new OpenLayers.Format.GeoJSON();
            var output = geojson.write(features);
            res.writeHead(200, {'Content-Type': 'application/json'});
            res.write(output);
            res.close();
        });
    }).listen(8000);
    
    sys.puts('Server running at http://127.0.0.1:8000/');

The End. Happy server-side JavaScript to all.

.. _node.js: http://nodejs.org
.. _jsconf slides: http://s3.amazonaws.com/four.livejournal/20091117/jsconf.pdf
.. _postgres-js: http://github.com/creationix/postgres-js
.. _OpenLayers: http://www.openlayers.org
.. _modules doc: http://nodejs.org/api.html#_modules
