Some valid reasons to prefer Ubuntu over CentOS:

1.  Despite joining forces with RedHat, CentOS is still, essentially, a
community effort supported with limited resources.  There is no way to pay for
commercial support of this product without moving to another distribution like
RedHat Enterprise.  Ubuntu is backed by Canonical Ltd. and, in addition to the
free community support, they also offer paid professional support should the
need ever arise.

2.  Many of the packages that are considered part of the core system for Ubuntu
are either missing on CentOS or are much, much older (CentOS 6.x is already 4
years old).  As a result, when using CentOS, we are forced to import unofficial
3rd-party repositories such as the "remi" repo and still other
community-maintained repositories such as "epel" to satisfy our requirements
for newer versions of php, ruby, MySQL, etc.

3.  CentOS's rpm/yum package management ecosystem is much more prone to errors
and deadlocks and is slower than Ubuntu's dpkg/apt package management system.
Should the need ever arise later, the barriers to creating our own in-house
custom Ubuntu packages are also much, much lower than making our own custom
CentOS packages.  It is also significantly easier to non-destructively test and
use custom package installation and custom package repositories in Ubuntu (but
would require a more in-depth discussion;  I have worked with both systems in
the past as part of my day job).

4.  CentOS derives most of it's packages from RedHat, their upstream provider.
Each release, CentOS will rebuild a fair percentage of the RedHat binary
packages from the official RedHat source packages with some modifications.
RedHat typically has already applied their own customizations to these source
packages after they came from the open-source community but deliberately
attempt to obscure the exact changes that they made to them.  In many cases
these source packages then receive further modifications by CentOS before they
are built.  With Ubuntu, their upstream provider is Debian and there are no
private, unpublished patches to be concerned about--the source code is likely
to be pretty much the same as it was when it was written and tested by the
original author.

5.  Unlike Ubuntu, CentOS has no ARM architecture support.  Today, this is not
a big issue, however, as we plan for other future opportunities such as using
an on-premesis server to cache transactions for a cloud application, we might
wish to keep our options open for using commodity, low-power ARM equipment.
