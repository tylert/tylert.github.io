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


PiHole Raspbian
---------------

* https://raspberrypi.stackexchange.com/questions/58732/remove-ssh-warning-about-default-password
* https://github.com/pi-hole/pi-hole/#one-step-automated-install

::

    # PiHole
    wget -O basic-install.sh https://install.pi-hole.net
    sudo bash basic-install.sh
