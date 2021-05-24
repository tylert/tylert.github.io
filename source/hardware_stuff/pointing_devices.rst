Pointing Devices
================

Ploopy Nano Trackball.

Any ball between 38.3 and 47.6 mm should work (stock kit uses 38.1 mm ball).

* https://www.ploopy.co/nano-trackball
* https://www.ploopy.co/product/nano-trackball/11
* https://github.com/ploopyco/trackball-nano/wiki
* https://www.reddit.com/r/Trackballs/comments/lnhvpy/ploopy_nano_project_ballonly_trackball_is/
* https://github.com/brickbots/aball
* https://github.com/MangoIV/dracuLad
* https://github.com/foureight84/sofle-keyboard-pimoroni/blob/master/README.md
* https://github.com/monroewilliams/trackball
* https://www.keysofkings.com/shop/mice/trackball/ploopy-project-ruby/pcb/ploopy-project-ruby-pcbs/
* https://shop.beekeeb.com/product/ploopy-nano-trackball-case-resin/


QMK Ploopy Stuff
----------------

Ploopy Nano has been merged and available in build "0.12.26".

* https://github.com/qmk/qmk_firmware/pull/11994
* https://www.reddit.com/r/ploopy/comments/merk8e/possible_for_nano_to_scroll_instead_of_moving/
* https://www.reddit.com/r/ploopy/comments/k1c7sh/drag_scroll_with_ploopy_trackball/

You might need to disable some silly USB stuff to get suspend to work "properly"::

    # Force the USB bus to not immediately wake up again as you try to suspend/hibernate
    sudo -s
    echo XHCI > /proc/acpi/wakeup

    # Find which device is Ploopy and set it to "auto" (off) during suspend/hibernate
    lsusb -t
    echo "auto" > /sys/bus/usb/devices/1-4/power/control


Trackpoint Setup
----------------

::

    # https://wiki.debian.org/InstallingDebianOn/Thinkpad/Trackpoint
    # apt-get install xinput
    # Add the following to ~/.xsessionrc

    # vertical scroll
    xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation" 1
    xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Button" 2
    xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Timeout" 200

    # horizontal scroll
    xinput set-prop "TPPS/2 IBM TrackPoint" "Evdev Wheel Emulation Axes" 6 7 4 5


Other/Wireless Keyboards
------------------------

* https://keebfol.io/
* https://zmkfirmware.dev/
* https://github.com/zmkfirmware/zmk
