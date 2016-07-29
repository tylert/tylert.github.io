Raspberry Pi Stuff
==================

* http://bobbyromeo.com/technology/triple-boot-raspberry-pi-on-usb-raspbianretropieopenelec-part-2/
* https://github.com/raspberrypi/linux/blob/rpi-4.0.y/Documentation/kernel-parameters.txt
* https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=41520&p=343793
* https://gist.github.com/abulte/3941653
* https://gist.github.com/sturadnidge/5630813
* https://github.com/Wookie/rpi_image_builder
* https://12dash.com

Adding codec junk::

    echo "decode_MPG2=0xdeadbeef" >> /boot/config.txt
    reboot
    vcgencmd codec_enabled MPG2

Turn off annoying raspberries::

    echo -n ‘ logo.nologo’ >> /boot/cmdline.txt

::

    # On Mac OS X
    wget https://downloads.raspberrypi.org/raspbian_lite_latest -O 2015-11-21-raspbian-jessie-lite.zip
    shasum -a 1 2015-11-21-raspbian-jessie-lite.zip
    # sha1sum 97888fcd9bfbbae2a359b0f1d199850852bf0104
    unzip 2015-11-21-raspbian-jessie-lite.zip
    diskutil unmountDisk /dev/disk2
    sudo dd if=2015-11-21-raspbian-jessie-lite.img of=/dev/disk2 bs=4m

    # On SD/uSD
    sed /boot/config.txt -i -e ‘s/^overscan_/#overscan_/’
    uncomment ‘disable_overscan=1’ in /boot/config.txt

    # On Raspbian
    sudo dpkg-reconfigure locales
    sudo raspi-config --expand-rootfs ; sudo reboot
    sudo apt-get update ; sudo apt-get --yes dist-upgrade ; sudo reboot
    sudo apt-get install dnsmasq

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

    <sources>
        <programs>
            <default pathversion="1"></default>
        </programs>
        <video>
            <default pathversion="1"></default>
            <source>
                <name>television</name>
                <path pathversion="1">/home/user/far/television/</path>
                <allowsharing>true</allowsharing>
            </source>
            <source>
                <name>movie</name>
                <path pathversion="1">/home/user/far/movie/</path>
                <allowsharing>true</allowsharing>
            </source>
        </video>
        <music>
            <default pathversion="1"></default>
            <source>
                <name>audio</name>
                <path pathversion="1">/home/user/far/audio/</path>
                <allowsharing>true</allowsharing>
            </source>
        </music>
        <pictures>
            <default pathversion="1"></default>
            <source>
                <name>photo</name>
                <path pathversion="1">/home/user/far/photo/</path>
                <allowsharing>true</allowsharing>
            </source>
        </pictures>
        <files>
            <default pathversion="1"></default>
            <source>
                <name>SuperRepo</name>
                <path pathversion="1">http://srp.nu/</path>
                <allowsharing>true</allowsharing>
            </source>
        </files>
    </sources>

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

    #echo >> /etc/rc.local <EOF
    #sleep 20
    #sudo -u osmc sshfs osmc@file:/television /home/osmc/TV\ Shows
    #sudo -u osmc sshfs osmc@file:/movie /home/osmc/Movies
    #sudo -u osmc sshfs osmc@file:/audio /home/osmc/Music
    #sudo -u osmc sshfs osmc@file:/photo /home/osmc/Pictures
    #
    #exit
    #EOF

Video Plug-ins -> Genesis

* http://srp.nu
* http://fusion.tvaddons.ag
