Raspberry Pi Stuff
==================

* http://bobbyromeo.com/technology/triple-boot-raspberry-pi-on-usb-raspbianretropieopenelec-part-2/
* https://github.com/raspberrypi/linux/blob/rpi-4.0.y/Documentation/kernel-parameters.txt
* https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=41520&p=343793
* https://gist.github.com/abulte/3941653
* https://gist.github.com/sturadnidge/5630813
* https://github.com/Wookie/rpi_image_builder
* https://12dash.com

::

    # On Mac OS X
    wget https://downloads.raspberrypi.org/raspbian_lite_latest -O 2015-11-21-raspbian-jessie-lite.zip
    shasum -a 1 2015-11-21-raspbian-jessie-lite.zip
    # sha1sum 97888fcd9bfbbae2a359b0f1d199850852bf0104
    unzip 2015-11-21-raspbian-jessie-lite.zip
    diskutil unmountDisk /dev/disk2
    sudo dd if=2015-11-21-raspbian-jessie-lite.img of=/dev/disk2 bs=4m

    # On Raspbian
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


Codec Stuff
-----------

::

    cd /boot
    cp start.elf start.elf_backup && \
        perl -pne 's/\x47\xE9362H\x3C\x18/\x47\xE9362H\x3C\x1F/g' < start.elf_backup > start.elf

* https://www.reddit.com/r/raspberry_pi/comments/5x7xbo/patch_for_mpeg2_vc1_license/
* https://news.ycombinator.com/item?id=16381331
