Configuring EdgeRouter Properly
-------------------------------

* https://kb.intermedia.net/Article/44415
* https://nelsonslog.wordpress.com/2018/06/26/ubiquiti-edgemax-edgeos-local-dns/
* https://loganmarchione.com/2016/08/edgerouter-lite-dnsmasq-setup/
* https://help.ui.com/hc/en-us/articles/115002673188-EdgeRouter-DHCP-Server-using-Dnsmasq
* https://ragingtiger.github.io/2018/04/29/ubq-erx-router-setup/
* https://www.edgerouterconfig.nl/reset-edgerouter-to-factroy-defaults/
* https://mynetworktraining.com/blog/216523/reset-the-configuration-of-the-ubiquiti-edgerouter-x-to-default

::

    configure
    set service dhcp-server use-dnsmasq enable
    commit
    save


Installing UniFi Controller
---------------------------

* https://blog.jessfraz.com/post/home-lab-is-the-dopest-lab/
* https://www.linuxserver.io/2016/02/13/manage-a-unifi-ap-via-the-ubiquiti-controller-running-in-docker/
* https://help.ubnt.com/hc/en-us/articles/220066768-UniFi-How-to-Install-Update-via-APT-on-Debian-or-Ubuntu
* https://bobmckay.com/coding-for-kids/running-ubiquiti-unifi-controller-raspberry-pi/
* https://gist.github.com/codeniko/381e8be3b0236a602e02f0a9fac13b3d
* https://bobmckay.com/coding-for-kids/running-ubiquiti-unifi-controller-raspberry-pi/

::

    # UniFi
    sudo apt-get --yes install openjdk-8-jre-headless
    sudo apt-get --yes install ./unifi_sysvinit_all.deb
    sudo apt-get --yes purge libpam-chksshpwd

    # UniFi alternate?
    echo 'deb http://www.ubnt.com/downloads/unifi/debian unifi5 ubiquiti' | sudo tee -a /etc/apt/sources.list.d/ubnt.list > /dev/null
    sudo apt-get --yes install dirmngr
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50
    sudo apt-get --yes install unifi

::

    sudo apt-get update && sudo apt-get --yes install ca-certificates apt-transport-https
    echo 'deb https://www.ui.com/downloads/unifi/debian stable ubiquiti' | sudo tee /etc/apt/sources.list.d/100-ubnt-unifi.list
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50
    sudo apt-get update && sudo apt-get --yes install unifi

    # Sometime later, you'll be nagged with an error that looks like:
    # N: Repository 'https://dl.ubnt.com/unifi/debian stable InRelease' changed its 'Codename' value from 'unifi-5.13' to 'unifi-6.0'
    # ... fix it with the following:
    sudo apt-get update --allow-releaseinfo-change
