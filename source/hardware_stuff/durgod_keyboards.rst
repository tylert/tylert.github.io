Durgod Taurus K320/K310 Non-Backlit Keyboards
=============================================

Some very nice, economical mechanical keyboards with Cherry MX switches (Blue,
Brown, Black) that can run the 100% open-source QMK keyboard firmware.


Product Pages
-------------

* https://www.durgod.com/page9?_l=en&product_id=47
* https://www.durgod.com/page9?_l=en&product_id=53


Reviews
-------

* https://www.techpowerup.com/review/durgod-taurus-320-tkl-keyboard/
* https://aphnetworks.com/index.php/reviews/durgod-taurus-k320
* https://switchandclick.com/2020/11/02/durgod-k320-review/
* https://tlrtechnology.com/2019/07/09/durgod-taurus-k320-tkl-review-can-it-really-be-this-good/
* https://www.reddit.com/r/MechanicalKeyboards/comments/7t70fr/review_durgod_taurus_k320_tenkeyless_keyboard/
* https://www.rtings.com/keyboard/reviews/durgod/taurus-k320
* https://www.youtube.com/watch?v=17rISRgJO1o
* https://www.youtube.com/watch?v=D_S30mEkggQ
* https://www.youtube.com/watch?v=dSXrde3sJpc
* https://www.youtube.com/watch?v=JDkkMzMGIm0


Where To Buy
------------

* https://www.aliexpress.com/item/32845509908.html?spm=a2g0o.productlist.0.0.4d8c6c1ab0jr7z&algo_pvid=b0551f21-6d17-4af2-a7f5-47d9c4db5aba&algo_expid=b0551f21-6d17-4af2-a7f5-47d9c4db5aba-0&btsid=0bb0622916113003247497560e2fdf&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_
* https://www.aliexpress.com/item/32852709021.html?spm=a2g0o.productlist.0.0.9e8769bbcJn9gR&algo_pvid=e2fc67ec-4b3a-41b0-85d6-085266f92d3a&algo_expid=e2fc67ec-4b3a-41b0-85d6-085266f92d3a-0&btsid=0b0a555b16113003437397344e4d82&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_
* https://kprepublic.com/products/durgod-87-taurus-k320-mechanical-keyboard-using-cherry-mx-switches-pbt-doubleshot-keycaps-brown-blue-black-red-silver-switch?_pos=4&_sid=bda219a06&_ss=r
* https://kprepublic.com/products/durgod-104-taurus-k310-mechanical-keyboard-using-cherry-mx-switches-pbt-doubleshot-keycaps-brown-blue-black-red-silver-switch?_pos=3&_sid=bda219a06&_ss=r
* https://www.amazon.ca/DURGOD-Mechanical-Keyboard-Switches-Interface/dp/B078H3WPHM
* https://www.amazon.ca/Durgod-Taurus-K310-Mechanical-Keyboard/dp/B07V1SQYB8
* https://www.durgodkeyboard.com/product/durgod-87-taurus-k320-mechanical-keyboard-using-cherry-mx-switches-pbt-doubleshot-keycaps-brown-blue-black-red-silver-switch/
* https://www.durgodkeyboard.com/product/durgod-104-taurus-k310-mechanical-keyboard-using-cherry-mx-switches-pbt-doubleshot-keycaps-brown-blue-black-red-silver-switch/


Disassembly
-----------

You must open the keyboard once to boot the keyboard into "DFU mode" for
initial flashing of QMK.  Once QMK is installed on the keyboard, you may boot
it into "DFU mode" whenever you like by holding down the "ESC" key while
plugging-in the keyboard (at power up).

Follow this video to open the keyboard but use a dozen or so guitar picks
instead of a nasty metal screwdriver.

* https://www.youtube.com/watch?v=H-HN3f20aLI
* https://duckduckgo.com/?t=ffab&q=guitar+pick+punch&iax=images&ia=images


Weird Button Inside
~~~~~~~~~~~~~~~~~~~

There is a weird button inside but nobody seems sure of what it does yet.

* https://www.techpowerup.com/review/durgod-taurus-320-tkl-keyboard/4.html
* https://www.reddit.com/r/MechanicalKeyboards/comments/bvmlfi/bricked_my_durgod_k320_taurus_after_firmware/


Force DFU Boot
~~~~~~~~~~~~~~

XXX TODO  See if the K310 can use the same DFU trick.
Short R21 to C27 (Boot0 to VDD) and apply power (plug the keyboard in).

.. image:: boot0.png


QMK Firmware
------------

QMK 0.11.54 or newer includes the K320.
K310 porting work hasn't been started yet.

* https://github.com/the-via/keyboards/pull/588  for K320 VIA support
* https://github.com/qmk/qmk_firmware/pull/11960  for K320 VIA support
* https://github.com/qmk/qmk_configurator/pull/887  for K320 QMK configurator support
* https://github.com/qmk/qmk_firmware/pull/11399  for K320 full-support
* https://github.com/qmk/qmk_firmware/pull/9901  for K320 initial draft work (NOT MERGED)
* https://github.com/qmk/qmk_firmware/issues/2179  for Apple Fn key magic (NOT MERGED)
* https://www.reddit.com/r/MechanicalKeyboards/comments/i0pfwv/first_qmk_powered_durgod_k320/
* https://coreysalzano.com/how-to/customizing-a-durgod-keyboard-for-macos/


Flashing New Firmware
---------------------

Confirm the keyboard is in DFU mode and find out what's inside the box::

    $ dfu-util --list
    dfu-util 0.9

    Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
    Copyright 2010-2016 Tormod Volden and Stefan Schmidt
    This program is Free Software and has ABSOLUTELY NO WARRANTY
    Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

    Found DFU: [0483:df11] ver=2200, devnum=61, cfg=1, intf=0, path="1-4", alt=1, name="@Option Bytes  /0x1FFFF800/01*016 e", serial="FFFFFFFEFFFF"
    Found DFU: [0483:df11] ver=2200, devnum=61, cfg=1, intf=0, path="1-4", alt=0, name="@Internal Flash  /0x08000000/064*0002Kg", serial="FFFFFFFEFFFF"

Download a firmware from the keyboard to a file::

    $ dfu-util --upload foo.bin --alt 0 --dfuse-address 0x08000000
    dfu-util 0.9

    Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
    Copyright 2010-2016 Tormod Volden and Stefan Schmidt
    This program is Free Software and has ABSOLUTELY NO WARRANTY
    Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

    Opening DFU capable USB device...
    ID 0483:df11
    Run-time device DFU version 011a
    Claiming USB DFU Interface...
    Setting Alternate Setting #0 ...
    Determining device status: state = dfuIDLE, status = 0
    dfuIDLE, continuing
    DFU mode device DFU version 011a
    Device returned transfer size 2048
    DfuSe interface name: "Internal Flash  "
    Limiting upload to end of memory segment, 131072 bytes
    Upload	[=========================] 100%       131072 bytes
    Upload done.

Upload a firmware from a file to the keyboard::

    $ dfu-util --download qmk_durgod_k320_default.bin --alt 0 --dfuse-address 0x08000000
    dfu-util 0.9

    Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
    Copyright 2010-2016 Tormod Volden and Stefan Schmidt
    This program is Free Software and has ABSOLUTELY NO WARRANTY
    Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

    Match vendor ID from file: 0483
    Match product ID from file: df11
    Opening DFU capable USB device...
    ID 0483:df11
    Run-time device DFU version 011a
    Claiming USB DFU Interface...
    Setting Alternate Setting #0 ...
    Determining device status: state = dfuIDLE, status = 0
    dfuIDLE, continuing
    DFU mode device DFU version 011a
    Device returned transfer size 2048
    DfuSe interface name: "Internal Flash  "
    Downloading to address = 0x08000000, size = 22336
    Download	[=========================] 100%        22336 bytes
    Download done.
    File downloaded successfully

* https://ardupilot.org/dev/docs/using-DFU-to-load-bootloader.html


USB Device Info
---------------


K320 Original Firmware
~~~~~~~~~~~~~~~~~~~~~~

On Linux, the K320 running the stock firmware shows up as::

    # usb-devices
    ...
    T:  Bus=01 Lev=01 Prnt=01 Port=03 Cnt=01 Dev#= 56 Spd=12  MxCh= 0
    D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
    P:  Vendor=2f68 ProdID=0082 Rev=01.03
    S:  Manufacturer=Hoksi Technology
    S:  Product=DURGOD Taurus K320
    C:  #Ifs= 3 Cfg#= 1 Atr=a0 MxPwr=500mA
    I:  If#=0x0 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=01 Driver=usbhid
    I:  If#=0x1 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=00 Driver=usbhid
    I:  If#=0x2 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
    ...

    # usbhid-dump
    001:056:002:DESCRIPTOR         1611164734.131720
     06 C2 FF 09 02 A1 01 15 00 26 FF 00 95 40 75 08
     09 02 B1 02 09 02 81 02 09 02 91 02 C0

    001:056:001:DESCRIPTOR         1611164734.133692
     05 01 09 80 A1 01 85 01 19 81 29 83 15 00 25 01
     95 03 75 01 81 02 95 05 81 01 C0 05 0C 09 01 A1
     01 85 02 19 00 2A 3C 02 15 00 26 3C 02 95 01 75
     10 81 00 95 01 75 08 81 01 C0 05 01 09 06 A1 01
     85 03 05 07 95 68 75 01 15 00 25 01 19 00 29 68
     81 02 C0 05 01 09 02 A1 01 85 04 09 01 A1 00 05
     09 19 01 29 05 15 00 25 01 75 01 95 05 81 02 75
     01 95 03 81 01 05 01 09 38 15 81 25 7F 75 08 95
     01 81 06 09 30 09 31 16 00 80 26 FF 7F 75 10 95
     02 81 06 05 0C 0A 38 02 15 81 25 7F 75 08 95 01
     81 06 C0 C0

    001:056:000:DESCRIPTOR         1611164734.137533
     05 01 09 06 A1 01 05 08 15 00 25 01 19 01 29 05
     95 05 75 01 91 02 95 03 91 01 05 07 19 E0 29 E7
     75 01 95 08 81 02 95 08 81 01 15 00 25 E7 19 00
     29 E7 95 06 75 08 81 00 C0

    # lsusb
    ...
    Bus 001 Device 057: ID 2f68:0082
    ...

    # lsusb -v
    ...
    Bus 001 Device 056: ID 2f68:0082
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               2.00
      bDeviceClass            0
      bDeviceSubClass         0
      bDeviceProtocol         0
      bMaxPacketSize0        64
      idVendor           0x2f68
      idProduct          0x0082
      bcdDevice            1.03
      iManufacturer           1
      iProduct                2
      iSerial                 0
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength       0x005b
        bNumInterfaces          3
        bConfigurationValue     1
        iConfiguration          0
        bmAttributes         0xa0
          (Bus Powered)
          Remote Wakeup
        MaxPower              500mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      1 Keyboard
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      57
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x81  EP 1 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0008  1x 8 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      0
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength     164
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x82  EP 2 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0010  1x 16 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       0
          bNumEndpoints           2
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      29
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x83  EP 3 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x03  EP 3 OUT
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
    ...

On macOS, the K320 running the stock firmware shows up as::

    DURGOD Taurus K320:

      Product ID:	0x0082
      Vendor ID:	0x2f68
      Version:	1.03
      Speed:	Up to 12 Mb/s
      Manufacturer:	Hoksi Technology
      Location ID:	0x14610000 / 57
      Current Available (mA):	500
      Current Required (mA):	500
      Extra Operating Current (mA):	0


K320 QMK Firmware
~~~~~~~~~~~~~~~~~

On Linux, the K320 running the QMK firmware shows up as::

    # usb-devices
    ...
    T:  Bus=01 Lev=01 Prnt=01 Port=03 Cnt=01 Dev#= 67 Spd=12  MxCh= 0
    D:  Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
    P:  Vendor=d60d ProdID=3200 Rev=00.01
    S:  Manufacturer=Hoksi Technology
    S:  Product=DURGOD Taurus K320 (QMK)
    C:  #Ifs= 2 Cfg#= 1 Atr=a0 MxPwr=500mA
    I:  If#=0x0 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=01 Driver=usbhid
    I:  If#=0x1 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
    ...

    # usbhid-dump
    001:067:001:DESCRIPTOR         1611364091.322183
     05 01 09 80 A1 01 85 03 19 01 2A B7 00 15 01 26
     B7 00 95 01 75 10 81 00 C0 05 0C 09 01 A1 01 85
     04 19 01 2A A0 02 15 01 26 A0 02 95 01 75 10 81
     00 C0 05 01 09 06 A1 01 85 05 05 07 19 E0 29 E7
     15 00 25 01 95 08 75 01 81 02 05 07 19 00 29 EF
     15 00 25 01 95 F0 75 01 81 02 05 08 19 01 29 05
     95 05 75 01 91 02 95 01 75 03 91 01 C0

    001:067:000:DESCRIPTOR         1611364091.324798
     05 01 09 06 A1 01 05 07 19 E0 29 E7 15 00 25 01
     95 08 75 01 81 02 95 01 75 08 81 01 05 07 19 00
     29 FF 15 00 26 FF 00 95 06 75 08 81 00 05 08 19
     01 29 05 95 05 75 01 91 02 95 01 75 03 91 01 C0

    # lsusb
    ...
    Bus 001 Device 067: ID d60d:3200  
    ...

    # lsusb -v
    ...
    Bus 001 Device 067: ID d60d:3200  
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               1.10
      bDeviceClass            0 
      bDeviceSubClass         0 
      bDeviceProtocol         0 
      bMaxPacketSize0        64
      idVendor           0xd60d 
      idProduct          0x3200 
      bcdDevice            0.01
      iManufacturer           1 Hoksi Technology
      iProduct                2 DURGOD Taurus K320 (QMK)
      iSerial                 0 
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength       0x003b
        bNumInterfaces          2
        bConfigurationValue     1
        iConfiguration          0 
        bmAttributes         0xa0
          (Bus Powered)
          Remote Wakeup
        MaxPower              500mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      1 Keyboard
          iInterface              0 
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.11
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      64
             Report Descriptors: 
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x81  EP 1 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0008  1x 8 bytes
            bInterval              10
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      0 
          bInterfaceProtocol      0 
          iInterface              0 
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.11
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength     109
             Report Descriptors: 
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x82  EP 2 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0020  1x 32 bytes
            bInterval              10
    ...

On macOS, the K320 running the QMK firmware shows up as::

    DURGOD Taurus K320 (QMK):

      Product ID:	0x3200
      Vendor ID:	0xd60d
      Version:	0.01
      Speed:	Up to 12 Mb/s
      Manufacturer:	Hoksi Technology
      Location ID:	0x14640000 / 31
      Current Available (mA):	500
      Current Required (mA):	500
      Extra Operating Current (mA):	0


K310 Original Firmware
~~~~~~~~~~~~~~~~~~~~~~

On Linux, the K310 running the stock firmware shows up as::

    # usb-devices
    ...
    T:  Bus=01 Lev=01 Prnt=01 Port=03 Cnt=01 Dev#= 66 Spd=12  MxCh= 0
    D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
    P:  Vendor=2f68 ProdID=0042 Rev=01.04
    S:  Manufacturer=Hoksi Technology
    S:  Product=DURGOD Taurus K310
    C:  #Ifs= 3 Cfg#= 1 Atr=a0 MxPwr=500mA
    I:  If#=0x0 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=01 Driver=usbhid
    I:  If#=0x1 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=01 Prot=00 Driver=usbhid
    I:  If#=0x2 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
    ...

    # usbhid-dump
    001:066:002:DESCRIPTOR         1611363098.485492
     06 C2 FF 09 02 A1 01 15 00 26 FF 00 95 40 75 08
     09 02 B1 02 09 02 81 02 09 02 91 02 C0

    001:066:001:DESCRIPTOR         1611363098.486422
     05 01 09 80 A1 01 85 01 19 81 29 83 15 00 25 01
     95 03 75 01 81 02 95 05 81 01 C0 05 0C 09 01 A1
     01 85 02 19 00 2A 3C 02 15 00 26 3C 02 95 01 75
     10 81 00 95 01 75 08 81 01 C0 05 01 09 06 A1 01
     85 03 05 07 95 68 75 01 15 00 25 01 19 00 29 68
     81 02 C0 05 01 09 02 A1 01 85 04 09 01 A1 00 05
     09 19 01 29 05 15 00 25 01 75 01 95 05 81 02 75
     01 95 03 81 01 05 01 09 38 15 81 25 7F 75 08 95
     01 81 06 09 30 09 31 16 00 80 26 FF 7F 75 10 95
     02 81 06 05 0C 0A 38 02 15 81 25 7F 75 08 95 01
     81 06 C0 C0

    001:066:000:DESCRIPTOR         1611363098.492332
     05 01 09 06 A1 01 05 08 15 00 25 01 19 01 29 05
     95 05 75 01 91 02 95 03 91 01 05 07 19 E0 29 E7
     75 01 95 08 81 02 95 08 81 01 15 00 25 E7 19 00
     29 E7 95 06 75 08 81 00 C0

    # lsusb
    ...
    Bus 001 Device 066: ID 2f68:0042
    ...

    # lsusb -v
    ...
    Bus 001 Device 066: ID 2f68:0042
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               2.00
      bDeviceClass            0
      bDeviceSubClass         0
      bDeviceProtocol         0
      bMaxPacketSize0        64
      idVendor           0x2f68
      idProduct          0x0042
      bcdDevice            1.04
      iManufacturer           1 Hoksi Technology
      iProduct                2 DURGOD Taurus K310
      iSerial                 0
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength       0x005b
        bNumInterfaces          3
        bConfigurationValue     1
        iConfiguration          0
        bmAttributes         0xa0
          (Bus Powered)
          Remote Wakeup
        MaxPower              500mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      1 Keyboard
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      57
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x81  EP 1 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0008  1x 8 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      1 Boot Interface Subclass
          bInterfaceProtocol      0
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength     164
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x82  EP 2 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0010  1x 16 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       0
          bNumEndpoints           2
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      0
          bInterfaceProtocol      0
          iInterface              0
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      29
             Report Descriptors:
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x83  EP 3 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x03  EP 3 OUT
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
    ...

On macOS, the K310 running the stock firmware shows up as::

    TBD


K310 QMK Firmware
~~~~~~~~~~~~~~~~~

On Linux, the K310 running the QMK firmware shows up as::

    TBD

On macOS, the K310 running the QMK firmware shows up as::

    TBD
