TP-Link EAP245 US v3
--------------------

* https://www.amazon.ca/TP-Link-EAP245-Wireless-Supports-Injector/dp/B07NMZR3F1
* https://lowtek.ca/roo/2022/openwrt-dumb-access-point/
* https://forum.openwrt.org/t/tp-link-eap245-v3-bad-file-when-attempting-to-flash/89111  non-US firmware fix
* https://gist.github.com/svanheule/9f82e156a3601d4a726639eb7400ec97
* https://gist.githubusercontent.com/svanheule/9f82e156a3601d4a726639eb7400ec97/raw/10673b16c5d697e5f6bf8b8292ee6bccf0adfe67/patch-safeloader.py
* https://openwrt.org/toh/tp-link/eap245_v3
* https://openwrt.org/docs/guide-user/network/wifi/dumbap  postprandial setup
* https://forum.openwrt.org/t/adding-openwrt-support-for-tp-link-eap245/57583/10  serial UART info
* https://www.aliexpress.com/item/1005002605013057.html?spm=a2g0o.detail.1000014.1.449211e2prYkfP  DC-DC step-up passive PoE

Full OpenWRT installation instructions from recent vintage stock firmware::

    # Prepare a payload that will work with the stock web UI firmware upload
    wget https://gist.githubusercontent.com/svanheule/9f82e156a3601d4a726639eb7400ec97/raw/10673b16c5d697e5f6bf8b8292ee6bccf0adfe67/patch-safeloader.py
    python patch-safeloader.py \
        --factory openwrt-22.03.3-ath79-generic-tplink_eap245-v3-squashfs-factory.bin \
        --input EAP245v3_ca_5.0.5_\[20220323-rel68784\]_up_signed.bin \
        --patch product-info \
        --output factory-ca.bin

    # Prepare your machine to talk to the stock UI and OpenWRT
    ip addr add 192.168.0.99/24 broadcast + dev enp0s25
    ip addr add 192.168.1.99/24 broadcast + dev enp0s25

    # Access the web UI and allow it to force you create a new user and passwd
    # Enable SSH access for management using the stock web UI

    # Then SSH into the stock firmware and disable the wonky signature checking
    ssh -oHostKeyAlgorithms=+ssh-rsa booya@192.168.0.254

    # On the stock firmware accesspoint, run the following command via SSH
    cliclientd stopcs

    # Finally upload the new, patched firmware via the stock web UI

UART Ramblings::

    On the underside of the board, there's a unpopulated R225 resistor that was
    able to connect to to get 115200 baud 8n1 UART output. I need to bridge solder
    it, but it at least works by holding a jumper wire against it.

    Also got my v3. For reference, the J3 header is >[ TX | RX | GND | 3.3V ]. To
    use TX and RX, you have to bridge (or put in a tiny resistor) on R225 and R237.
    Make sure not to bridge R230 next to R237, or you'll connect RX to ground. R225
    is inside the can on the bottom side of the PCB. Carefully lift the can lid to
    access it.


Basic Accesspoint Setup
~~~~~~~~~~~~~~~~~~~~~~~

Configuration thingies::

    # Main configuration
    System -> System                     :  Set hostname
    System -> Administration             :  Set password
    Network -> Interfaces                :  Interfaces -> LAN -> Edit button
        DHCP Server -> General Setup     :  Ignore interface checked (disable DHCP)
        DHCP Server -> Advanced Settings :  Dynamic DHCP unchecked
        DHCP Server -> IPv6 Settings     :  RA-Service disabled
                                         :  DHCPv6-Service disabled
                                         :  NDP-Proxy disabled
    Network -> Wireless                  :  SSID(s) -> Edit button(s)
                                         :  Enable button, Set ESSID, set encryption
        Advanced Settings                :  Country Code

    # These might be obviated if using DHCP rather than a static IP
    Network -> Interfaces                :  Interfaces -> LAN -> Edit button
        General Settings                 :  IPv4 address, IPv4 gateway (IP of router)
        Advanced Settings                :  Use custom DNS servers (IP of router)

Add stuff to /etc/rc.local (System -> Startup -> Local Startup)::

    for i in dnsmasq firewall odhcpd; do
        if /etc/init.d/"$i" enabled; then
            /etc/init.d/"$i" disable
            /etc/init.d/"$i" stop
        fi
    done

.. image:: all_hostname.png
.. image:: all_password.png
.. image:: wap_interfaces_main.png
.. image:: wap_interfaces_general.png
.. image:: wap_interfaces_advanced.png
.. image:: wap_dhcp_general.png
.. image:: wap_dhcp_advanced.png
.. image:: wap_dhcp_ipv6.png
.. image:: wap_startup.png


Ubiquiti EdgeRouter X
---------------------

* https://www.amazon.ca/Ubiquiti-ER-X-UBIQUITI-Router-Black/dp/B0144R449W
* http://sector5d.org/openwrt-on-the-ubiquiti-edgerouter-x.html
* http://www.makikiweb.com/ipv6/edgerouterx_openwrt.html
* https://www.reddit.com/r/openwrt/comments/x1grtz/proscons_of_openwrt_on_ubiquiti_edgerouter_x/
* https://www.reddit.com/r/openwrt/comments/nejwp6/openwrt_on_edgerouterx_advantage/
* https://openwrt.org/toh/ubiquiti/edgerouter_x_er-x_ka
* https://openwrt.org/inbox/toh/ubiquiti/ubiquiti_edgerouter_x_er-x_ka
* https://openwrt.org/docs/techref/hardware/switch

Steps for replacement of stock firmware::

    # Prepare your machine to talk to the stock UI and OpenWRT
    # Use eth0 if still on stock firmware and eth1 if on OpenWRT
    ip addr add 192.168.1.99/24 broadcast + dev enp0s25

    # Backup any flash partitions you think you might need
    ssh ubnt@192.168.1.1
    sudo su
    mount -o remount,size=240M tmpfs /tmp
    cat /proc/mtd > /tmp/proc_mtd.txt
    dd if=/dev/mtd2ro of=/tmp/dev_mtd2.img
    dd if=/dev/mtd3ro of=/tmp/dev_mtd3.img
    dd if=/dev/mtd4ro of=/tmp/dev_mtd4.img
    dd if=/dev/mtd5ro of=/tmp/dev_mtd5.img
    dd if=/dev/mtd6ro of=/tmp/dev_mtd6.img

    # Get an interim factory image onto the unit and flash it
    scp openwrt-ramips-mt7621-ubnt-erx-initramfs-factory.tar ubnt@192.168.1.1:/tmp
    ssh ubnt@192.168.1.1
    add system image /tmp/openwrt-ramips-mt7621-ubnt-erx-initramfs-factory.tar

    # Upgrade from the older OpenWRT factory image to the newest OpenWRT
    scp -O openwrt-22.03.3-ramips-mt7621-ubnt_edgerouter-x-squashfs-sysupgrade.bin root@192.168.1.1:/tmp
    ssh -oHostKeyAlgorithms=+ssh-rsa root@192.168.1.1
    sysupgrade -F -n /tmp/openwrt-22.03.3-ramips-mt7621-ubnt_edgerouter-x-squashfs-sysupgrade.bin

.. image:: all_hostname.png
.. image:: all_password.png
.. image:: router_interfaces_main.png
.. image:: router_interfaces_general.png
.. image:: sqm_basic_settings.png
.. image:: sqm_queue_discipline.png

QoS setup::

    # Install "sqm-scripts"

    Network -> SQM QoS -> Basic Settings :  Download and upload speeds (in kbit/s)
                                         :    [15000 kbit/s download speed]
                                         :    [1500 kbit/s upload speed]
                                         :  Enable this SQM interface checked