LoRa
----

* https://heltec.org/project/mesh-node-t114  Heltec T114-V2
* https://www.aliexpress.com/item/1005008182274183.html  Heltec T114-V2
* https://github.com/meshtastic/firmware/issues/4723#issuecomment-2369336696  Heltec T114-V1 hardware bug description
* https://www.reddit.com/r/meshtastic/comments/1fekv0v/gorse_solar_node_using_t114  solar charging for Heltec T114-V2
* https://www.youtube.com/watch?v=FcQzAxWBN7A  solar charging for Heltec T114-V2
* https://unsigned.io/rnode_firmware/#supported-hardware
* https://github.com/markqvist/RNode_Firmware/releases/tag/1.81
* https://github.com/markqvist/RNode_Firmware
* https://github.com/liberatedsystems/RNode_Firmware_CE  CE = Community Edition
* https://meshtastic.org/docs/hardware/devices/heltec-automation/mesh-node
* https://unsigned.io/guides/2022_03_26_private-messaging-over-lora.html
* https://unsigned.io/guides/2020_05_27_ethernet-and-ip-over-packet-radio-tncs.html
* https://unsigned.io/15-kilometre-ssh-link-with-rnode
* https://unsigned.io/aprs-over-lora-with-rnode
* https://unsigned.io/understanding-lora-parameters  calculate data rate from coding rate, spreading factor, etc.
* https://reticulum.network/manual/networks.html#interconnected-lora-sites
* https://reticulum.network/hardware.html
* https://github.com/markqvist/Reticulum
* https://github.com/markqvist/Reticulum/releases  rnodeconf.py utility
* https://github.com/markqvist/tncattach
* https://raw.githubusercontent.com/markqvist/Reticulum/master/docs/Reticulum%20Manual.pdf
* https://www.chatters.io
* https://awsh.org/rnode
* https://github.com/liamcottle/reticulum-meshchat
* https://git.liberatedsystems.co.uk/jacob.eva/opencom_xl_firmware
* https://store.liberatedsystems.co.uk/product/wisblock-sx1280-module  Semtech SX1280 2.4-2.5 GHz @ up to 0.5 W and 200 kbps
* https://www.cnx-software.com/2022/08/30/esp32-board-supports-2-4ghz-lora-with-sx1280-rf-transceiver
* https://lilygo.cc/products/t3s3-v1-0  Semtech SX1280 with ESP32-S3
* https://duckduckgo.com/?q=2.4+GHz+grid+antenna&t=ffab&iar=images&iax=images&ia=images  2.4 GHz grid antenna images
* https://gitlab.com/crankylinuxuser/meshtastic_sdr  Tx and Rx for Meshtastic from HackRF

::

    pip install adafruit-nrfutil  # for flashing firmware
    pip install rns               # for rnodeconf and rns* utils
    pip install nomadnet          # a chat thingy
    pip install sbapp             # another chat thingy

::

    # host A (10.0.0.1)
    rnodeconf /dev/ttyUSB0 \
        --freq 915000000 \  # frequency in Hz
        --bw 125000      \  # bandwidth in Hz
        --txp 22         \  # Tx power in dBm (max 22)
        --sf 7           \  # spreading factor (7 to 12)
        --cr 5           \  # coding rate (5 to 8)
        --tnc               # TNC mode
    sudo tncattach /dev/ttyUSB0 115200 \
        --daemon   \
        --ethernet \
        --ipv4 10.0.0.1/24
        --mtu 478  \  # RNode can handle 500 - 22 bytes for Ethernet with VLAN tags (default 392)
        --noipv6

    # host B (10.0.0.2)
    rnodeconf /dev/ttyUSB0 \
        --freq 915000000 \  # frequency in Hz
        --bw 125000      \  # bandwidth in Hz
        --txp 22         \  # Tx power in dBm (max 22)
        --sf 7           \  # spreading factor (7 to 12)
        --cr 5           \  # coding rate (5 to 8)
        --tnc               # TNC mode
    sudo tncattach /dev/ttyUSB0 115200 \
        --daemon   \
        --ethernet \
        --ipv4 10.0.0.2/24
        --mtu 478  \  # RNode can handle 500 - 22 bytes for Ethernet with VLAN tags (default 392)
        --noipv6

Raw bytes sent by rnodeconf::

    freq => \xc0,\x01,....,\xc0  (4 bytes)
    bw   => \xc0,\x02,....,\xc0  (4 bytes)
    txp  => \xc0,\x03,....,\xc0  (1 byte, values ranging from \x01 to \x16)
    sf   => \xc0,\x04,....,\xc0  (1 byte, values ranging from \x07 to \x0c)
    cr   => \xc0,\x05,....,\xc0  (1 byte, values ranging from \x05 to \x08)
    tnc  => \xc0,\x53,\x00,\xc0

* https://github.com/markqvist/Reticulum/blob/master/RNS/Utilities/rnodeconf.py
* https://github.com/bugst/go-serial
* https://pkg.go.dev/go.bug.st/serial


DMR
---

* https://www.farnsworth.org/dale/codeplug/editcp  better CPS
* https://github.com/dalefarnsworth-dmr  better CPS
* https://www.retevis.com/Download/brochure/RT3S-brochure.pdf  RT3S brochure
* https://www.retevis.com/resources_center/mannual/RT3S-English-Manual.pdf  RT3S manual
* https://www.passion-radio.com/index.php?controller=attachment&id_attachment=204  RT3 manual in French
* https://www.retevis.com/resources_center/mannual/RT3_manual_del_usuario_en_espanol.pdf  RT3 manual in Spanish
* https://www.retevis.com/resources_center/software/RT3S_updated_FirmwareV3.04.zip  official firmware
* https://www.retevis.com/resources_center/software/RT3S_GPS_SoftwareV1.2.zip  official CPS
* https://www.retevis.com/resources_center/software/RT3&RT8_USBDriver.zip  official USB driver
* https://www.youtube.com/watch?v=Lw0Y-jQZMZ0  DMR features and overview
* https://www.jeffreykopcak.com/2017/06/11/dmr-in-amateur-radio-programming-a-code-plug  DMR programming
* https://www.youtube.com/watch?v=VExx628R0DM  DMR programming
* https://www.youtube.com/watch?v=ip3a37G68JA  DMR programming in French
* https://www.taitradioacademy.com/topic/benefits-of-dmr-1
* https://www.jpole-antenna.com/2018/07/13/retevis-rt3s-dual-band-dmr-handheld-transceiver-review
* https://m6ceb.com/reviews/retevis-rt3s-dmr-fm-dual-band-handheld-radio
* https://blog.retevis.com/index.php/hd1-promiscuous-mode-and-rt3s-group-call-match-introduction
* https://www.ailunce.com/blog/How-to-Upgrade-Retevis-RT3S-Firmware
* https://www.ailunce.com/blog/How-to-import-Digital-Contacts-into-RT3S
* https://radioid.net
* https://blog.retevis.com/index.php/how-to-set-rt3s-aprs
* http://www.tothewoods.net/Comms-mounting-baofeng-uv-5r-ham-radio-in-Jeep-Wrangler-TJ.php
* https://www.thingiverse.com/thing:2252779  RT3S cradle
* https://www.thingiverse.com/thing:267879  clone RAM arm
* https://www.thingiverse.com/thing:1323115  clone RAM base
* https://www.youtube.com/watch?v=wsPt91xVEKE  MMDVM build
* https://www.youtube.com/watch?v=gVlXYLTD_DI  MMDVM build
* https://www.youtube.com/watch?v=DNQgZx92Gj0  MMDVM build


Repeaters
---------

* https://www.digikey.ca/en/products/detail/te-connectivity-amp-connectors/104422-2/550725  20-pin connector housing
* https://www.digikey.ca/en/products/detail/te-connectivity-amp-connectors/104422-1/289312  16-pin connector housing
* https://www.digikey.ca/en/products/detail/te-connectivity-amp-connectors/1-87309-3/29826  16-pin pins
* https://www.itead.cc/nextion-nx4832k035.html  3.5 Nextion display
* https://www.amazon.ca/M-D-Building-Products-84327-020-Inch/dp/B007NG6EQI  holey metal
* https://www.rtl-sdr.com/a-tutorial-on-using-sdrangel-for-dmr-d-star-and-fusion-reception-with-an-rtl-sdr
* https://n5amd.com/digital-radio-how-tos/tune-mmdvm-repeater-sdr-low-ber


Pagers
------

* https://www.hackster.io/news/alley-cat-s-alley-chat-pocket-ht-brings-back-the-pager-with-lora-and-meshtastic-technology-edb388e66c8f
* https://archive.fosdem.org/2024/schedule/event/fosdem-2024-1721-dapnet-bringing-pagers-back-to-the-21st-century
* https://www.reddit.com/r/hackrf/comments/ls3a3c/portapack_pocsac_pager_guide


HackRF and PortaPack
--------------------

* https://greatscottgadgets.com/2021/12-07-testing-a-hackrf-clone
* https://www.rtl-sdr.com/tech-minds-a-beginners-guide-to-the-hackrf-and-portapack-with-mayhem-firmware
* https://opensourcesdrlab.com/products/h4m-receiver-and-spectrum-analyzer?VariantsId=10002
* https://opensourcesdrlab.com/products/mayhem-signature-edition-h4m-portapack-and-transparent-shell-with-speaker-and-2500-mah-lithium-battery
* https://opensourcesdrlab.com/products/r10c-hrf-sdr-software-defined-1mhz-to-6ghz-mainboard-development-board-kit
* https://www.printables.com/model/1033734-hackrf-portapack-h4m-stand  desk stand for H4M
* https://www.printables.com/model/1096252-hackrf-portapack-h4m-rotary-encoder-dial-upgrade  grippier scrolly thing for H4M
* https://www.printables.com/model/784000-threaded-sma-connector-knurled-caps-fpv-drones-hac  SMA covers
* https://ppsplash.creativo.hu  PortaPack splash screens
* https://github.com/htotoo/PPSplash
* https://github.com/llopisdon/skies-adsb  3D ADS-B visualizer in web browser
* https://www.nooelec.com/store/opera-cake.html  HackRF antenna switcher?
* https://github.com/portapack-mayhem/mayhem-firmware/wiki/Add-GPIO-to-H2
* https://github.com/portapack-mayhem/mayhem-firmware/wiki/USB%E2%80%90C-charging-modification-for-older-HackRF-boards  second charge port?


Shortwave Receivers
-------------------

* https://swling.com/blog/2018/09/guest-post-supercharging-the-xhdata-d-808-with-a-7-5-loopstick
* https://swling.com/blog/2021/10/gary-debocks-xhdata-d-808-loopstick-model
* https://swling.com/blog/2021/05/gary-debocks-2021-ultralight-radio-shootout
* https://www.amazon.ca/Tecsun-Digital-PL330-Worldband-Receiver/dp/B0921HN6QM  Tecsun PL-330
* https://www.amazon.ca/XHDATA-Portable-Speaker-Display-External/dp/B0DCFZYMHY  Xhdata D-808
* https://swling.com/blog/2020/09/tecsun-pl-330-initial-impressions-overview-of-functions-and-operation
* https://swling.com/blog/tag/xhdata-d-808-review
* https://www.blogordie.com/2023/05/pl-330-or-d-808
* https://www.blogordie.com/2023/03/my-favorite-shortwave-radio
