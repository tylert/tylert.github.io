Service Mesh
------------

* https://youtu.be/8T8t4-hQY74
* https://www.youtube.com/watch?v=vh1YtWjfcyk
* https://youtu.be/bEFILWrRJJ4


Python IP Address
-----------------

Find the size of an IPv4 address range::

    import ipaddress

    ip1 = int(ipaddress.IPv4Address('10.1.200.202'))
    ip2 = int(ipaddress.IPv4Address('10.1.200.207'))

    print(ip2 - ip1 + 1)


LANParty Automation
-------------------

* https://github.com/kentonv/lanparty


Magnetometer
------------

* https://github.com/keepworking/Mecha_QMC5883L
* https://github.com/e-Gizmo/QMC5883L-GY-271-Compass-module


EdgeRouter X
------------

* https://kb.intermedia.net/Article/44415


Unifi/PiHole Raspbian
---------------------

* https://gist.github.com/codeniko/381e8be3b0236a602e02f0a9fac13b3d
* https://bobmckay.com/coding-for-kids/running-ubiquiti-unifi-controller-raspberry-pi/
* https://raspberrypi.stackexchange.com/questions/58732/remove-ssh-warning-about-default-password
* https://github.com/pi-hole/pi-hole/#one-step-automated-install

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

    # PiHole
    wget -O basic-install.sh https://install.pi-hole.net
    sudo bash basic-install.sh
