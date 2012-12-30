Testing
#######
:date: 2009-06-30 11:37
:author: Erilem
:tags: geoext, mapfish, openlayers, programming, testing

I've been reading about testing. Here are a few words on my thoughts
about testing.

From my reading and understanding there are three types of tests:

-  Unit tests: a unit test tests a single function (e.g. an object
   method). A unit test must take care of isolating the tested function
   from the functions the tested function normally relies on (when
   executed outside any test).
-  Integration tests: an integration test tests if two or more dependent
   functions correctly work together.
-  User-acceptance tests: a user-acceptance tests whether a given
   function provides the behavior its users expect. User Interface tests
   belong to this type.

.. raw:: html

   </p>

These three types of tests are complementary, they all have their
importance when testing an application.

In OpenLayers, GeoExt, and MapFish (its JavaScript library), we provide
unit and integration tests, and actually don't distinguish whether
they're of the unit or integration type (they're all referred to as unit
tests, which is fine I think). Not providing user-acceptance tests makes
sense, as OpenLayers, GeoExt and MapFish are libraries as opposed to
applications. The three libraries come with examples that in some way
are user-acceptance tests. (In OpenLayers we've attempted to create
actual user-acceptance tests, but developpers haven't paid much
attention to them, possibly their scopes and goals haven't been well
defined.)

Applications built with OpenLayers and/or GeoExt and/or MapFish
instantiate classes from these libraries. Often, most of their code
doesn't include actual logic, and from that regard writing unit and
integration tests for such applications doesn't make sense. However, as
User Interfaces, these applications would deserve user-acceptance tests.

Providing automated User Interface tests is in my opinion a very
difficult task, and I'd be very interested in having feedback from
others on that.
