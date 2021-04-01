PiKVM Stuff
-----------

* https://pikvm.org/
* https://github.com/pikvm/pikvm

Web default login is:  "admin" with password "admin"
SSH default login is:  "root" with password "root"

Look under "pages" in the GitHub repo for additional documentation.

::

    # Upgrade the pikvm root filesystem to latest
    # Use the local terminal and use su or ssh in, then do...
    rw
    pacman -Syu --noconfirm
    pacman -Sc --noconfirm
    rm -rf /var/cache/pacman/pkg
    reboot

    # Change the default web and ssh passwords
    # Use the local terminal and use su or ssh in, then do...
    rw
    kvmd-htpasswd set admin
    passwd root
