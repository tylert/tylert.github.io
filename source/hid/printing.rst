Brother P-Touch
---------------

* https://github.com/HenrikBengtsson/brother-ptouch-label-printer-on-linux
* https://git.familie-radermacher.ch/linux/ptouch-print.git

PT-2730::

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
