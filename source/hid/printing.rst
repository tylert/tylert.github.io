Brother P-Touch
---------------

* https://github.com/HenrikBengtsson/brother-ptouch-label-printer-on-linux
* https://git.familie-radermacher.ch/linux/ptouch-print.git  cutting edge
* https://aur.archlinux.org/packages/ptouch-print-git  kinda unmaintained and old
* https://aur.archlinux.org/packages/ptouch-print  way out of date

PT-2730::

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


3D
--

* https://calbryant.uk/blog/3d-printing-giant-things-with-jigsaw-generator
