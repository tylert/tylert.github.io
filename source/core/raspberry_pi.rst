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


Fix Default Password
--------------------

::

    passwd pi


Update Everything
-----------------

Images are always stale.  Update them with::

    sudo apt-get update
    sudo apt-get --yes dist-upgrade
    sudo apt-get --yes autoremove
    sudo apt-get autoclean
    sudo apt-get clean


Install Wireguard
-----------------

::

    sudo apt-get --yes install wireguard-tools


Firmware Upgrades
-----------------

::

    sudo rpi-eeprom-update        # check if any are available
    sudo rpi-eeprom-update -a -d  # just blindly apply them


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


UEFI
----

* https://github.com/pftf/RPi4  boot arm64 ISO images just like you can on amd64!!!


Encrypted Root
--------------

* https://gist.github.com/gea0/4fc2be0cb7a74d0e7cc4322aed710d38
* https://wiki.polaire.nl/doku.php?id=archlinux-raspberry-encrypted


Kiosk
-----

* http://alexba.in/blog/2013/01/07/use-your-raspberrypi-to-power-a-company-dashboard/

Do all the usual stuff with raspi-config first.

Install packages needed for chromium::

    sudo apt-get install chromium ttf-mscorefonts-installer

Make sure the mouse cursor hides itself when it isn't being used::

    sudo apt-get install unclutter

To make chromium automatically start at boot time, add the following line to
/home/pi/.config/lxsession/LXDE-pi/autostart::

    chromium --kiosk http://bla.bla.bla --incognito

It might also be helpful to add a symlink to it in the user's home directory
to make it easier to find with::

    ln -s /home/pi/.config/lxsession/LXDE-pi/autostart /home/pi

To disable the screensaver, uncomment or add the following lines to
/etc/lightdm/lightdm.conf::

    [SeatDefaults]
    xserver-command=X -s 0 -dpms

To cut down on the boot chatter, add the following to the end of the line in
/boot/cmdline.txt::

    logo.nologo loglevel=3
