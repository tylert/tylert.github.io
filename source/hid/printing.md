# Brother Label Printers

* <https://github.com/HenrikBengtsson/brother-ptouch-label-printer-on-linux>
* <https://git.familie-radermacher.ch/linux/ptouch-print.git> cutting edge
* <https://aur.archlinux.org/packages/ptouch-print-git> kinda unmaintained and old
* <https://aur.archlinux.org/packages/ptouch-print> way out of date
* <https://nmattia.com/posts/2025-08-28-label-printer-rpi-nix>
* <https://github.com/pklaus/brother_ql>

PT-2730:

    # Fetch the source
    git clone https://git.familie-radermacher.ch/linux/ptouch-print.git
    cd ptouch-print

    # Build the tool
    ./build.sh
    sudo make -C build install

    # Check things out
    ptouch-print --list-supported
    ptouch-print --info

    # Produce some labels
    ptouch-print --text 'Flibbertifloo' 'Fiddledeedee' --writepng moo.png
    ptouch-print --text 'Wheeeeeeee' --writepng boo.png
    ptouch-print --image moo.png --pad 10 --image boo.png

    # Make fancier labels
    ptouch-print --font 'Noto Sans Black' --text BAMALAM --writepng bla.png


# 3D

* <https://calbryant.uk/blog/3d-printing-giant-things-with-jigsaw-generator>


# Dymo Tapewriter

* <https://thingiverse.com/thing:5150698> replacement driver gear
* <https://github.com/andreisperid/E-TKT>
* <https://andreisperid.github.io/E-TKT>
* <https://glenalec.net/projects/dymo> custom embossing wheels (wrong model)
* <https://thingiverse.com/thing:6176018> custom embossing wheels (wrong model)


# Other

* <https://behind.pretix.eu/2018/01/20/cups-driver> writing your own custom CUPS driver in Python
* <https://github.com/pretix/cups-fgl-printers> ticket printers driver source
* <https://aur.archlinux.org/packages/cups-fgl-printers-git> Arch ticket printers
* <https://download.pretix.eu> Debian ticket printers
