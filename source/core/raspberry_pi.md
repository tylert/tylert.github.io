# Raspberry Pi OS Images

Most of these images are built using the code at
<https://github.com/RPi-Distro/pi-gen> (maybe).

The faster, more useful download link is
<https://downloads.raspberrypi.org>.

The shitty, less-automated download link is
<https://raspberrypi.org/downloads>.


# Berryboot

- <https://berryterminal.com/doku.php/berryboot>
- <https://sourceforge.net/projects/berryboot/files>
- <https://sourceforge.net/projects/berryboot/files/os_images>


# Flash Image

If you have a pesky zip file:

```
    unzip 2016-05-27-raspbian-jessie-lite.zip
    dd if=2016-05-27-raspbian-jessie-lite.img of=/dev/sdz bs=4M
    sync

    touch /dev/sdz/boot/ssh
    openssl passwd -6  # append to user:hash in boot/userconf.txt
```

- <https://raspberrypi.com/documentation/computers/configuration.html#configuring-a-user>
- <https://raspberrypi.com/documentation/computers/remote-access.html>
- <https://raspberrypi.com/documentation/computers/configuration.html>


# Fix All The Broken Stuff

A lot of horrible defaults have been chosen for you. You can fix them
with:

```
    # Locale Stuff
    raspi-config nonint do_change_locale en_CA.UTF-8
    raspi-config nonint do_configure_keyboard us
    raspi-config nonint do_change_timezone UTC  # or America/Toronto

    # Networking Stuff
    raspi-config nonint do_wifi_country CA
    raspi-config nonint do_hostname ${NEWHOSTNAME}
    raspi-config nonint do_ssh 0
    apt-get --yes purge libpam-chksshpwd

    # Display Stuff
    raspi-config nonint do_overscan 1  # or uncomment 'disable_overscan=1' in /boot/config.txt
    bash -c "sed -i 's/$/ logo.nologo/' /boot/cmdline.txt"
```


# Fix Default Password

```
    passwd pi
```


# Update Everything

Images are always stale. Update them with:

```
    apt-get update
    apt-get --yes dist-upgrade
    apt-get --yes autoremove
    apt-get autoclean
    apt-get clean
```


# Install Wireguard

```
    apt-get --yes install wireguard-tools
```


# Firmware Upgrades

```
    rpi-eeprom-update        # check if any are available
    rpi-eeprom-update -a -d  # just blindly apply them
```


# Install Go

```
    wget https://golang.org/dl/${TARBALL}
    tar -C /usr/local -xzf ${TARBALL}
```


# Assorted Links

- <https://github.com/raspberrypi/linux/blob/rpi-4.0.y/Documentation/kernel-parameters.txt>
- <https://raspberrypi.org/forums/viewtopic.php?f=66&t=41520&p=343793>
- <https://gist.github.com/abulte/3941653>
- <https://gist.github.com/sturadnidge/5630813>
- <https://github.com/Wookie/rpi_image_builder>
- <https://github.com/RPi-Distro/pi-gen>
- <https://12dash.com>
- <https://downloads.raspberrypi.org>
- <https://wiki.openwrt.org/toh/raspberry_pi_foundation/raspberry_pi>
- <https://amazon.ca/BQLZR-3000mA-Mobile-Charger-Adapter/dp/B00LWQH99Q/ref=cm_cd_al_qh_dp_t>
- <https://hardill.me.uk/wordpress/2019/11/02/pi4-usb-c-gadget>


# Raspbian Stuff

```
    get_json_string_val() {
        python -c "import json,sys;sys.stdout.write(json.dumps(json.load(sys.stdin)$1))";
    }

    FOO=$(cat os_config.json | get_json_string_val "['flavour']")
    BAR=$(cat os_config.json | get_json_string_val "['language']")
    BAZ=$(cat os_config.json | get_json_string_val "['keyboard']")

    echo $FOO
    echo $BAR
    echo $BAZ
```


# Hardware

- <https://dfrobot.com/product-2242.html>
- <https://lincolnbinns.com/shop/internet-of-things-iot/raspberry-pi4-enclosures/raspberry-pi4-accessories/pi4-extender-board.html>
- <https://github.com/TzuHuanTai/RaspberryPi_WebRTC>
- <https://josh.pencheon.dev/2025/01/05/manually-updating-raspberry-pi-eeprom.html> fetching and installing EEPROM images
- <https://github.com/raspberrypi/rpi-eeprom> rpi-eeprom-update shell script and EEPROM bin files


# UEFI

- <https://github.com/pftf/RPi4> boot arm64 ISO images just like you can on amd64!!!


# Encrypted Root

- <https://gist.github.com/gea0/4fc2be0cb7a74d0e7cc4322aed710d38>
- <https://wiki.polaire.nl/doku.php?id=archlinux-raspberry-encrypted>


# Kiosk

- <https://alexba.in/blog/2013/01/07/use-your-raspberrypi-to-power-a-company-dashboard>

Do all the usual stuff with raspi-config first.

Install packages needed for chromium:

```
    apt-get --yes install chromium ttf-mscorefonts-installer
```

Make sure the mouse cursor hides itself when it isn\'t being used:

```
    apt-get --yes install unclutter
```

To make chromium automatically start at boot time, add the following line to
/home/pi/.config/lxsession/LXDE-pi/autostart:

```
    chromium --kiosk https://bla.bla.bla --incognito
```

It might also be helpful to add a symlink to it in the user's home directory to
make it easier to find with:

```
    ln -s /home/pi/.config/lxsession/LXDE-pi/autostart /home/pi
```

To disable the screensaver, uncomment or add the following lines to
/etc/lightdm/lightdm.conf:

```
    [SeatDefaults]
    xserver-command=X -s 0 -dpms
```

To cut down on the boot chatter, add the following to the end of the
line in /boot/cmdline.txt:

```
    logo.nologo loglevel=3
```
