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


OSMC Stuff
----------

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


Modern Netflix
--------------

* https://mytruemedia.com/best-kodi-addons/how-to-install-netflix-kodi-18-addon/

::

    1.  Go to the Kodi File manager found in the Settings System menu.
    2.  Click Add source and then None. Then, enter http://absolut-kodi.com/repo and name it absolut.
    3.  In the Add-on browser, click Install from zip file.
    4.  Select the absolut source then click the repository.Absolut.Kodi-1.0.5.zip within to install the repo.
    5.  Once you notice the repo has installed, go back and click Install from Repository >> Absolut Repo >> Video addons.
    6.  Select Netflix then click Install.

    7.  DAFUQ?!?  pycryptodomex missing?!?  pip not installed?!?
