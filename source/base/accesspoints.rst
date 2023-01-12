TP-Link EAP245v3
----------------

* https://forum.openwrt.org/t/tp-link-eap245-v3-bad-file-when-attempting-to-flash/89111
* https://forum.openwrt.org/t/adding-openwrt-support-for-tp-link-eap245/57583/10
* https://openwrt.org/toh/tp-link/eap245_v3

::

    # Prepare your machine to talk to the stock UI and OpenWRT
    ip addr add 192.168.0.99/24 broadcast + dev enp0s25
    ip addr add 192.168.1.99/24 broadcast + dev enp0s25

    # Get onto the stock firmware and unblock the wonky signature checking
    ssh booya@192.168.0.254 \
        -oKexAlgorithms=+diffie-hellman-group1-sha1 \
        -oHostKeyAlgorithms=+ssh-dss
    cliclientd stopcs

    # Trick the stock UI into accepting the OpenWRT factory image
    python patch-safeloader.py \
        --factory openwrt-22.03.3-ath79-generic-tplink_eap245-v3-squashfs-factory.bin \
        --input EAP245v3_ca_5.0.5_\[20220323-rel68784\]_up_signed.bin \
        --patch product-info \
        --output factory-ca.bin
