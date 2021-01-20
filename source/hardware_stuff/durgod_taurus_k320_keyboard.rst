Durgod Taurus K320 Non-Backlit Keyboard
=======================================

Disassembly Video
-----------------

* https://www.youtube.com/watch?v=H-HN3f20aLI


Stock Firmware
--------------

On Linux, this device shows up as::

    $ usb-devices
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

    $ usbhid-dump
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

    $ lsusb
    ...
    Bus 001 Device 057: ID 2f68:0082  
    ...

    $ lsusb -v
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

On macOS, this device shows up as::

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
