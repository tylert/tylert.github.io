Font Stuff
----------

* https://stackoverflow.com/questions/38299930/how-to-add-a-simple-text-label-to-an-image-in-go
* https://github.com/faiface/pixel/wiki/Typing-text-on-the-screen
* https://github.com/golang/freetype/blob/master/example/freetype/main.go


Photography Stuff
-----------------

* https://jackw01.github.io/scanlight  negative/slide scanning light source
* https://github.com/wikey/bookscan  workflow automation for scanning books
* https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes
* http://aggregate.org/DIT/CHDK  CHDK with CHDKPTP remote control


Microscopes and Camera Stuff
----------------------------

* https://ibm-research.medium.com/ibm-open-sources-300-fully-functional-lego-microscope-design-248a6cdc81bf
* https://jakecoppinger.com/2022/12/creating-aerial-imagery-with-a-bike-helmet-camera-and-opendronemap
* https://joshuabird.com/blog/post/3d-printed-film-video-camera
* https://people.skolelinux.org/pere/blog/Managing_and_using_ONVIF_IP_cameras_with_Linux.html
* https://www.diy-thermocam.net  IR imagery with nearly, nearly all open-source stuff (Teensy meh)
* https://github.com/Jana-Marie/ligra  open-source projector?
* https://www.anfractuosity.com/projects/cnc-microscopy
* https://openflexure.org/projects/microscope
* https://github.com/TadPath/PUMA  PUMA Microscope (PUMA = Portable Upgradeable Modular Affordable)
* https://docs.hackerfab.org/hacker-fab-space
* https://www.briandorey.com/post/raspberry-pi-high-quality-camera-on-the-microscope


Camera Stuff
------------

* https://www.uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-csi-usb-uvc-camera-adapter-board-for-12-3mp-imx477-raspberry-pi-camera-b0278.html
* https://www.uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-12mp-imx477-ir-cut-filter-auto-switch-camera-for-raspberry-pi-b0270.html
* https://www.arducam.com/64mp-ultra-high-res-camera-raspberry-pi
* https://www.kickstarter.com/projects/blindspotgear/power-any-camera-and-12-volt-device-with-the-power-junkie-v2
* http://www.kevsrobots.com/blog/pikon-camera.html
* https://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera
* https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv
* https://github.com/jasaw/bbPiCam
* https://www.linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera
* https://www.waveshare.com/wiki/RPi_IR-CUT_Camera
* https://www.amazon.ca/gp/product/B01M1BZXJQ
* https://www.amazon.ca/gp/product/B0056XFS5S
* https://www.amazon.ca/gp/product/B003AXEFMI
* http://nestboxtech.blogspot.ca/2014/10/how-to-make-your-own-raspberry-pi-trail.html
* http://www.instructables.com/id/PiPoE-powering-a-Raspberry-Pi-over-Ethernet
* https://ruha.camera

850 nm near IR


CHDK Doc/Book Scanner
---------------------

* https://chdk.fandom.com/wiki/CHDK_User_Manual
* https://chdk.fandom.com/wiki/PTP_Extension
* https://app.assembla.com/wiki/show/chdkptp
* https://aur.archlinux.org/packages/chdkptp-svn  currently abandoned package
* https://chdk.setepontos.com/index.php?topic=14091.0  set_clock to set camera date/time
* https://diybookscanner.org/en/intro.html  some camera selection criteria

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


Music Stuff
-----------

* https://github.com/sergree/matchering  funky AI stuff with music


Graphics
--------

* https://raytracing.github.io/books/RayTracingInOneWeekend.html


3D Printing
-----------

* https://github.com/cooljjj33/PolyDye  white filament + inkjet technology = full-colour prints


Other
-----

* https://github.com/Acly/krita-ai-diffusion  Krita plugin for inpaint/outpaint within images!!!
* https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog
* https://www.cloudskillsboost.google/paths/118  generative AI learning path
* https://github.com/esimov/triangle  make bitmaps look all triangley
* https://stable-diffusion-art.com/qr-code  artwork which incorporates a QR code into the image
* https://simonwillison.net/2023/Nov/29/llamafile
* https://penrose.cs.cmu.edu  web diagrams from text
* https://voussoir.net/writing/css_for_printing
* https://nfraprado.net/post/vcard-rss-as-an-alternative-to-social-media.html
* https://github.com/vitoplantamura/OnnxStream  Stable Diffusion on Raspberry Pi Zero
* https://www.blocklayer.com/sundial-popeng  paper horizontal sundial generator (not equatorial ones)
* https://github.com/CHAITron/sketchdeco-code  auto-colourizing B&W drawings
* https://sallywolf.ca  flute and recorder lessons


Woodworking
-----------

* https://aroundhomediy.com/build-roubo-workbench-leg-vise
* https://www.leevalley.com/en-ca/shop/tools/workshop/workbenches/benches-and-tables/117579-bora-centipede-table?item=99W8349
