Pointing Devices
================

Ploopy Nano trackball.
Made in Canada (Mississauga, Ontario).
Very high quality, easy to repair and a great ordering experience.

Any ball between 37.6 and 38.3 mm should work (stock kit uses 38.1 mm ball).
Bearings are "MR63ZZ" and are available at places like Aliexpress.

* https://www.ploopy.co/nano-trackball
* https://www.ploopy.co/product/nano-trackball/11
* https://github.com/ploopyco/trackball-nano/wiki
* https://www.reddit.com/r/Trackballs/comments/lnhvpy/ploopy_nano_project_ballonly_trackball_is/
* https://github.com/brickbots/aball
* https://github.com/MangoIV/dracuLad
* https://github.com/foureight84/sofle-keyboard-pimoroni/blob/master/README.md
* https://github.com/monroewilliams/trackball
* https://shop.beekeeb.com/product/ploopy-nano-trackball-case-resin/
* https://www.keysofkings.com/shop/mice/trackball/ploopy-project-ruby/pcb/ploopy-project-ruby-pcbs/


More QMK Ploopy Stuff
---------------------

QMK build "0.12.26" or newer includes the mainline-merged Ploopy Nano code.

* https://github.com/qmk/qmk_firmware/pulls?q=is%3Apr+ploopy+is%3Aopen
* https://github.com/qmk/qmk_firmware/pulls?q=is%3Apr+ploopy+is%3Aclosed
* https://www.reddit.com/r/ploopy/comments/k1c7sh/drag_scroll_with_ploopy_trackball/
* https://www.reddit.com/r/ploopy/comments/merk8e/possible_for_nano_to_scroll_instead_of_moving/
* https://www.reddit.com/r/ploopy/comments/nfdmrc/ploopy_nano_for_scrolling/
* https://www.reddit.com/r/ploopy/comments/ngltuh/toggle_functionality_of_nano_using_other_qmk/
* https://www.reddit.com/r/ploopy/comments/nlvgkq/how_to_scroll_with_the_trackball_nano/
* https://www.reddit.com/r/ploopy/comments/nnb9qn/hold_to_drag_scroll/


Power Management
----------------

You might need to disable some silly USB stuff to get suspend to work "properly"::

    # Force the USB bus to not immediately wake up again as you try to suspend/hibernate
    sudo -s
    echo XHCI > /proc/acpi/wakeup

    # Find which device is Ploopy and set it to "auto" (off) during suspend/hibernate
    lsusb -t
    echo "auto" > /sys/bus/usb/devices/1-4/power/control

* https://www.kernel.org/doc/html/v4.19/driver-api/usb/power-management.html


Thiccpad Trackpoint Stuff
-------------------------

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


Mouseless Navigation
--------------------

* https://felipecortez.net/blog/mouseless.html
