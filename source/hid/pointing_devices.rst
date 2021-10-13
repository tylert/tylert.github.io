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


Ploopy Nano Gets Better Bearings
--------------------------------

The default bearings for the Ploopy Nano seem to get rusty with regular use.

* https://github.com/gbrnt/ploopy-nano/tree/master/hardware/mechanicals-btu-mod 3D files
* https://www.reddit.com/r/ploopy/comments/p7mkhd/new_btu_mod_for_ploopy_nano/ discussion
* https://imgur.com/a/o2Ar9VT original designer's renders and prototype pics
* https://i.imgur.com/PGTLar9.jpg finished print example
* https://www.reddit.com/r/ploopy/comments/ldfcde/heres_a_3dprintable_ploopy_trackball_mod_to_use/ BTU discussions


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
* https://www.reddit.com/r/ploopy/comments/oqwyzs/help_drag_scroll_as_held_key_in_tap_dance/
* https://www.reddit.com/r/ploopy/comments/ou2110/auto_hot_key_script_for_right_click_scroll_wheel/
* https://www.reddit.com/r/ploopy/comments/pl67bn/ploopy_mini_trackball_and_ubuntu/


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
