OpenLayers sandbox dev with git svn
###################################
:date: 2010-11-10 22:17
:author: Erilem
:category: Uncategorized

I've been using git-svn for OpenLayers development for some time now.
Although git-svn isn't so easy to work with, I'm quite happy with it for
OpenLayers.

So I have a git-svn clone of
``http://svn.openlayers.org/trunk/openlayers`` on my development
machine. I use this git repository for "trunk work", that is mainly for
bug fixes meant to go to trunk. When I start working on a bug fix, I
create a temporary branch, naming it with the id of the corresponding
trac ticket. When I have patch reviewed and accepted, I merge the
temporary branch into the master, dcommit, and remove the temporary
branch.

These days, I've been working on more experimental things (*Kinetic
Dragging*). Using OpenLayers SVN sandboxes is nice for developing new
features and experimenting, because they allow you to easily show and
share your work. So I needed a way to have my experimental box is a
sandbox while still managing my code with git-svn. And here's what I
did.

I started by creating a sandbox in the OpenLayers SVN repository::

    $ svn cp http://svn.openlayers.org/trunk/openlayers http://svn.openlayers.org/sandbox/elemoine/kinetic

Then, I added a new ``svn-remote`` in my OpenLayers Git repository's
``.git/config``::

    [svn-remote "svn-kinetic"]
    url = http://svn.openlayers.org/sandbox/elemoine/kinetic
    fetch = :refs/remotes/git-svn-kinetic

and fetched changes from that remote branch with::

    $ git svn fetch svn-kinetic -r 10884

``10884`` is the number of the SVN revision created when the sandbox directory
was built with ``svn cp``. This command created a remote branch named
git-svn-kinetic, and listed when entering ``git branch -r``::

    $ git branch -r
    git-svn
    git-svn-kinetic

Then I checked out the freshly-created remote branch, and created a
local branch from it::

    $ git checkout git-svn-kinetic
    $ git checkout -b kinetic

The local branch "kinetic" is bound to the remote branch "git-svn-kinetic", and
"git svn dcommit" commands done with the "kinetic" branch checked out go to
http://svn.openlayers.org/sandbox/elemoine/kinetic, which is exactly what
I want.
