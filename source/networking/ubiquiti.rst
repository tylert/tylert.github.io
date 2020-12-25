Rebuilding EdgeRouter
---------------------

1. Boot router with "factory defaults" (refer to "quick start guide").
1. Login to the web UI with "ubnt:ubnt".
1. Make sure the firmware is up-to-date.
1. Decline to send data to Ubiquiti and do not start any wizards.
1. Disable "UNMS Connection (beta)" and "UBNT Discovery" and click save.
1. Set the hostname and click save.
1. Enable "Traffic Analysis".
1. Turn on "Smart Queue" QoS:  Policy name 'lte', WAN interface "eth0", set upload and download rates
1. Login via SSH and install wireguard-vyatta-ubnt.  STOP HERE IF PREPPING A SPARE ROUTER.
1. Use the "Basic Setup" wizard (set LAN port address and new password).
1. Boot router "normally" and put it into full service.
1. Login to the web UI with new username/password.
1. Switch to using dnsmasq for DHCP.
1. Reboot.

* https://github.com/WireGuard/wireguard-vyatta-ubnt


Configuring EdgeRouter Properly
-------------------------------

* https://kb.intermedia.net/Article/44415
* https://ragingtiger.github.io/2018/04/29/ubq-erx-router-setup/
* https://help.ui.com/hc/en-us/articles/115002673188-EdgeRouter-DHCP-Server-using-Dnsmasq
* https://loganmarchione.com/2016/08/edgerouter-lite-dnsmasq-setup/

::

    configure
    set service dhcp-server use-dnsmasq enable
    commit
    save
    exit


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
