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


QMK Ploopy Stuff
----------------

Ploopy Nano has been merged and available in build "0.12.26".

* https://github.com/qmk/qmk_firmware/pull/11994


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
