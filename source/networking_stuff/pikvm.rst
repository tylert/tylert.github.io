PiKVM Stuff
-----------

* https://pikvm.org/
* https://github.com/pikvm/pikvm

Web default login is:  "admin" with password "admin"
SSH default login is:  "root" with password "root"

Look under "pages" in the GitHub repo for additional documentation.

::

    # How to upgrade a pikvm:  Use the local terminal and use su or ssh in,
    # then do...
    rw
    pacman -Syu --noconfirm
    pacman -Sc
    rm -rf /var/cache/pacman/pkg
    reboot
