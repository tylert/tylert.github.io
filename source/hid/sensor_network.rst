Fan Controller
--------------

* https://digiblur.com/2021/07/08/itead-sonoff-ifan04-l-they-listened
* https://www.amazon.ca/iFAN04-L-Ceiling-Controller-Assistant-Required/dp/B09C21LX9R
* https://templates.blakadder.com/sonoff_iFan04-L.html
* https://sonoff.tech/product-document/diy-smart-switches-doc/ifan04-l-doc
* https://sonoff.tech/product/diy-smart-switches/ifan04-l


Thermostat Stuff
----------------

* https://www.mysensors.org/build/rs485
* https://arduinoinfo.mywikis.net/wiki/RS485-Modules
* https://www.raspberrypi.org/products/raspberry-pi-pico/specifications
* https://www.windmill.co.uk/rs485.html
* https://en.wikipedia.org/wiki/RS-485
* https://buzzert.net/posts/2020-02-10-chipotherm
* https://github.com/gtls64/MontyHome-Hackers-Guide  MontyHome compost sensor
* https://montycompost.co  MontyHome compost sensor


Doorbell/Camera Stuff
---------------------

* https://buzzert.net/posts/2021-05-09-doorbell


Garage Door Stuff
-----------------

* https://github.com/geerlingguy/pico-w-garage-door-sensor
* https://www.hackster.io/news/open-and-close-your-garage-door-with-raspberry-pi-81347881a4cb


Level Stuff
-----------

* https://adonno.com/salt-level-sensor


Light Switches
--------------

* https://www.jamesridgway.co.uk/making-traditional-light-switches-smart


Weather Station Stuff
---------------------

* https://www.instructables.com/DIY-Weather-Station-With-ESP32


Magnetometer
------------

* https://github.com/keepworking/Mecha_QMC5883L
* https://github.com/e-Gizmo/QMC5883L-GY-271-Compass-module


Pi Pico/PicoW
-------------

* https://forums.raspberrypi.com/viewtopic.php?p=2015975#p2015975  BLE on Pico
* https://www.raspberrypi.com/news/getting-to-grips-with-bluetooth-on-pico-w
* https://electrocredible.com/raspberry-pi-pico-serial-uart-micropython
* https://arduino-pico.readthedocs.io
* https://github.com/Noltari/pico-uart-bridge
* http://antirez.com/news/143  playing audio files on a Pico without a DAC
* https://github.com/tinygo-org/tinygo/issues/2947  plain Pico is already supported but PicoW is still pending
* https://github.com/soypat/cyw43439  Bluetooth and TinyGo on a Pico???
* https://circuitpython.org/board/raspberry_pi_pico_w
* https://blog.brixit.nl/moving-to-a-rtos-on-the-rp2040  FreeRTOS et al
* http://cowlark.com/2021-03-10-fuzix-pi-pico
* http://cowlark.com/2021-02-16-fuzix-pi-pico
* https://github.com/kevinmcaleer/pi_to_pico_bluetooth
* https://github.com/mcknly/breadboard-os
* https://www.cnx-software.com/2024/12/26/inky-frame-7-3-7-color-epaper-display-powered-by-a-raspberry-pi-pico-2-w


nRF52840
--------

* https://blog.voltaicsystems.com/solar-powered-lora-radio-barometric-pressure-and-altimeter-tutorial  power cells with 50k charge cycles
* https://tinygo.org/docs/concepts/low-power/#nrf-family
* https://github.com/tinygo-org/bluetooth
* https://tinygo.org/docs/reference/microcontrollers/itsybitsy-nrf52840
* https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/overview
* https://www.adafruit.com/product/4481  part available from Adafruit
* https://www.pishop.ca/product/adafruit-itsybitsy-nrf52840-express-bluetooth-le  part available from PiShop.ca
* https://www.digikey.ca/en/products/detail/adafruit-industries-llc/4481/11497502  part available from Digikey.ca
* https://github.com/orgs/micropython/discussions/13482  MicroPython on ItsyBitsy?
* https://learn.adafruit.com/adafruit-itsybitsy-nrf52840-express/circuitpython-cpu-temp
* https://github.com/tinygo-org/tinygo/issues/2591  DotStar on ItsyBitsy is just a APA102 RGB LED
* https://pkg.go.dev/tinygo.org/x/drivers/apa102

Upgrade ItsyBitsy bootloader to latest::

    # Get latest bootloader files starting with "itsybitsy_nrf52840" from
    # https://github.com/adafruit/Adafruit_nRF52_Bootloader/releases

    # Put the unit in DFU mode and then flash it
    python -m pip install adafruit-nrfutil
    adafruit-nrfutil --verbose dfu serial --package itsybitsy_nrf52840_express_bootloader-foopdidoo.zip -p /dev/ttyACM0 -b 115200 --singlebank --touch 1200

    # Prepare to use tinygo
    pacman -S tinygo avrdude
    tinygo flash -target=itsybitsy-nrf52840 moo.go


Tinygo
------

* https://tinygo.org/docs/tutorials/blinky  blink red LED
* https://github.com/tinygo-org/bluetooth/blob/release/examples/advertisement/main.go  BLE advertisements

::

    go mod init blinky


Electronics
-----------

* https://learn.sparkfun.com/tutorials/voltage-dividers/all
* https://docs.kicad.org/8.0/en/getting_started_in_kicad/getting_started_in_kicad.html  KiCAD getting started
* https://forum.kicad.info/t/configure-global-symbol-footprint-library-table/20264/7  silly KiCAD problem
* https://badar.tech/2023/04/30/electronics-lab-bench-setup-guide
* https://blog.jgc.org/2024/06/two-ways-to-use-led-as-light-sensor.html


Temperature Controller
----------------------

* https://heatmasterss.com/products/mf-eseries  MF 5000e overview
* https://heatmasterss.com/wp-content/uploads/2022/02/MF-Series-Owners-Manual-2018-HM-Update.pdf  MF 5000e manual
* https://www.rancoetc.com/ranco-etc-111000-000-digital-temperature-controller  default controller
* https://www.rancoetc.com/ranco-etc-111100-000-digital-temperature-controller0-10v-output  replacement controller
* https://www.amazon.ca/Ranco-Product-ETC-111100-000/dp/B00EZH3BO6


USB Sniffer
-----------

* https://github.com/ataradov/usb-sniffer-lite  cheap Pi Pico USB sniffer


Tools
-----

* https://www.instructables.com/Reading-Digital-Callipers-with-an-Arduino-USB
* http://www.shumatech.com/support/chinese_scales.htm
* https://github.com/kemsky/arduino-digital-caliper
