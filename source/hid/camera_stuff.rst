Camera Stuff
------------

* https://www.uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-csi-usb-uvc-camera-adapter-board-for-12-3mp-imx477-raspberry-pi-camera-b0278.html
* https://www.uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-12mp-imx477-ir-cut-filter-auto-switch-camera-for-raspberry-pi-b0270.html
* https://www.arducam.com/64mp-ultra-high-res-camera-raspberry-pi/
* https://www.kickstarter.com/projects/blindspotgear/power-any-camera-and-12-volt-device-with-the-power-junkie-v2
* http://www.kevsrobots.com/blog/pikon-camera.html
* https://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera
* https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv/
* https://github.com/jasaw/bbPiCam
* https://www.linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera
* https://www.waveshare.com/wiki/RPi_IR-CUT_Camera
* https://www.amazon.ca/gp/product/B01M1BZXJQ
* https://www.amazon.ca/gp/product/B0056XFS5S
* https://www.amazon.ca/gp/product/B003AXEFMI
* http://nestboxtech.blogspot.ca/2014/10/how-to-make-your-own-raspberry-pi-trail.html
* http://www.instructables.com/id/PiPoE-powering-a-Raspberry-Pi-over-Ethernet/
* https://ruha.camera/

850 nm near IR


CHDK Doc/Book Scanner
---------------------

* https://app.assembla.com/wiki/show/chdkptp
* https://aur.archlinux.org/packages/chdkptp-svn  currently abandoned package

::

    pacman -S git subversion
    pacman -S libusb-compat lua53 lua53-lgi

    # Prepare the subversion config gunk in your home directory so git-svn can work properly
    mkdir chdkptp-tmp
    pushd chdkptp-tmp
    svn checkout --username=guest https://subversion.assembla.com/svn/chdkptp/trunk
    # enter password "guest" at the prompt
    echo "store-passwords = yes" >> ~/.subversion/config
    echo "store-passwords = yes" >> ~/.subversion/servers
    popd

    # Convert the subversion goop into a local git repo and compile it
    mkdir chdkptp
    pushd chdkptp
    git svn clone --username=guest https://subversion.assembla.com/svn/chdkptp  # branches, tags, trunk
    pushd trunk
    make LUA_LIB=lua5.3 LUA_INCLUDE_DIR=/usr/include/lua5.3 GUI=1 GTK_SUPPORT=1
    popd
    popd
