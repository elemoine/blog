Notes on Docker Volumes
#######################
:date: 2016-01-27 20:40
:author: Erilem
:tags: Docker

Docker is popular because it's approachable and well documented.  These are not
the only reasons for its popularity, but I think they are key bits.  For
example, what do you want to use? `this
<http://libvirt.org/sources/virshcmdref/html/sect-create.html>`_ or `that
<https://docs.docker.com/engine/reference/run/>`_?  libvirt and Docker are not
comparable technologies, but I think you get the point.

So Docker is easy!?  It's accessible, sexy and using it is immediately
enjoyable.  But I don't think it's easy, especially when it comes to doing real
stuff with it.

I've had to use Docker Volumes lately.  Again, the Docker documentation does
a great job at `documenting
<https://docs.docker.com/v1.8/userguide/dockervolumes/>`_ volumes!  But, as
always, there are interesting subtleties, and important differences between the
different ways to use volumes.  And determining what type of volumes to use may
be far from easy!

Let's use this simple ``Dockerfile``::

    FROM debian:latest

    RUN useradd user \
        && mkdir /foo \
        && touch /foo/bar \
        && chown -R user:user /foo

    CMD ls -lh /foo && ls -ldh /foo

    USER user

This ``Dockerfile`` defines an image whose base is the latest Debian image.  It
adds a user ``user``, a directory ``/foo``, a file ``bar`` in the ``/foo``
directory and change the owner and group of the ``/foo`` directory and its
content to ``user``.  When the image is run the content of the ``/foo``
directory is displayed, together with information (permissions, owner, group)
about that content and the directory itself.

So let's build the image::

    $ docker build -t foo .

and run it::

    $ docker run --name foo -it foo
    total 0
    -rw-r--r-- 1 user user 0 Jan 27 20:34 bar
    drwxr-xr-x 2 user user 4.0K Jan 27 20:34 /foo

The output of ``docker run`` is as expected.  The ``/foo`` directory contains
the ``bar`` file, and the owner/group of ``/foo`` and ``/foo/bar`` is
``user``/``user``.

Our container executed the two ``ls`` commands and exited.  But it's still
there.  Run ``docker ps -a`` to confirm that.

So let's remove it before going further::

    $ docker rm foo
    foo

Now let's run the image again, but using a volume ``/foo`` this time::

    $ docker run --name foo -it -v /foo foo
    total 0
    -rw-r--r-- 1 user user 0 Jan 27 20:34 bar
    drwxr-xr-x 2 user user 4.0K Jan 27 20:51 /foo

The output is the same as previously, except that the creation time of the
``/foo`` directory has changed.  Here ``docker run`` created a new directory
for the volume, and copied the content of the image's ``/foo`` directory into
that volume directory.

Let's use ``docker volume ls`` to list all the existing volumes::

   $ docker volume ls
   DRIVER              VOLUME NAME
   local               50de22407faecc7b0ae8cd3329e1c21a97b5f75876242e31d166bc95d24c3f1b

Here there is only one existing one, which is the one we just created with the
previous ``docker run`` command.

To know where the volume directory is the ``docker volume inspect`` command can
be used::


    $ docker volume inspect -f "{{.Mountpoint}}" 50de22407faecc7b0ae8cd3329e1c21a97b5f75876242e31d166bc95d24c3f1b
    /var/lib/docker/volumes/50de22407faecc7b0ae8cd3329e1c21a97b5f75876242e31d166bc95d24c3f1b/_data

On my system (Ubuntu) ``/var/lib/docker/volumes`` is the directory where Docker
creates the directory mount points.

If we remove the container the volume will persist.  To remove volumes the
``docker volume rm`` command is to be used::

    $ docker rm foo  # remove the container first
    $ docker volume rm 50de22407faecc7b0ae8cd3329e1c21a97b5f75876242e31d166bc95d24c3f1b

Ok, so far so good, and I guess we haven't encountered anything unexpected.

This time, we're going to mount a host directory as a volume (a.k.a. **bind-mount**)::

    $ docker run --name foo -it -v /tmp/foo:/foo foo
    total 0
    drwxr-xr-x 2 root root 4.0K Jan 27 21:19 /foo

Now the output of the ``docker run`` command is completely different.  From the
container's perspective the ``/foo`` directory is empty, and its owner/group is
``root``/``root``.

Here ``docker run`` bind-mounts the host directory ``/tmp/foo`` into the
container, as ``/foo`` in the container.  In our case, the directory ``/foo``
exists in the image.  The bind-mount of ``/tmp/foo`` into ``/foo`` hides it
completely, which explains the different output that we obtained this time.

Note that when using a bind-mount there's volume/mount point created by Docker.
Run ``docker volume ls`` if you need to be convinced::

    $ docker volume ls

Now we're going to create a **named volume**::

    $ docker run --name foo -it -v foo:/foo foo
    total 0
    drwxr-xr-x 2 root root 4.0K Jan 27 21:35 /foo

Named volumes are very similar to normal/standard volumes except that they're
a bit different.  Note that, as when we used a bind-mount, the named volume
``foo`` has hidden the image's ``/foo`` directory.  This is why ``docker run``
reports that the ``/foo`` directory is empty and that its owner/group is
``root``/``root``.  Named volumes are between standard volumes and bind-mounts.

For the last example of this blog post let's create a slightly different
``Dockerfile``::

    FROM debian:latest

    RUN useradd user \
        && mkdir /foo \
        && touch /foo/bar \
        && chown -R user:user /foo

    VOLUME /foo

    CMD ls -lh /foo && ls -ldh /foo

    USER user

Note the ``VOLUME /foo`` line.  In this case ``docker run`` will create
a volume even if no volume is specified on the command line::

    $ docker run --name foo -it foo
    total 0
    -rw-r--r-- 1 user user 0 Jan 27 20:34 bar
    drwxr-xr-x 2 user user 4.0K Jan 27 21:58 /foo

    $ docker volume ls
    DRIVER              VOLUME NAME
    local               7f6cd56e1795ef443d03b32e01ccc672b022ce85a2ff2818072065f10554351c

Thanks for reading!
