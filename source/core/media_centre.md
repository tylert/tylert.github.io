# LibreELEC

* <https://wiki.archlinux.org/index.php/ConnMan>
* <https://git.kernel.org/pub/scm/network/connman/connman.git>
* <https://jeffgeerling.com/blog/2022/using-libreelec-pro-management-ssh>


# Netflix

* <https://itnext.io/the-2021-onward-guide-to-install-netflix-on-raspberry-pi-smartphone-as-the-remote-control-2e7662ccc80>
* <https://github.com/oss001/KodiStreaming/blob/master/setup.sh>
* <https://makingstuffwork.net/technology/watch-netflix-amazon-prime-kodi>
* <https://raspberrytips.com/install-netflix-on-kodi>
* <https://raw.githubusercontent.com/zjoasan/netflix-install-script/master/netflix_prep_install.sh>
* <https://hackster.io/sbcomponentsuk/netflix-and-amazon-prime-video-now-streaming-on-raspberry-pi-44f3cb>


# OMFG Kodi CLI

* <https://forum.kodi.tv/showthread.php?tid=120248&pid=2664155#pid2664155>
* <https://mankier.com/1/kodi-send>
* <https://github.com/jose1711/kodi-ansible-role>
* <https://github.com/nawar/kodi-cli>


# OSMC on Debian

```
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
```


# Activate MPEG Stuff (DEPRECATED)

Go buy license key(s) from <https://raspberrypi.com/mpeg-2-license-key>
and <https://raspberrypi.com/vc-1-license-key>.

Wait up to 24 hours for an email to arrive with your keys.

FIXME Do this better:

```
    # Add 'decode_MPG2=0xdeadbeef' to /boot/config.txt
    # Add 'decode_WVC1=0xdeadbeef' to /boot/config.txt
```

To verify that it worked after a reboot, type:

```
    vcgencmd codec_enabled MPG2
    vcgencmd codec_enabled WVC1
```

The less painful way of enabling the codecs:

```
    cd /boot
    cp start_x.elf start_x.elf.backup && \
        perl -pne 's/\x47\xE9362H\x3C\x18/\x47\xE9362H\x3C\x1F/g' < start_x.elf.backup > start_x.elf
```

* <https://reddit.com/r/raspberry_pi/comments/5x7xbo/patch_for_mpeg2_vc1_license>
* <https://news.ycombinator.com/item?id=16381331>


# Other

* <https://johnlian.net/posts/hdmi-cec> HDMI-CEC
