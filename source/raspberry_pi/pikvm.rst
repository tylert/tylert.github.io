PiKVM Stuff
-----------

* https://pikvm.org/
* https://github.com/pikvm/pikvm

Web default login is:  "admin" with password "admin"
SSH default login is:  "root" with password "root"

Look under "pages" in the GitHub repo for additional documentation.


USB-C OTG + Power Splitter
--------------------------

* https://www.tindie.com/products/8086net/usb-cpwr-splitter/
* https://www.buyapi.ca/product/usb-c-pwr-splitter/


ATX Control
-----------

* https://perdeas.bigcartel.com/product/pi-kvm-atx-controller
* https://www.ebay.com/itm/Pi-KVM-ATX-Controller-board-Fully-assembled-and-tested/265214220357
* https://www.reddit.com/r/pikvm/comments/mmiz34/custom_pcb_to_control_atx_without_breadboarding/


Multiple Units
--------------

* https://blog.ktz.me/pikvm-controlling-up-to-4-servers-simultaneously/


Upgrades
--------

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
