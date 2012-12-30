FeatureServer Versus MapFish Server
###################################
:date: 2008-10-31 15:10
:author: Erilem

I thought I could say a few words on the differences between
`FeatureServer`_ and MapFish Server.

First, FeatureServer and MapFish Server have similarities. They share a
similar, REST-based protocol, for creating, reading, updating and
deleting features.

The main difference between the two: FeatureServer is a standalone
application, MapFish Server is a web-mapping development framework.

FeatureServer is perfect for very rapidly setting up editable layers,
with no custom needs. MapFish Server is good if you work on a customer
project, with specific, customer-oriented needs; MapFish

Server provides a complete development framework, which, thanks to the
great components it relies on (`Pylons`_, `SQLAlchemy`_, `Shapely`_,
etc.) allows to write high-quality and maintainable code.

Two different goals.

.. _FeatureServer: http://featureserver.org/
.. _Pylons: http://pylonshq.com
.. _SQLAlchemy: http://www.sqlalchemy.org
.. _Shapely: http://pypi.python.org/pypi/Shapely
