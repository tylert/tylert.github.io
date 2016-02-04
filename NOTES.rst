Python Stuff
------------

* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
* http://flask-restful.readthedocs.org/en/0.3.5/quickstart.html#a-minimal-api
* http://locust.io/

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


Go Stuff
--------

* http://howistart.org/posts/go/1


Apt-cacher-ng Stuff
-------------------

* http://www.boehmi.net/index.php/blog/14-how-to-setup-an-apt-cacher-ng-server-in-ubuntu
* https://help.ubuntu.com/community/Apt-Cacher-Server
* https://help.ubuntu.com/community/AutomateAptCacheNgProxySettings?highlight=%28\bCategoryInternet\b%29
* http://docs.docker.com/examples/apt-cacher-ng/

(on apt-cacher-ng server)::

    apt-get install apt-cacher-ng

(on servers and clients, assuming server is 10.0.2.4)
New file /etc/apt/apt.conf.d/98check-proxy::

    APT::Update::Pre-Invoke {
      "ping -c1 -W1 10.0.2.4; if [ $? == \"0\" ]; then echo \"Acquire::http::Proxy 'http://10.0.2.4:3142'\;\" > /etc/apt/apt.conf.d/99use-proxy; else echo \"\" > /etc/apt/apt.conf.d/99use-proxy; fi"
    }


Docker
------

* http://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container/
* http://prakhar.me/docker-curriculum/
* http://stable.release.core-os.net/amd64-usr/current/
* http://stackoverflow.com/questions/18274088/how-can-i-make-my-own-base-image-for-docker
* http://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html
* http://www.aossama.com/build-debian-docker-image-from-scratch/
* https://blog.docker.com/2013/06/create-light-weight-docker-containers-buildroot/
* https://developer.atlassian.com/blog/2015/12/atlassian-docker-orchestration/


Install Stuff
-------------

::

    sudo add-apt-repository ppa:inkscape.dev/stable
    sudo apt-add-repository ppa:system76-dev/stable


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


Android Stuff
-------------

::

    sudo dpkg --add-architecture i386
    sudo apt-get update 
    sudo apt-get install libc6:i386 libstdc++6:i386


LDAP/Kerberos
-------------

* http://aput.net/~jheiss/krbldap/howto.html
* http://www.roguelynn.com/words/explain-like-im-5-kerberos/
* https://help.ubuntu.com/lts/serverguide/kerberos-ldap.html
* https://wiki.debian.org/LDAP/Kerberos


Stupid Shell Tricks
-------------------

* http://www.theunixschool.com/2012/10/how-to-find-duplicate-records-of-file.html
* http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html


Backups
-------

* http://duplicity.nongnu.org/features.html
* http://support.code42.com/CrashPlan/Latest/Configuring/Upgrading_CrashPlan_Security_To_Custom_448_Bit_Key
* http://support.code42.com/CrashPlan/Latest/Configuring/Using_CrashPlan_On_A_Headless_Computer
* http://www.code42.com/crashplan/download/
* http://www.mikerubel.org/computers/rsync_snapshots/
* http://www.unixmen.com/install-crashplan-backup-tool-in-linux/
* https://blog.interlinked.org/tutorials/rsync_time_machine.html
* https://github.com/Backblaze/B2_Command_Line_Tool
* https://www.backblaze.com/b2/cloud-storage.html
* https://www.code42.com/store/


Assorted Things-to-Read
-----------------------

* http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
* http://blogs.aws.amazon.com/security/post/Tx2MUS2R3CMGG8H/Enable-a-New-Feature-in-the-AWS-Management-Console-Cross-Account-Access
* http://chris.beams.io/posts/git-commit/
* http://lett.be/oauth2/
* http://randsinrepose.com/archives/bored-people-quit/
* http://randsinrepose.com/archives/the-update-the-vent-and-the-disaster/
* http://unix.stackexchange.com/questions/66154/ssh-causes-while-loop-to-stop
* http://www.daedtech.com/how-to-keep-your-best-programmers
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it/
* https://aws.amazon.com/blogs/aws/new-amazon-elasticsearch-service/
* https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
* https://medium.com/swlh/agile-is-the-new-waterfall-f7baef5d026d
* http://redsquirrel.com/dave/work/a2j/patterns/BreakableToys.html


Zoom Stuff
----------

* https://support.zoom.us/hc/en-us/articles/204206269-Getting-Started-on-Linux


MySQL Stuff
-----------

::

    select concat('KILL ',id,';') from information_schema.processlist where command='Sleep';

::

    #!/bin/bash

    echo "Killing existing xlsws_category queries"
    for process_id in `mysql -e "show full processlist" | grep 'xlsws_category' | awk '{print $1}'`
    do
      echo "- process: ${process_id}"
      mysql -e "kill ${process_id}"
    done


Keepass Stuff
-------------

* http://blog.sharedmemory.fr/en/2014/04/30/keepass-file-format-explained/
* https://github.com/asmpro/keepasspy
* https://github.com/fdemmer/libkeepass
* https://github.com/jamesls/python-keepassx
* https://github.com/keepassx/keepassx
* https://github.com/kindahl/libkeepass
* https://github.com/phpwutz/libkeepass
* https://www.keepassx.org


Cool Products
-------------

* http://nwavguy.blogspot.ca/2011/07/o2-headphone-amp.html


Stuff to watch
--------------

* https://drive.google.com/a/lightspeedretail.com/folderview?id=0B8u-re5tDrX8fldWX3I1VnNNVnlxSmJBRzB5VEVSc2ZkTkdTUDctSW1hSDV5NFliVHJ5QVU&usp=drive_web#list
* https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/
* https://www.youtube.com/watch?v=cn7QLSPB3OA
* https://www.youtube.com/watch?v=fVMlxJJNmyA
* https://www.youtube.com/watch?v=uicjqeZO690&list=WL&index=9


Current Stuff
-------------

* https://github.com/WhoopInc/vagrant-s3auth
* https://github.com/mlafeldt/chef-runner


Keyboard CNC
------------

* https://geekhack.org/index.php?topic=65747.0


Raspberry Pi Stuff
------------------

* http://bobbyromeo.com/technology/triple-boot-raspberry-pi-on-usb-raspbianretropieopenelec-part-2/
* https://github.com/raspberrypi/linux/blob/rpi-4.0.y/Documentation/kernel-parameters.txt
* https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=41520&p=343793

::

    # On Mac OS X
    wget https://downloads.raspberrypi.org/raspbian_lite_latest -O 2015-11-21-raspbian-jessie-lite.zip
    shasum -a 1 2015-11-21-raspbian-jessie-lite.zip
    # sha1sum 97888fcd9bfbbae2a359b0f1d199850852bf0104
    unzip 2015-11-21-raspbian-jessie-lite.zip
    diskutil unmountDisk /dev/disk2
    sudo dd if=2015-11-21-raspbian-jessie-lite.img of=/dev/disk2 bs=4m

    # On SD/uSD
    echo -n ‘ logo.nologo’ >> /boot/cmdline.txt
    sed /boot/config.txt -i -e ‘s/^overscan_/#overscan_/’
    uncomment ‘disable_overscan=1’ in /boot/config.txt

    # On Raspbian
    sudo dpkg-reconfigure locales
    sudo raspi-config --expand-rootfs ; sudo reboot
    sudo apt-get update ; sudo apt-get --yes dist-upgrade ; sudo reboot
    sudo apt-get install dnsmasq


Kobo Stuff
----------

::

    127.0.0.1 host localhost.localdomain localhost localhost localhost.localdomain
    127.0.0.1 www.google-analytics.com ssl.google-analytics.com google-analytics.com

::

    cd KOBOeReader/.kobo
    sqlite3 KoboReader.sqlite
    INSERT INTO user VALUES('', '', '', '', '', '', '', '', '', '', '', '', '');
    .quit

::

    ebook-convert dummy.html .epub


Awesome Font Stuff
------------------

* http://www.1001fonts.com/


Git Stuff
---------

::

    # Snip out just a single directory
    git clone foo
    cd foo
    git remote rm origin
    git filter-branch --subdirectory-filter arf --prune-empty -- --all


    # Get rid of files permanently
    for i in foo.svg bar.svg ; do
      git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch $i" --prune-empty -f HEAD
    done


    # Fix the size of the repository by losing unreferenced things
    git reflog expire --expire=now --all
    git fsck --full --unreachable
    git gc --prune=now --aggressive

    rm -rf .git/refs/original/*
    git reflog expire --all --expire-unreachable=0
    git repack -A -d
    git prune


    # Fix email for old commits
    git filter-branch --env-filter 'GIT_AUTHOR_NAME="Tyler Tidman" ; GIT_COMMITTER_NAME="Tyler Tidman"' -f -- --all
    git filter-branch --env-filter 'GIT_AUTHOR_EMAIL="tyler.tidman@draak.ca" ; GIT_COMMITTER_EMAIL="tyler.tidman@draak.ca"' -f -- --all
    git show-ref
    git update-ref -d refs/original/refs/heads/master


    # Cull a single directory
    git filter-branch --tree-filter 'rm -rf radio/logos/ares' -f HEAD
    git filter-branch --prune-empty -f HEAD


    # Stitch two repos together
    cd Adir
    mkdir Bdir
    git remote add -f Bproject /path/to/Brepo
    git merge -s ours --no-commit Bproject/master
    git read-tree --prefix=Bdir -u Bproject/master
    git commit -m "Merge B project as our subdirectory"
    git pull -s subtree Bproject master
