Font Stuff
----------

* https://stackoverflow.com/questions/38299930/how-to-add-a-simple-text-label-to-an-image-in-go
* https://github.com/faiface/pixel/wiki/Typing-text-on-the-screen
* https://github.com/golang/freetype/blob/master/example/freetype/main.go
* https://blog.willdepue.com/how-to-legally-pirate-all-fonts-in-an-afternoon
* https://www.technomancer.com/archives/163  creating a Linux console font
* https://reddit.com/r/linuxquestions/comments/7st7hz/any_way_to_convert_ttf_files_to_psf_files
* https://en.wikipedia.org/wiki/PC_Screen_Font  pretty simple format in case you want to just handbomb it
* https://aur.archlinux.org/packages/otf2bdf
* https://aur.archlinux.org/packages/bdf2psf
* https://heckmeck.de/computerstuff/psf_tools
* https://linuxfromscratch.org/blfs/view/basic/console-fonts.html
* https://github.com/NateChoe1/ttf2psf  maybe convert TTF to PSF directly

::

    setfont moo.psf.gz


Screen Recording
----------------

Record terminal commands to an SVG animation::

    pip install termtosvg  # termtosvg is currently abandonware
    echo "PS1='\$ '" > ugh.sh
    termtosvg login.svg --screen-geometry 80x10 --command 'bash --rcfile ugh.sh'

* https://help.gnome.org/users/gnome-help/stable/screen-shot-record.html.en  hotkeys for video screen recording
* https://bubelov.com/blog/2020/10/gnome-screenshots  hotkeys for static screen captures

::

    Shift + Ctrl + Alt + R  # start screen recording (same combo when you're done to stop it)


Photography Stuff
-----------------

* https://jackw01.github.io/scanlight  negative/slide scanning light source
* https://github.com/wikey/bookscan  workflow automation for scanning books
* https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes
* http://aggregate.org/DIT/CHDK  CHDK with CHDKPTP remote control
* https://gitlab.com/zephray/sitina1  open-source DSLR body
* https://printables.com/model/356278-camera-2-cinema-style-camera-housing-for-raspberry
* https://github.com/eat-sleep-code/camera
* https://github.com/schoolpost/CinePI  CinePi v2

::

    0.  fetch CHDK firmware zip for "Elph 115" (full).
    1.  put SD card in camera (unlocked).
    2.  hit "Play" button to start camera without moving the lens.
    3.  select menu item to format SD card.
    4.  power off camera.
    5.  put SD card in computer (unlocked).
    6.  extract CHDK firmware zip onto root of SD card.
    7.  unmount SD card from computer.
    8.  put SD card in camera (unlocked).
    9.  select menu item to upgrade firmware.
    10.  hit "Play" button to enter "<ALT>" mode.
    11.  select menu item Miscellaneous -> Make SD card bootable.
    12.  power off camera and take out SD card.
    13.  put SD card in camera (locked).
    14.  power off camera.


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
* https://mariozechner.at/posts/2025-04-20-boxie  USB microscope upgrade?


Camera Stuff
------------

* https://uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-csi-usb-uvc-camera-adapter-board-for-12-3mp-imx477-raspberry-pi-camera-b0278.html
* https://uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-12mp-imx477-ir-cut-filter-auto-switch-camera-for-raspberry-pi-b0270.html
* https://arducam.com/64mp-ultra-high-res-camera-raspberry-pi
* https://kickstarter.com/projects/blindspotgear/power-any-camera-and-12-volt-device-with-the-power-junkie-v2
* http://www.kevsrobots.com/blog/pikon-camera.html
* https://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera
* https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv
* https://github.com/jasaw/bbPiCam
* https://linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera
* https://waveshare.com/wiki/RPi_IR-CUT_Camera
* https://amazon.ca/gp/product/B01M1BZXJQ
* https://amazon.ca/gp/product/B0056XFS5S
* https://amazon.ca/gp/product/B003AXEFMI
* http://nestboxtech.blogspot.ca/2014/10/how-to-make-your-own-raspberry-pi-trail.html
* http://instructables.com/id/PiPoE-powering-a-Raspberry-Pi-over-Ethernet
* https://ruha.camera
* https://reolink.com  ONVIF cameras (seem to get bad reviews from the Frigate folks though)
* https://frigate.video  NVR software?
* https://shinobi.video  has Nodejs gunk
* https://zoneminder.com  another possibility
* https://aliexpress.com/item/1005004626681677.html  Ingenic T31X + ONVIF + PoE (4 or 5 MPx, 3.6 mm lens)???

850 nm near IR


Thermal Imaging
---------------

* https://github.com/samyk/GetThermal
* https://github.com/groupgets/GetThermal  viewer for cheap USB thermal webcams?
* https://groupgets.com/collections/lepton  cheap USB thermal webcam options?


CHDK Doc/Book Scanner
---------------------

* https://chdk.fandom.com/wiki/CHDK_User_Manual
* https://chdk.fandom.com/wiki/PTP_Extension
* https://app.assembla.com/wiki/show/chdkptp
* https://aur.archlinux.org/packages/chdkptp-svn  currently abandoned package
* https://gitman.readthedocs.io/en/latest/setup/git-svn  git-svn annoyances?
* https://chdk.setepontos.com/index.php?topic=14091.0  set_clock to set camera date/time
* https://diybookscanner.org/en/intro.html  some camera selection criteria
* https://scantips.com
* https://ocr4all.org/about/ocr4all  automated workflows for OCR?

::

    pacman -S git subversion perl-term-readkey
    pacman -S libusb-compat lua53 lua53-lgi

    # Convert the subversion goop into a local git repo and compile it
    mkdir chdkptp
    pushd chdkptp
    svn --username=guest --password=guest ls https://subversion.assembla.com/svn/chdkptp
    git svn clone --username=guest https://subversion.assembla.com/svn/chdkptp  # branches, tags, trunk
    pushd trunk
    make LUA_LIB=lua5.3 LUA_INCLUDE_DIR=/usr/include/lua5.3 GUI=1 GTK_SUPPORT=1
    popd
    popd


Music and Audio Stuff
---------------------

* https://github.com/sergree/matchering  funky AI stuff with music
* https://opendaw.studio  DAW in a web browser
* https://sallywolf.ca  flute and recorder lessons
* https://codeberg.org/unspeaker/tek  old-school tracker?
* https://crowdsupply.com/cool-tech-zone/tangara  currently unobtainable (CAD $250+)
* https://amazon.ca/HIFI-WALKER-H2-Resolution-Bluetooth/dp/B072C4YPCG  runs Rockbox and you can get it now (CAD $170)
* https://rockbox.org/wiki/AIGOErosQK.html  install Rockbox on "HIFI WALKER H2"
* https://rockbox.org/wiki/JztoolInstall.html  install Rockbox on "HIFI WALKER H2"
* https://mynoise.net  OMFG fabulous background sounds (forest, waterfall, kitten purring, ringing bowls, etc.)
* https://hannahilea.com/blog/birdnet-intro  BirdNET-Pi
* https://sonic-pi.net
* https://bespokesynth.com
* https://youtube.com/watch?v=JDxhkdm_t1U  DJ Dave
* https://lmms.io
* https://ardour.org
* https://tenacityaudio.org
* https://audacityteam.org
* https://milkytracker.org
* https://schismtracker.org
* https://renoise.com
* https://renoise.com/redux
* https://docs.qmk.fm/features/midi
* https://docs.qmk.fm/features/sequencer
* https://hydrogen-music.org  drum machine
* https://kx.studio/Applications:Carla
* https://qtractor.org
* https://famistudio.org  NES native and Linux options
* https://kvraudio.com/product/stargate-daw-by-stargate-daw


Blender
-------

* https://gitlab.com/sheepitrenderfarm
* https://www.sheepit-renderfarm.com/home


Graphics
--------

* https://raytracing.github.io/books/RayTracingInOneWeekend.html
* https://remove.bg  remove background from images automatically
* https://remove.bg/b/remove-the-background-in-gimp


AI
--

* https://github.com/Acly/krita-ai-diffusion  Krita plugin for inpaint/outpaint within images!!!
* https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog
* https://www.cloudskillsboost.google/paths/118  generative AI learning path
* https://github.com/vitoplantamura/OnnxStream  Stable Diffusion on Raspberry Pi Zero
* https://simonwillison.net/2023/Nov/29/llamafile
* https://github.com/CHAITron/sketchdeco-code  auto-colourizing B&W drawings
* https://stable-diffusion-art.com/qr-code  incorporates a QR code into artwork
* https://ewintr.nl/posts/2025/building-a-personal-private-ai-computer-on-a-budget
* https://muffinman.io/blog/the-tiny-book-of-great-joys  centre-line tracing for pen plotting
* https://github.com/trycua/cua  containers for AI?
* https://koomen.dev/essays/horseless-carriages
* https://simonwillison.net/2025/Oct/13/nanochat


Other
-----

* https://github.com/esimov/triangle  make bitmaps look all triangley
* https://voussoir.net/writing/css_for_printing
* https://nfraprado.net/post/vcard-rss-as-an-alternative-to-social-media.html
* https://www.blocklayer.com/sundial-popeng  paper horizontal sundial generator (not equatorial ones)
* https://praxispuzzles.com/calendar_puzzle_rhombus


Printer
-------

* https://crowdsupply.com/open-tools/open-printer
