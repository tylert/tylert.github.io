Pi First Boot
=============


Download Image
--------------


Raspbian Lite
~~~~~~~~~~~~~

Fetch the latest image from
https://downloads.raspberrypi.org/raspbian_lite/images/.

If you have trouble finding that, try
https://www.raspberrypi.org/downloads/raspbian/ instead.


Raspbian
~~~~~~~~

Fetch the latest image from https://downloads.raspberrypi.org/raspbian/images/.

If you have trouble finding that, try
https://www.raspberrypi.org/downloads/raspbian/ instead.


OSMC
~~~~

Fetch the latest image from https://osmc.tv/download/.


RetroPie
~~~~~~~~

Fetch the latest image from
http://blog.petrockblock.com/retropie/retropie-downloads/.


Ubuntu
~~~~~~

Fetch the latest image from https://ubuntu-pi-flavour-maker.org/download/.


NOOBS Lite
~~~~~~~~~~

Fetch the latest image from
https://downloads.raspberrypi.org/NOOBS_lite/images/.

If you have trouble finding that, try
https://www.raspberrypi.org/downloads/noobs/ instead.


NOOBS
~~~~~

Fetch the latest image from https://downloads.raspberrypi.org/NOOBS/images/.

If you have trouble finding that, try
https://www.raspberrypi.org/downloads/noobs/ instead.


Other
~~~~~

Fetch the latest image from https://www.raspberrypi.org/downloads/.


Berryboot
~~~~~~~~~

TBD

http://www.berryterminal.com/doku.php/berryboot
http://sourceforge.net/projects/berryboot/files/
http://sourceforge.net/projects/berryboot/files/os_images/


Flash Image
-----------

If you have a pesky zip file::

    unzip 2016-05-27-raspbian-jessie-lite.zip
    sudo dd if=2016-05-27-raspbian-jessie-lite.img of=/dev/sdc bs=4M
    sudo sync


Fix Broken Stuff
----------------


Fix Locale
~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Internationalisation Options' -> 'Change Locale'
    # Select 'en_CA.UTF-8'


Fix Keyboard
~~~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Internationalisation Options' -> 'Change Keyboard Layout'
    # Select 'English (US)'


Fix Password
~~~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Change User Password'
    # Type in new password


Fix Timezone
~~~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Internationalisation Options' -> 'Change Timezone'
    # Select 'America/Toronto'


Fix WiFi Country
~~~~~~~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Internationalisation Options' -> 'Change Wi-fi Country'
    # Select 'CA Canada'


Fix Overscan
~~~~~~~~~~~~

FIXME Do this better.

::

    # Uncomment 'disable_overscan=1' in /boot/config.txt
    sudo reboot


Remove Boot Logo
~~~~~~~~~~~~~~~~

FIXME Do this better.

::

    # Add ' logo.nologo' to the end of /boot/cmdline.txt
    sudo reboot


Fix Hostname
~~~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Advanced Options' -> 'Hostname'
    # Choose new hostname string


Update Everything
~~~~~~~~~~~~~~~~~

Images are always stale.  Update them with::

    sudo apt-get update
    sudo apt-get --yes dist-upgrade
    sudo reboot


Enable SSH
~~~~~~~~~~

FIXME Do this better.

::

    sudo raspi-config
    # 'Advanced Options' -> 'SSH'
    # Select 'yes'


Activate MPEG Stuff
-------------------

Go buy a license key from http://www.raspberrypi.com/mpeg-2-license-key/.

Wait up to 24 hours for an email to arrive with your license key.

FIXME Do this better.

::

    # Add 'decode_MPG2=0xdeadbeef' to /boot/config.txt
    sudo reboot

To verify that it worked after a reboot, type::

    vcgencmd codec_enabled MPG2
