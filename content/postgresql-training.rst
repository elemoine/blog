PostgreSQL Training
###################
:date: 2018-06-05 20:40
:author: Erilem
:tags: PostgreSQL, Oslandia

I just attended a 3-day training on PostgreSQL Administration. The training was given by Thibaud
Walkowiak, from `Dalibo <https://www.dalibo.com>`_. I've been using PostgreSQL for years, mainly for
GIS-related stuff with PostGIS. And I wanted to know more about its internals and
administration. This training's been an excellent opportunity for that!

The training covered a lot of topics. My favorite were PostgreSQL's Journaling system, PITR
(Point-In-Time Recovery) system, and MVCC (Multi-Version Concurrency Control) implementation. I like
systems (in the broad sense), and these topics are very much system-oriented. Along the way, I've
also learned a few psql tricks, plus system extensions, views and functions that can be very useful
for diagnosing and troubleshooting problems.

In this blog post I am going to summarize on the things I learned about Journaling, PITR, and MVCC,
providing links to doc pages and articles I've found useful and interesting as I tried to gather
more information and understanding on these exciting topics.

Journaling
----------

PostgreSQL's Journaling system, a.k.a. WAL (Write-Ahead Logging), is what guarantees the integrity
of the data, the durability of operations, while enabling high peformance to database users.

This is how I'd summarize the functioning of Journaling in a few sentences: on a transaction commit
data changes are recorded into the journal, and the data itself is written into PostgreSQL's memory
(in the *shared buffers*) without actually being flushed to disk. The flushing of "dirty" buffers is
done at a later time by PostgreSQL system processes, namely the Background Writer and the
Checkpointer (explaining the differences between the two is beyond the scope of this post). Now, in
the event of a crash, the database can be recovered by replaying the operations recorded in the
journal.

What's really really cool that WAL is the basis for other cool features such as on-line backup,
point-in-time recovery and replication! The Postgres project is indeed really good at building
things in a gradual manner, with the low-level stuff being built first, and providing the foundation
for higher-level features.

With the hands-on exercises I discovered the ``pg_buffercache`` extension. This extension allows
getting information about all the blocks of the PostgreSQL instance's *shared buffers* memory. It
tells about what objects use the blocks, what blocks are dirty, etc. For example here's a query
that return the 5 objects that use the most memory::

	SELECT c.relname,
		   c.relkind,
		   count(*) AS buffers,
		   pg_size_pretty(count(*)*8192) as mem_size
	FROM   pg_buffercache b
	INNER JOIN pg_class c
		  ON b.relfilenode = pg_relation_filenode(c.oid)
			AND b.reldatabase IN (0, (SELECT oid FROM pg_database
									  WHERE datname = current_database()))
	GROUP BY c.relname, c.relkind
	ORDER BY 3 DESC
	LIMIT 5 ;

To go further:

* `Official PostgreSQL WAL documentation <https://www.postgresql.org/docs/current/static/wal.html>`_

Point-In-Time Recovery
----------------------

PITR is a way to back up PostgreSQL databases. As opposed to traditional backup strategies based on
``pg_dump`` or similar the backup process is done continuously, greatly narrowing the data loss
window. PITR also operates without shutting down the PostgreSQL instance, and with close to zero
impact on the database users.

PITR is based on the journaling system. The journals are archived in a safe location, and in the
event of a bad operation or a data loss on the PostgreSQL system the data can be recovered by
replaying the journal operations on top of a previous image of the data files. The recovery
can be done up to a certain point in time, hence the name PITR.

PITR involves two operations: the archiving of WAL files, and the copying of the data files for the
creation of "images" onto which journal operations can be replayed. For the archiving of WAL files
one can rely on the ``archive_command`` (push model) or on the ``pg_receivewal`` command (pull
model). For the copying of the data files there's also two options. One can rely on the
``pg_start_backup`` and ``pg_stop_backup`` functions, and use her own tool for the actual
copying of the data files. Or the ``pg_basebackup`` tool can be used.

I see PITR as very good way to achieve backups, when minimizing the data loss window is a key
element. Using PITR is certainly more involved than just using ``pg_dump`` and ``pg_restore``, but
setting it up is not that complex really. Plus there are good tools such *Barman*, *pitrery*, and
*pgBackRest* that simplify and streamline the PITR process. I'd definitely consider those tools
next time I need to set up PostgreSQL database backups.

To go further:

* `Official PostgreSQL PITR documentation <https://www.postgresql.org/docs/current/static/continuous-archiving.html>`_
* `Barman <https://www.pgbarman.org/documentation/>`_
* `pitrery <https://dalibo.github.io/pitrery/>`_
* `pgBackRest <https://pgbackrest.org/>`_

MVCC
----

MVCC means « Multi-Version Concurrency Control ». It is the model used by PostgreSQL for
handling data changes and transactions.

Basically, in a PostgreSQL table, a record can be stored in multiple versions. A change to an
existing record leads to the creation of a new version of that record. Similarly the deletion of
a record leads to the creation of a new version of the record. With this mechanism transactions can
see different versions of records, which is precisely what transactions are about.

Related to MVCC and the transaction isolation levels are the ``xmin`` and ``xmax`` system columns.
For example, let's assume you have a table named ``t`` with columns ``c1`` and ``c2``. In addition
to ``c1`` and ``c2`` you can select the ``xmin`` and ``xmax`` columns. For example::

    # select xmin, xmax, * from t;
     xmin | xmax | c1 | c2 
    ------+------+----+---
     1105 |    0 | 1  |  1
     1105 |    0 | 2  |  2
     1105 |    0 | 3  |  3
    (3 rows)

``xmin`` is the id of the transaction that created the record. ``xmax`` is the id of the transaction
that deleted the record. For example if a transaction is being deleting a record you will see this
in another transaction::

    # select xmin, xmax, * from t;
     xmin | xmax | c1 | c2 
    ------+------+----+----
     1105 | 1106 |  1 |  1
     1105 |    0 |  2 |  2
     1105 |    0 |  3 |  3
    (3 rows)

Here are two rules that always apply:

* Records with ``xmin`` smaller than the id of the current transaction are visible to the
  current transaction if the ``xmin`` transaction was committed.
* Records with ``xmax`` smaller that the id of the current transaction are not visible to
  the current transaction if the ``xmax`` transaction was committed. 

The other cases depend on the isolation level used in the transactions.

Another thing closely related to MVCC is ``VACUUM``. MVCC and the creation of new record versions
imply that mechanisms exist to clean up "dead" records. A record is dead if it has a ``xmax`` that
corresponds to a transaction that was committed or rolled back, and that there's no ongoing
transaction using that record. In old versions of PostgreSQL the administrator was responsible
for setting up periodic VACUUM jobs. The PostgreSQL versions that everyone uses nowadays include
an ``autovacuum`` process that takes care of these periodic VACUUM operations.

To go further:

* `Official PostgreSQL Transaction Isolation documentation <https://www.postgresql.org/docs/current/static/transaction-iso.html>`_
* `Official PostgreSQL System Columns documentation <https://www.postgresql.org/docs/current/static/ddl-system-columns.html>`_
* `How VACUUM works <http://rhaas.blogspot.com/2017/12/mvcc-and-vacuum.html>`_
* `The State of VACUUM <http://rhaas.blogspot.com/2018/01/the-state-of-vacuum.html>`_
* `A Practical Guide to SQL Transaction Isolation <https://begriffs.com/posts/2017-08-01-practical-guide-sql-isolation.html>`_

Some conclusion
---------------

The notes in this blog post just touches the surface of the topics discussed. They also certainly
take shortcuts. What I love about PostgreSQL is its transparency. In particular the excellent
documentation is very transparent on the way PostgreSQL works internally. For example the
`Pointcloud extension <https://github.com/pgpointcloud/pointcloud>`_ I work defines types that
support the ``TOAST`` interface, and I've found `the TOAST doc
<https://www.postgresql.org/docs/current/static/storage-toast.html>`_ very clear and informative!

Keep up the good work PostgreSQL! We love you!
