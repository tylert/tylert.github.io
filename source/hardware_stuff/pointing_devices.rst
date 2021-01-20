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
