LoRa
----

* https://unsigned.io/rnode_firmware/#supported-hardware
* https://github.com/markqvist/RNode_Firmware
* https://github.com/liberatedsystems/RNode_Firmware_CE  CE = Community Edition
* https://meshtastic.org/docs/hardware/devices/heltec-automation/mesh-node
* https://unsigned.io/guides/2022_03_26_private-messaging-over-lora.html
* https://unsigned.io/guides/2020_05_27_ethernet-and-ip-over-packet-radio-tncs.html
* https://unsigned.io/guides/2018_07_01_using-rnode-as-a-lora-based-wireless-nic.html
* https://unsigned.io/15-kilometre-ssh-link-with-rnode
* https://unsigned.io/tncattach
* https://unsigned.io/using-rnode-as-a-lora-based-wireless-nic
* https://gist.github.com/liamcottle/f42d01570108ec71706fb9c109fc5408
* https://unsigned.io/understanding-lora-parameters  calculate data rate from coding rate, spreading factor, etc.
* https://github.com/markqvist/Reticulum/wiki/Popular-RNode-Settings  anecdotal LoRa settings
* https://reticulum.network/manual/networks.html#interconnected-lora-sites
* https://reticulum.network/hardware.html
* https://github.com/markqvist/Reticulum  also includes rnodeconf utility
* https://github.com/markqvist/tncattach
* https://raw.githubusercontent.com/markqvist/Reticulum/master/docs/Reticulum%20Manual.pdf
* https://chatters.io
* https://awsh.org/rnode
* https://github.com/liamcottle/reticulum-meshchat
* https://gitlab.com/crankylinuxuser/meshtastic_sdr  Tx and Rx for Meshtastic from HackRF
* https://youtube.com/watch?v=aBt56UpaQ0E&list=PLNuF5RFkwVtEjRU0wriiSQWO5B6jMKGi7&index=1  other Reticulum/RNode videos
* https://youtube.com/watch?v=aBt56UpaQ0E  how to get started with Reticulum and RNode
* https://github.com/markqvist/Reticulum/wiki/Awesome-Reticulum
* https://reticulum.betweentheborders.com/guidance.pdf  "Sideband Situation Tracker" search-and-rescue team sensor network?
* https://r8io.github.io/rns-presentations/source/001-introduction.html
* https://www.hackster.io/news/blagojce-bill-kolicoski-hits-a-25-mile-range-with-a-3d-printed-yagi-style-lora-antenna-a9ef96458da2  cute yagi
* https://media.ccc.de/v/38c3-building-your-first-lora-mesh-network-from-scratch
* https://elecrow.com/thinknode-m1-meshtastic-lora-signal-transceiver-powered-by-nrf52840-with-154-screen-support-gps.html


APRS
----

* https://unsigned.io/aprs-over-lora-with-rnode
* https://hamradio.my/2024/09/how-to-turn-a-433-mhz-heltec-wireless-tracker-into-a-433-mhz-lora-aprs-tracker
* https://github.com/richonguzman/LoRa_APRS_Tracker  for some older ESP32 LoRa boards
* https://github.com/richonguzman/LoRa_APRS_iGate  for some older ESP32 LoRa boards


Heltec T114
-----------

* https://heltec.org/project/mesh-node-t114  Heltec T114-V2
* https://aliexpress.com/item/1005008182274183.html  Heltec T114-V2
* https://aliexpress.com/item/1005006359246399.html  915 MHz handheld radio antennas (20cm and 40cm versions)
* https://github.com/meshtastic/firmware/issues/4723#issuecomment-2369336696  Heltec T114-V1 hardware bug description
* https://zerofox3d.com/products/flexo-hardware-kit?variant=53497579471223  custom switch PCB?
* https://zerofox3d.com/products/bender-heltec-v3-battery-case-hardware-kit  custom battery holder?
* https://github.com/arduino/arduino-cli/issues/1538  some Arduino horribleness
* https://forum.arduino.cc/t/why-are-there-four-config-directories-for-the-arduino-ide-under-linux/1237624  some more Arduino horribleness

Build firmware for RNodes::

    # Install some other needed tools
    # arduino-cli
    # make

    # Prepare Python stuff
    python -m pip install --break-ssytem-packages adafruit-nrfutil  # for flashing firmware
    python -m pip install --break-ssytem-packages rns               # for rnodeconf and rn* utils

    # ERROR: Can not perform a '--user' install. User site-packages are not visible in this virtualenv.
    # patch ./Makefile (remove all occurences of "--user")
    make prep-nrf

    # Error during build: fork/exec python /home/bubba/.arduino15/packages/Heltec_nRF52/hardware/Heltec_nRF52/1.7.0/tools/uf2conv/uf2conv.py: no such file or directory
    # patch ~/.arduino15/packages/Heltec_nRF52/hardware/Heltec_nRF52/1.7.0/platform.txt (fix quotes on line with "uf2conv")
    # patch ~/.arduino15/packages/Heltec_nRF52/hardware/Heltec_nRF52/1.7.0/tools/platform.txt (fix quotes on line with "uf2conv")
    make firmware-heltec_t114_gps
    make upload-heltec_t114

More firmware stuff for RNodes::

    # If this is your first time running this here
    rnodeconf --key

    rnodeconf --autoinstall

Flash an official firmware zip fetched from GitHub::

    adafruit-nrfutil dfu serial --package rnode_firmware_1.82_heltec_t114.zip --port /dev/ttyACM0 --baudrate 115200 --touch 1200
    rnodeconf /dev/ttyACM0 --firmware-hash $(./partition_hashes from_device /dev/ttyACM0)

Other fun over RNodes::

    # host A
    rnodeconf /dev/ttyACM0 \
        --freq 915000000 \  # frequency in Hz (902000000 to 928000000)
        --bw 125000      \  # bandwidth in Hz
        --txp 22         \  # Tx power in dBm (max 22)
        --sf 8           \  # spreading factor (6 to 12)
        --cr 6           \  # coding rate (5 to 8)
        --tnc               # TNC mode
    sudo tncattach /dev/ttyACM0 115200 \
        --ipv4 10.0.0.1/24 \
        --daemon   \
        --ethernet \
        --mtu 478  \  # 500 - 22 bytes Ethernet + VLANs (default 392)
        --noipv6

    # host B
    rnodeconf /dev/ttyACM0 \
        --freq 915000000 \  # frequency in Hz (902000000 to 928000000)
        --bw 125000      \  # bandwidth in Hz
        --txp 22         \  # Tx power in dBm (max 22)
        --sf 8           \  # spreading factor (6 to 12)
        --cr 6           \  # coding rate (5 to 8)
        --tnc               # TNC mode
    sudo tncattach /dev/ttyACM0 115200 \
        --ipv4 10.0.0.2/24 \
        --daemon   \
        --ethernet \
        --mtu 478  \  # 500 - 22 bytes Ethernet + VLANs (default 392)
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


Transport RNodes
----------------

* https://unsigned.io/articles/2022_01_27_rnode-with-anything.html
* https://unsigned.io/rnode_bootstrap_console/guides/make_rnodes.html
* https://git.liberatedsystems.co.uk/jacob.eva/opencom_xl_firmware
* https://store.liberatedsystems.co.uk/product/wisblock-sx1280-module  Semtech SX1280 2.4-2.5 GHz @ up to 0.5 W (27 dBm max) and 200 kbps
* https://cnx-software.com/2022/08/30/esp32-board-supports-2-4ghz-lora-with-sx1280-rf-transceiver
* https://lilygo.cc/products/t3s3-v1-0  Semtech SX1280 with ESP32-S3 (12 dBm max)
* https://duckduckgo.com/?q=2.4+GHz+grid+antenna&t=ffab&iar=images&iax=images&ia=images  2.4 GHz grid antenna images
* https://meezenest.nl/mees-elektronica/projects/reticulum_design_my_own_rnode/index.html  RNode from scratch overview
* https://reddit.com/r/meshtastic/comments/1fekv0v/gorse_solar_node_using_t114  solar charging for Heltec T114-V2
* https://youtube.com/watch?v=FcQzAxWBN7A  solar charging for Heltec T114-V2
* https://github.com/heyitsyang/W9ETC-Meshtastic-Solar-Node  MPPT modules?
* https://uart.cz/en/2534/solar-mppt-charger-for-meshtastic  LoRa module, CN3795 MPPT charging chip, boost converter on custom board
* https://lectronz.com/products/solar-mppt-charger-for-meshtastic  KiCAD design files for the PCB
* https://lectronz.com/products/fully-assembled-meshtastic-solar-node-station  another all-in-one solution
* https://youtube.com/watch?v=T1itQcdf5cc  nRF52840 RNode, Pi Zero RNS, WiFi hotspot
* https://loramesh.org  loads more Reticulum/RNode info and solar installs


Reticulum
---------

* https://hub.federated.channel/channel/reticulum  news and updates for Reticulum
* https://hub.federated.channel/channel/reticulum?mid=5f06882f-ddbe-4cf0-ab9c-bac79f9172ff  Rphones
* https://github.com/markqvist/Reticulum/discussions/702  some newbie thoughts about Reticulum
* https://github.com/markqvist/Reticulum/discussions/399  encryption
* https://github.com/markqvist/Reticulum/discussions/84  encryption
* https://github.com/markqvist/Reticulum/discussions/70  encryption
* https://github.com/markqvist/Reticulum/discussions/261  more HF
* https://github.com/RFnexus/reticulum-over-hf
* https://simplyequipped.github.io/fskmodem/fskmodem.html
* https://github.com/simplyequipped/fskmodem
* https://github.com/simplyequipped/tcpkissserver
* http://www.whence.com/minimodem
* https://github.com/markqvist/Reticulum/discussions/192  basic setup for propagation node
* https://github.com/markqvist/Reticulum/discussions/57  how to run a propagation or router node
* https://meezenest.nl/mees/projects/reticulum_field_server/build_doc/index.html  portable reticulum server
* https://meezenest.nl/mees/projects/reticulum_field_server/build_doc/reticulum_portable_server.pdf  PDF of same
* https://reticulum.betweentheborders.com/primer.pdf  IMS/ICS and off-grid planning for Reticulum
* https://piratebox.info/reticulum/understanding.html
* https://reticulum.network/connect.html  public testnets
* https://github.com/attermann/microReticulum_Firmware  supports RAK4631 nRF52840 boards?
* https://reticulum.n7ekb.net  some notes about running your own networks
* https://ikiwiki.laglab.org/_Reticulum  more notes about getting started as a group
* https://reticulum.network/connect.html  other test nets
* https://technopolis.tv/blog/2023/05/22/TNC-IP-over-LoRa
* https://github.com/resiliencetheatre/rpi4edgemap  Reticulum and Meshtastic on same map?
* https://resilience-theatre.com/edgemap
* https://resilience-theatre.com/wiki/doku.php?id=start
* https://github.com/jooray/lxmf-message  CLI for sending messages to a destination
* https://github.com/randogoth/lxmf-bot

LXMF config for a server::

    [propagation]
    enable_node = yes
    [lxmf]
    display_name = Whoopdidoo

Reticulum config for a server::

    [reticulum]
    enable_transport = yes
    respond_to_probes = yes
    [interfaces]
      [[Default Interface]]
        type = AutoInterface
        enabled = yes
      [[Whoopdidoo]]
        type = TCPServerInterface
        enabled = yes
        listen_ip = 0.0.0.0
        listen_port = 4242
        mode = gateway

Reticulum config for a client::

    [reticulum]
    enable_transport = no
    [interfaces]
      [[Default Interface]]
        type = AutoInterface
        enabled = yes
      [[Whoopdidoo]]
        type = TCPClientInterface
        enabled = yes
        target_host = <EXT_IP_OR_HOSTNAME_OF_RNS_SERVER>
        target_port = 4242
      [[RNode]]
        type = RNodeInterface
        enabled = yes
        port = /dev/ttyACM0  # port = ble://
        frequency = 915000000
        bandwidth = 125000
        txpower = 22
        spreadingfactor = 8
        codingrate = 6

rnsd.service::

    [Unit]
    Description=Reticulum Network Stack Daemon
    After=multi-user.target

    [Service]
    # If you run Reticulum on WiFi devices,
    # or other devices that need some extra
    # time to initialise, you might want to
    # add a short delay before Reticulum is
    # started by systemd:
    # ExecStartPre=/bin/sleep 10
    Type=simple
    Restart=always
    RestartSec=3
    User=${USER}
    ExecStart=rnsd --service

    [Install]
    WantedBy=multi-user.target

lxmd.service::

    [Unit]
    Description=Lightweight eXtensible Messaging Daemon
    After=multi-user.target

    [Service]
    # ExecStartPre=/bin/sleep 10
    Type=simple
    Restart=always
    RestartSec=3
    User=${USER}
    ExecStart=lxmd --service

    [Install]
    WantedBy=multi-user.target


Meshtastic
----------

* https://treerocket.bearblog.dev/reticulum-vs-meshtastic-why-i-chose-reticulum
* https://blog.erethon.com/blog/2024/01/31/comparing-reticulum-and-meshtastic
* https://github.com/markqvist/Reticulum/discussions/77
* https://linuxinabit.codeberg.page/blog/reticulum  loads of useful links
* https://github.com/landandair/RNS_Over_Meshtastic


DMR
---

* https://farnsworth.org/dale/codeplug/editcp  better CPS
* https://github.com/dalefarnsworth-dmr  better CPS
* https://www.retevis.com/Download/brochure/RT3S-brochure.pdf  RT3S brochure
* https://www.retevis.com/resources_center/mannual/RT3S-English-Manual.pdf  RT3S manual
* https://www.passion-radio.com/index.php?controller=attachment&id_attachment=204  RT3 manual in French
* https://www.retevis.com/resources_center/mannual/RT3_manual_del_usuario_en_espanol.pdf  RT3 manual in Spanish
* https://www.retevis.com/resources_center/software/RT3S_updated_FirmwareV3.04.zip  official firmware
* https://www.retevis.com/resources_center/software/RT3S_GPS_SoftwareV1.2.zip  official CPS
* https://www.retevis.com/resources_center/software/RT3&RT8_USBDriver.zip  official USB driver
* https://youtube.com/watch?v=Lw0Y-jQZMZ0  DMR features and overview
* https://www.jeffreykopcak.com/2017/06/11/dmr-in-amateur-radio-programming-a-code-plug  DMR programming
* https://youtube.com/watch?v=VExx628R0DM  DMR programming
* https://youtube.com/watch?v=ip3a37G68JA  DMR programming in French
* https://www.taitradioacademy.com/topic/benefits-of-dmr-1
* https://www.jpole-antenna.com/2018/07/13/retevis-rt3s-dual-band-dmr-handheld-transceiver-review
* https://m6ceb.com/reviews/retevis-rt3s-dmr-fm-dual-band-handheld-radio
* https://blog.retevis.com/index.php/hd1-promiscuous-mode-and-rt3s-group-call-match-introduction
* https://www.ailunce.com/blog/How-to-Upgrade-Retevis-RT3S-Firmware
* https://www.ailunce.com/blog/How-to-import-Digital-Contacts-into-RT3S
* https://radioid.net
* https://blog.retevis.com/index.php/how-to-set-rt3s-aprs
* http://www.tothewoods.net/Comms-mounting-baofeng-uv-5r-ham-radio-in-Jeep-Wrangler-TJ.php
* https://thingiverse.com/thing:2252779  RT3S cradle
* https://thingiverse.com/thing:267879  clone RAM arm
* https://thingiverse.com/thing:1323115  clone RAM base
* https://youtube.com/watch?v=wsPt91xVEKE  MMDVM build
* https://youtube.com/watch?v=gVlXYLTD_DI  MMDVM build
* https://youtube.com/watch?v=DNQgZx92Gj0  MMDVM build


M17
---

* https://github.com/M17-Project/Module_17
* https://github.com/M17-Project/wiki/blob/main/wiki/radio_compatibility.md
* https://github.com/M17-Project/wiki/blob/main/wiki/gm300.md  M17 VHF mobiles


Repeaters
---------

* https://digikey.ca/en/products/detail/te-connectivity-amp-connectors/104422-2/550725  20-pin connector housing
* https://digikey.ca/en/products/detail/te-connectivity-amp-connectors/104422-1/289312  16-pin connector housing
* https://digikey.ca/en/products/detail/te-connectivity-amp-connectors/1-87309-3/29826  16-pin pins
* https://www.itead.cc/nextion-nx4832k035.html  3.5 Nextion display
* https://amazon.ca/M-D-Building-Products-84327-020-Inch/dp/B007NG6EQI  holey metal
* https://rtl-sdr.com/a-tutorial-on-using-sdrangel-for-dmr-d-star-and-fusion-reception-with-an-rtl-sdr
* https://n5amd.com/digital-radio-how-tos/tune-mmdvm-repeater-sdr-low-ber


Pagers
------

* https://hackster.io/news/alley-cat-s-alley-chat-pocket-ht-brings-back-the-pager-with-lora-and-meshtastic-technology-edb388e66c8f
* https://archive.fosdem.org/2024/schedule/event/fosdem-2024-1721-dapnet-bringing-pagers-back-to-the-21st-century
* https://reddit.com/r/hackrf/comments/ls3a3c/portapack_pocsac_pager_guide


HackRF and PortaPack
--------------------

* https://greatscottgadgets.com/2021/12-07-testing-a-hackrf-clone
* https://rtl-sdr.com/tech-minds-a-beginners-guide-to-the-hackrf-and-portapack-with-mayhem-firmware
* https://opensourcesdrlab.com/products/h4m-receiver-and-spectrum-analyzer?VariantsId=10002
* https://opensourcesdrlab.com/products/mayhem-signature-edition-h4m-portapack-and-transparent-shell-with-speaker-and-2500-mah-lithium-battery
* https://opensourcesdrlab.com/products/r10c-hrf-sdr-software-defined-1mhz-to-6ghz-mainboard-development-board-kit
* https://printables.com/model/1033734-hackrf-portapack-h4m-stand  desk stand for H4M
* https://printables.com/model/1096252-hackrf-portapack-h4m-rotary-encoder-dial-upgrade  grippier scrolly thing for H4M
* https://printables.com/model/784000-threaded-sma-connector-knurled-caps-fpv-drones-hac  SMA covers
* https://ppsplash.creativo.hu  PortaPack splash screens
* https://github.com/htotoo/PPSplash
* https://github.com/llopisdon/skies-adsb  3D ADS-B visualizer in web browser
* https://nooelec.com/store/opera-cake.html  HackRF antenna switcher?
* https://github.com/portapack-mayhem/mayhem-firmware/wiki/Add-GPIO-to-H2
* https://github.com/portapack-mayhem/mayhem-firmware/wiki/USB%E2%80%90C-charging-modification-for-older-HackRF-boards  second charge port?
* https://blog.videah.net/attacking-my-landlords-boiler
* https://github.com/lraton/FlopperZiro


Shortwave Receivers
-------------------

* https://swling.com/blog/2018/09/guest-post-supercharging-the-xhdata-d-808-with-a-7-5-loopstick
* https://swling.com/blog/2021/10/gary-debocks-xhdata-d-808-loopstick-model
* https://swling.com/blog/2021/05/gary-debocks-2021-ultralight-radio-shootout
* https://amazon.ca/Tecsun-Digital-PL330-Worldband-Receiver/dp/B0921HN6QM  Tecsun PL-330
* https://amazon.ca/XHDATA-Portable-Speaker-Display-External/dp/B0DCFZYMHY  XHDATA D-808
* https://swling.com/blog/2020/09/tecsun-pl-330-initial-impressions-overview-of-functions-and-operation
* https://swling.com/blog/tag/xhdata-d-808-review
* https://blogordie.com/2023/05/pl-330-or-d-808
* https://blogordie.com/2023/03/my-favorite-shortwave-radio


Other
-----

* https://github.com/wb2osz/direwolf/tree/master/doc  docs for setting up DireWolf for various fun things
* https://ad6dm.net/log/2024/04/vara-fm-packet-dual-mode-winlink-gateway-in-linux  ugh, Wine
* https://github.com/km4ack/73Linux  pre-canned ham apps for to install on Linux
* https://www.scc-ares-races.org/gokit/SCCo_Go_Kit_rev20240326.pdf  2-hour kits, 12-hour kits, etc.
* https://direbox.net


Power
-----

* https://blog.k7jlx.io/2021/08/21/100ah-battery-box-build
* https://www.skywide.ca/portable-battery-box
* https://xplrcreate.com/2020/04/09/diy-camping-power-station-battery-pack
* https://www.cloudynights.com/topic/842615-diy-power-tank-with-a-12v-100ah-lifepo4-battery-story-pros-cons-and-equipment
* https://www.ke7hlr.com/ecw/personal_go-kit_2011.pdf  page 25
* https://lyonscomputer.com.au/PV-Solar-Generator-Systems/SolarKing-100Ah-Battery-Rebuild/SolarKing-100Ah-Battery-Rebuild.html  test setup?
* https://zeroping.github.io/PowerPoleDist
