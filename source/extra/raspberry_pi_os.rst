Raspberry Pi OS Images
----------------------

Most of these images are built using the code at
https://github.com/RPi-Distro/pi-gen/ (maybe).

The faster, more useful download link is
https://downloads.raspberrypi.org/.

The shitty, less-automated download link is
https://www.raspberrypi.org/downloads/.


Berryboot
---------

* http://www.berryterminal.com/doku.php/berryboot
* http://sourceforge.net/projects/berryboot/files/
* http://sourceforge.net/projects/berryboot/files/os_images/


Flash Image
-----------

If you have a pesky zip file::

    unzip 2016-05-27-raspbian-jessie-lite.zip
    sudo dd if=2016-05-27-raspbian-jessie-lite.img of=/dev/sdz bs=4M
    sync

    touch /dev/sdz/boot/ssh


Fix All The Broken Stuff
------------------------

A lot of horrible defaults have been chosen for you.  You can fix them with::

    # Locale Stuff
    sudo raspi-config nonint do_change_locale en_CA.UTF-8
    sudo raspi-config nonint do_configure_keyboard us
    sudo raspi-config nonint do_change_timezone UTC  # or America/Toronto

    # Networking Stuff
    sudo raspi-config nonint do_wifi_country CA
    sudo raspi-config nonint do_hostname ${NEWHOSTNAME}
    sudo raspi-config nonint do_ssh 0
    sudo apt-get --yes purge libpam-chksshpwd

    # Display Stuff
    sudo raspi-config nonint do_overscan 1  # or uncomment 'disable_overscan=1' in /boot/config.txt
    sudo bash -c "sed -i 's/$/ logo.nologo/' /boot/cmdline.txt"

    # Not needed anymore?
    sudo raspi-config nonint do_expand_rootfs


Fix Default Password
--------------------

::

    sudo raspi-config nonint do_change_pass


Firmware Upgrades
-----------------

::

    sudo rpi-eeprom-update        # check if any are available
    sudo rpi-eeprom-update -a -d  # just blindly apply them


Update Everything
-----------------

Images are always stale.  Update them with::

    sudo apt-get update
    sudo apt-get --yes dist-upgrade
    sudo apt-get --yes autoremove
    sudo apt-get autoclean
    sudo apt-get clean


Install Go
----------

::

    wget https://golang.org/dl/${TARBALL}
    sudo tar -C /usr/local -xzf ${TARBALL}


Assorted Links
--------------

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

    get_json_string_val() {
        python -c "import json,sys;sys.stdout.write(json.dumps(json.load(sys.stdin)$1))";
    }

    FOO=$(cat os_config.json | get_json_string_val "['flavour']")
    BAR=$(cat os_config.json | get_json_string_val "['language']")
    BAZ=$(cat os_config.json | get_json_string_val "['keyboard']")

    echo $FOO
    echo $BAR
    echo $BAZ


Hardware
--------

* https://www.dfrobot.com/product-2242.html
* https://lincolnbinns.com/shop/internet-of-things-iot/raspberry-pi4-enclosures/raspberry-pi4-accessories/pi4-extender-board.html


Camera Stuff
------------

* https://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera
* https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
* https://github.com/jasaw/bbPiCam
* https://www.linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera
* https://www.waveshare.com/wiki/RPi_IR-CUT_Camera
* https://www.amazon.ca/gp/product/B01M1BZXJQ
* https://www.amazon.ca/gp/product/B0056XFS5S
* https://www.amazon.ca/gp/product/B003AXEFMI
* http://nestboxtech.blogspot.ca/2014/10/how-to-make-your-own-raspberry-pi-trail.html
* http://www.instructables.com/id/PiPoE-powering-a-Raspberry-Pi-over-Ethernet/
* https://ruha.camera/

850 nm near IR


Encrypted Root
--------------

* https://gist.github.com/gea0/4fc2be0cb7a74d0e7cc4322aed710d38
* https://wiki.polaire.nl/doku.php?id=archlinux-raspberry-encrypted
