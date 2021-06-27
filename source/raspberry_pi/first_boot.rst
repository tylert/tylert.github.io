Pi First Boot
=============


Download Images
---------------

Most of these images are built using the code at
https://github.com/RPi-Distro/pi-gen/.

The faster, more useful download link is
https://downloads.raspberrypi.org/.

The slower, less-automated download link is
https://www.raspberrypi.org/downloads/.


Berryboot
~~~~~~~~~

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
    sudo raspi-config nonint do_hostname moopoo
    sudo raspi-config nonint do_ssh 0
    sudo apt-get --yes purge libpam-chksshpwd

    # Display Stuff
    sudo raspi-config nonint do_overscan 1  # or uncomment 'disable_overscan=1' in /boot/config.txt
    sudo bash -c "sed -i 's/$/ logo.nologo/' /boot/cmdline.txt"

    # Not needed anymore?
    sudo raspi-config nonint do_expand_rootfs


Fix Password
~~~~~~~~~~~~

::

    sudo raspi-config nonint do_change_pass


Update Everything
~~~~~~~~~~~~~~~~~

Images are always stale.  Update them with::

    sudo apt-get update
    sudo apt-get --yes dist-upgrade
    sudo apt-get --yes autoremove
    sudo apt-get autoclean
    sudo apt-get clean


Activate MPEG Stuff (DEPRECATED)
--------------------------------

Go buy license key(s) from http://www.raspberrypi.com/mpeg-2-license-key/ and
http://www.raspberrypi.com/vc-1-license-key/.

Wait up to 24 hours for an email to arrive with your keys.

FIXME Do this better::

    # Add 'decode_MPG2=0xdeadbeef' to /boot/config.txt
    # Add 'decode_WVC1=0xdeadbeef' to /boot/config.txt

To verify that it worked after a reboot, type::

    vcgencmd codec_enabled MPG2
    vcgencmd codec_enabled WVC1

The less painful way of enabling the codecs::

    cd /boot
    cp start_x.elf start_x.elf.backup && \
        perl -pne 's/\x47\xE9362H\x3C\x18/\x47\xE9362H\x3C\x1F/g' < start_x.elf.backup > start_x.elf

* https://www.reddit.com/r/raspberry_pi/comments/5x7xbo/patch_for_mpeg2_vc1_license/
* https://news.ycombinator.com/item?id=16381331
