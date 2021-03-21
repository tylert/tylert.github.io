Raspberry Pi Stuff
==================

* http://bobbyromeo.com/technology/triple-boot-raspberry-pi-on-usb-raspbianretropieopenelec-part-2/
* https://github.com/raspberrypi/linux/blob/rpi-4.0.y/Documentation/kernel-parameters.txt
* https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=41520&p=343793
* https://gist.github.com/abulte/3941653
* https://gist.github.com/sturadnidge/5630813
* https://github.com/Wookie/rpi_image_builder
* https://github.com/RPi-Distro/pi-gen
* https://12dash.com
* http://downloads.raspberrypi.org/
* http://www.berryterminal.com/doku.php/berryboot
* https://wiki.openwrt.org/toh/raspberry_pi_foundation/raspberry_pi
* http://www.kaibader.de/homemade-minimal-raspberry-pi-raspbian-image/
* https://www.amazon.ca/BQLZR-3000mA-Mobile-Charger-Adapter/dp/B00LWQH99Q/ref=cm_cd_al_qh_dp_t
* https://www.hardill.me.uk/wordpress/2019/11/02/pi4-usb-c-gadget/


Raspbian Stuff
--------------

::

    sudo dpkg-reconfigure locales
    sudo raspi-config --expand-rootfs ; sudo reboot

::

    get_json_string_val() {
        python -c "import json,sys;sys.stdout.write(json.dumps(json.load(sys.stdin)$1))";
    }

    FOO=$(cat os_config.json | get_json_string_val "['flavour']")
    BAR=$(cat os_config.json | get_json_string_val "['language']")
    BAZ=$(cat os_config.json | get_json_string_val "['keyboard']")

    echo $FOO
    echo $BAR
    echo $BAZ


OSMC on Debian
--------------

::

    #!/usr/bin/env bash

    # http://software.opensuse.org/download.html?project=home:osmc&package=osmc-installer
    # s/8.0/7.0/ for wheezy

    wget -O - \
      http://download.opensuse.org/repositories/home:osmc/Debian_8.0/Release.key |\
      apt-key add -

    echo 'deb http://download.opensuse.org/repositories/home:/osmc/Debian_8.0/ /' \
      > /etc/apt/sources.list.d/osmc-installer.list

    apt-get update
    apt-get install osmc-installer


LibreELEC
---------

The networking stuff for LibreELEC is "slightly weird".

* https://wiki.archlinux.org/index.php/ConnMan
* https://git.kernel.org/pub/scm/network/connman/connman.git


Netflix
-------

* https://itnext.io/the-2021-onward-guide-to-install-netflix-on-raspberry-pi-smartphone-as-the-remote-control-2e7662ccc80


OMFG Kodi CLI!!!
----------------

* https://forum.kodi.tv/showthread.php?tid=120248&pid=2664155#pid2664155
* https://www.mankier.com/1/kodi-send
* https://github.com/jose1711/kodi-ansible-role
* https://github.com/nawar/kodi-cli
