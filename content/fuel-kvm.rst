Deploy Fuel and OpenStack on KVM virtual machines
#################################################
:date: 2015-11-22 20:20
:author: Erilem
:tags: OpenStack, Fuel, KVM, Mirantis

This post provides the steps to deploy Fuel and OpenStack on KVM virtual
machines.

It is based on the `Fuel devops page
<https://docs.fuel-infra.org/fuel-dev/devops.html>`_ from the official Fuel
documentation, but uses shortcuts, and relies on ``virtualenv`` as much as
posssible (more than the official documentation does).

This post is by no means a replacement for the official documentation. I wrote
it mainly for me, from notes I took when I set up my development environment
the very first time. I'll update this post as I discover things about
``fuel-devops``.

Ubuntu 14.04 (Trusty) is assumed.

Install system packages
-----------------------

Run the following command to install the required system packages::

    $ sudo apt-get install git postgresql postgresql-server-dev-all \
        libyaml-dev libffi-dev python-dev qemu-kvm libvirt-bin \
        libvirt-dev ubuntu-vm-builder bridge-utils \
        libpq-dev libgmp-dev

You will also need to install ``python-pip`` and ``python-virtuaenv`` if you
don't have ``pip`` and ``virtualenv`` installed::

    $ sudo apt-get install python-pip python-virtualenv

Note: I personally install ``pip``, ``virtualenv`` and ``virtualenvwrapper`` to
the user site, i.e. in ``~/.local``. See my `dotfiles' Makefile
<https://github.com/elemoine/dotfiles/blob/master/Makefile>`_ if you want to
know how.

Create virtual environment and install ``fuel-devops``
------------------------------------------------------

Create a virtual environment::

    $ cd /some/path
    $ virtualenv fuel-devops-venv

Now install ``fuel-devops`` in the virtual environment just created::

    $ ./fuel-devops-venv/bin/pip install git+https://github.com/openstack/fuel-devops.git@2.9.12

Configure ``libvirt`` pool
--------------------------

Create a ``libvirt`` persistent pool and start it::

    $ sudo virsh pool-define-as --type=dir --name=default --target=/var/lib/libvirt/images
    $ sudo virsh pool-autostart default sudo
    $ virsh pool-start default

``/var/lib/libvirt/images`` is where QEMU QCOW images will be stored, so make
sure this directory is attached to a file system with sufficient storage.

Make your user a member of the ``libvirtd`` group::

   $ sudo usermod $(whoami) -a -G libvirtd

Configure the PostgreSQL database
---------------------------------

Create a database and database user::

    $ sudo sed -ir 's/peer/trust/' /etc/postgresql/9.*/main/pg_hba.conf
    $ sudo service postgresql restart
    $ sudo -u postgres createuser -P fuel_devops # see default <user> and <db> below
    $ sudo -u postgres createdb fuel_devops -O fuel_devops
    $ django-admin.py syncdb --settings=devops.settings
    $ django-admin.py migrate devops --settings=devops.settings

Check that nested KVM is enabled
--------------------------------

Check the following::

    $ cat /etc/modprobe.d/qemu-system-x86.conf
    options kvm_intel nested=1

And::

    $ cat /sys/module/kvm_intel/parameters/nested
    Y

Create environment using ``fuel-qa``
------------------------------------

Clone the ``fuel-qa`` repository::

    $ git clone https://github.com/openstack/fuel-qa
    $ cd fuel-qa

Install requirements in the virtual environment::

    $ source /some/path/fuel-devops-venv/bin/activate
    $ pip install -r ./fuelweb_test/requirements.txt

Download a Fuel ISO image
-------------------------

You now need to download a Fuel ISO image from the `Fuel CI website
<https://ci.fuel-infra.org/view/ISO/>`_. I personally use
``MirantisOpenStack-7.0.iso``.

Create Fuel node
----------------

And run this command to create the Fuel node (a.k.a. Fuel master)::

    $ export NODES_COUNT=5
    $ ./utils/jenkins/system_tests.sh -t test -w $(pwd) -j fuel_test -k -K \
        -i <path_to_iso> -V <path_to_venv> -e <environment_name> -o \
        --group=prepare_release

``<environment_name>`` is the name of your test environment, any name of your
choice really. But make sure you use the same environment when running
``system_tests.sh`` again to add nodes to the OpenStack cluster.

The ``-t`` and ``-j`` flags are used to set the task name and job name,
respectively. Really, these flag make sense when ``system_tests.sh`` is run
from Jenkins, which is how the devops team uses the script. In our case any
value can be used for these flags, and the same values can be used for multiple
environments.

Create Fuel slaves
------------------

Use the following command to create four Fuel slaves (nodes that you will
install OpenStack on)::

    $ ./utils/jenkins/system_tests.sh -t test -w $(pwd) -j fuel_test -k -K \
        -i <path_to_iso> -V <path_to_venv> -e <environment_name> -o \
        --group=prepare_slaves_5

Connect to Fuel interface
-------------------------

You should now have five nodes: a Fuel master node and four Fuel slave
nodes. You can now open the Fuel UI at http://10.109.0.2 (admin/admin),
create an environment and deploy OpenStack on the Fuel slave nodes.
