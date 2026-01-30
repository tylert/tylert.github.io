# Video/Audio/Camera Awesome

```
    # Convert files to/from other formats
    ffmpeg -i foo.mov -map 0 -c copy foo.mp4
    ffmpeg -i foo.webm -c copy foo.mp4

    # Downsample videos and/or chop off/out sections based on time
    # to alter length of videos, after the -i, add:  '-ss' start time, '-t' duration or '-to' end time
    ffmpeg -i foo.mpg -r 30 -s 960x540 smaller.mp4

    # Concatenate files end-to-end
    # put "file 1.mp4\nfile2.mp4" and so on in a list.txt file and then run
    ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4

    # audio cd -> wav -> flac
    cdda2wav -vall cddb=0 speed=4 -paranoia paraopts=proof -B -D /dev/sr0
    flac --verify foo.wav

    # Stream ripping example (try to keep metadata; needs work)
    ffmpeg -i http://fr.ah.fm:8000/192k -map_metadata 0:s:0 ah_fm.mp3

    # Yootoob
    yt-dlp -f 'bv[height<=360]+ba' https://foobiewoobie.com/wholebunchofblablablablablabla
```

Just fix the title of the video file:

```
    ffmpeg -i input.whatever -c copy -map 0 -metadata title='Something else' output.whatever
```

HandBrake settings for DVDs:

```
    # Start with settings 'Official -> General -> HQ 1080p30 Surround'
    Summary:
        Format:  MPEG-4 (avformat)
        Web Optimized:  disabled
        Align A/V Start:  enabled
        iPod 5G Support:  disabled
        Passthru Common Metadata:  enabled
    Dimensions:
        Flipping Horizontal:  disabled
        Rotation:  Off
        Cropping:  Conservative or None depending on the disc
        Resolution Limit:  720p HD
        Anamorphic:  Automatic
        Optimal Size:  enabled
        Allow Upscaling:  disabled
        Borders Fill:  None
        Color:  Black
        Final Dimensions Automatic:  enabled
    Filters:
        Detelecine:  Off
        Interlace Detection:  Default
        Deinterlace:  Decomb
        Deinterlace Preset:  Default
        Deblock Filter:  Off
        Denoise Filter:  Off
        Chroma Smooth Filter:  Off
        Sharpen Filter:  Off
        Colorspace:  Off
        Grayscale:  disabled
    Video:
        Video Encoder:  H.264 (x264)
        Framerate:  30
        RF:  19
        Constant Quality:  selected
        Constant Framerate:  selected
        Preset:  slow
        Tune:  None
        Fast Decode:  disabled
        Profile:  high
        Level:  4.0
    Audio:
        Bitrate:  English (AC3) (5.1 ch) 448 kpbs (48 kHz) -> AAC (avcodec) Stereo 160 kbps
        Gain:  7 dB
        DRC:  4.0
    Subtitles:
        Foreign Audio Scan -> Burned Into Video (Forced Subtitles Only)
```

- <https://trac.ffmpeg.org/wiki/Capture/Desktop>
- <https://img.ly/blog/ultimate-guide-to-ffmpeg>
- <https://mifi.no/losslesscut>
- <https://github.com/mifi/lossless-cut>
- <https://en.wikipedia.org/wiki/LosslessCut>
- <https://frigate.video>
- <https://motion-project.github.io> MotionEye
- <https://danq.me/2025/05/26/downloading-vs-streaming>
- <https://rm2000.app> macOS app that acts like a tape recorder
- <http://nyanko.ws/nymphcast.php> NymphCast Linux network video/audio stuff (mandatory 'http' here)
- <https://github.com/MayaPosch/NymphCast> NymphCast Linux network video/audio stuff
- <https://gist.github.com/arch1t3cht/b5b9552633567fa7658deee5aec60453> details about working with video files


# Font Stuff

- <https://stackoverflow.com/questions/38299930/how-to-add-a-simple-text-label-to-an-image-in-go>
- <https://github.com/faiface/pixel/wiki/Typing-text-on-the-screen>
- <https://github.com/golang/freetype/blob/master/example/freetype/main.go>
- <https://blog.willdepue.com/how-to-legally-pirate-all-fonts-in-an-afternoon>
- <https://www.technomancer.com/archives/163> creating a Linux console font
- <https://reddit.com/r/linuxquestions/comments/7st7hz/any_way_to_convert_ttf_files_to_psf_files>
- <https://en.wikipedia.org/wiki/PC_Screen_Font> pretty simple format in case you want to just handbomb it
- <https://aur.archlinux.org/packages/otf2bdf>
- <https://aur.archlinux.org/packages/bdf2psf>
- <https://heckmeck.de/computerstuff/psf_tools>
- <https://linuxfromscratch.org/blfs/view/basic/console-fonts.html>
- <https://github.com/NateChoe1/ttf2psf> maybe convert TTF to PSF directly
- <https://github.com/pcarrin2/otf2psf>

```
    setfont moo.psf.gz
```


# ANSI and PETSCII and so on

- <http://viznut.fi/unscii> unicode bitmapped fonts for classic computing
- <https://github.com/viznut/unscii>
- <https://github.com/TheZoraiz/ascii-image-converter>


# Screen Recording

Record terminal commands to an SVG animation:

```
    pip install termtosvg  # termtosvg is currently abandonware
    echo "PS1='\$ '" > ugh.sh
    termtosvg login.svg --screen-geometry 80x10 --command 'bash --rcfile ugh.sh'
```

- <https://help.gnome.org/users/gnome-help/stable/screen-shot-record.html.en> hotkeys for video screen recording
- <https://bubelov.com/blog/2020/10/gnome-screenshots> hotkeys for static screen captures

```
    Shift + Ctrl + Alt + R  # start screen recording (same combo when you're done to stop it)
```


# Photography Stuff

- <https://jackw01.github.io/scanlight> negative/slide scanning light source
- <https://github.com/wikey/bookscan> workflow automation for scanning books
- <https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes>
- <https://gitlab.com/zephray/sitina1> open-source DSLR body
- <https://printables.com/model/356278-camera-2-cinema-style-camera-housing-for-raspberry>
- <https://github.com/eat-sleep-code/camera>
- <https://github.com/schoolpost/CinePI> CinePi v2


# Microscopes and Camera Stuff

- <https://ibm-research.medium.com/ibm-open-sources-300-fully-functional-lego-microscope-design-248a6cdc81bf>
- <https://jakecoppinger.com/2022/12/creating-aerial-imagery-with-a-bike-helmet-camera-and-opendronemap>
- <https://joshuabird.com/blog/post/3d-printed-film-video-camera>
- <https://people.skolelinux.org/pere/blog/Managing_and_using_ONVIF_IP_cameras_with_Linux.html>
- <https://www.diy-thermocam.net> IR imagery with nearly, nearly all open-source stuff (Teensy meh)
- <https://github.com/Jana-Marie/ligra> open-source projector?
- <https://www.anfractuosity.com/projects/cnc-microscopy>
- <https://openflexure.org/projects/microscope>
- <https://github.com/TadPath/PUMA> PUMA Microscope (PUMA = Portable Upgradeable Modular Affordable)
- <https://docs.hackerfab.org/hacker-fab-space>
- <https://www.briandorey.com/post/raspberry-pi-high-quality-camera-on-the-microscope>
- <https://mariozechner.at/posts/2025-04-20-boxie> USB microscope upgrade?


# Camera Stuff

- <https://uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-csi-usb-uvc-camera-adapter-board-for-12-3mp-imx477-raspberry-pi-camera-b0278.html>
- <https://uctronics.com/camera-modules/camera-for-raspberry-pi/arducam-12mp-imx477-ir-cut-filter-auto-switch-camera-for-raspberry-pi-b0270.html>
- <https://arducam.com/64mp-ultra-high-res-camera-raspberry-pi>
- <https://kickstarter.com/projects/blindspotgear/power-any-camera-and-12-volt-device-with-the-power-junkie-v2>
- <http://www.kevsrobots.com/blog/pikon-camera.html>
- <https://www.codeproject.com/Articles/665518/Raspberry-Pi-as-low-cost-HD-surveillance-camera>
- <https://www.pyimagesearch.com/2016/01/18/multiple-cameras-with-the-raspberry-pi-and-opencv>
- <https://github.com/jasaw/bbPiCam>
- <https://linux.com/learn/give-your-raspberry-pi-night-vision-pinoir-camera>
- <https://waveshare.com/wiki/RPi_IR-CUT_Camera>
- <https://amazon.ca/gp/product/B01M1BZXJQ>
- <https://amazon.ca/gp/product/B0056XFS5S>
- <https://amazon.ca/gp/product/B003AXEFMI>
- <http://nestboxtech.blogspot.ca/2014/10/how-to-make-your-own-raspberry-pi-trail.html>
- <http://instructables.com/id/PiPoE-powering-a-Raspberry-Pi-over-Ethernet>
- <https://ruha.camera>
- <https://reolink.com> ONVIF cameras (seem to get bad reviews from the Frigate folks though)
- <https://frigate.video> NVR software?
- <https://shinobi.video> has Nodejs gunk
- <https://zoneminder.com> another possibility
- <https://aliexpress.com/item/1005004626681677.html> Ingenic T31X + ONVIF + PoE (4 or 5 MPx, 3.6 mm lens)???

850 nm near IR


# Thermal Imaging

- <https://github.com/samyk/GetThermal>
- <https://github.com/groupgets/GetThermal> viewer for cheap USB thermal webcams?
- <https://groupgets.com/collections/lepton> cheap USB thermal webcam options?


# CHDK Doc/Book Scanner

- <https://mighty-hoernsche.de>
- <https://chdk.fandom.com/wiki/CHDK>
- <https://chdk.fandom.com/wiki/CHDK_User_Manual>
- <https://chdk.fandom.com/wiki/PTP_Extension>
- <https://app.assembla.com/wiki/show/chdkptp>
- <https://aur.archlinux.org/packages/chdkptp-svn> currently abandoned package
- <https://gitman.readthedocs.io/en/latest/setup/git-svn> git-svn annoyances?
- <https://chdk.setepontos.com/index.php?topic=14091.0> set_clock to set camera date/time
- <https://diybookscanner.org>
- <https://diybookscanner.org/en/intro.html> some camera selection criteria
- <https://duckduckgo.com/?q=diy+book+scanner&ia=images&iax=images>
- <https://scantips.com>
- <https://ocr4all.org/about/ocr4all> automated workflows for OCR?
- <https://www.monperrus.net/martin/store-data-paper> (mandatory 'www' here)
- <https://www.monperrus.net/martin/perfect-ocr-digital-data> (mandatory 'www' here)
- <https://thephoblographer.com/2025/08/20/how-chdk-helped-bring-my-old-canon-back-to-life>
- <https://35mmc.com/13/06/2022/digital-negatives-the-power-of-chdk-on-canon-powershots-by-sean-benham>
- <https://danielc.dev/ptp/chdk>
- <https://aggregate.org/DIT/CHDK> CHDK with CHDKPTP remote control
- <https://chdk.fandom.com/wiki/Multiple_Cameras_using_CHDK>
- <https://github.com/Tenrec-Builders/pi-scan>
- <https://chdk.setepontos.com/index.php?topic=14229.0> two cameras with chdkptp
- <https://chdk.setepontos.com/index.php?topic=13442.0> simultaneous capture with dual cameras and chdkptp scripts
- <https://github.com/scoder/lupa> Python with inline Lua

```
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
```

Upgrading CHDK

1.  fetch CHDK firmware zip for "Elph 115" (full).
1.  put SD card in camera (unlocked).
1.  hit "Play" button to start camera without moving the lens.
1.  select menu item to format SD card.
1.  power off camera.
1.  put SD card in computer (unlocked).
1.  extract CHDK firmware zip onto root of SD card.
1.  unmount SD card from computer.
1.  put SD card in camera (unlocked).
1.  select menu item to upgrade firmware.
1.  hit "Play" button to enter "<ALT>" mode.
1.  select menu item Miscellaneous -> Make SD card bootable.
1.  power off camera and take out SD card.
1.  put SD card in camera (locked).
1.  power off camera.


# Music and Audio Stuff

- <https://github.com/sergree/matchering> funky AI stuff with music
- <https://opendaw.studio> DAW in a web browser
- <https://sallywolf.ca> flute and recorder lessons
- <https://codeberg.org/unspeaker/tek> old-school tracker?
- <https://crowdsupply.com/cool-tech-zone/tangara> currently unobtainable (CAD \$250+)
- <https://amazon.ca/HIFI-WALKER-H2-Resolution-Bluetooth/dp/B072C4YPCG> runs Rockbox and you can get it now (CAD \$170)
- <https://rockbox.org/wiki/AIGOErosQK.html> install Rockbox on 'HIFI WALKER H2'
- <https://rockbox.org/wiki/JztoolInstall.html> install Rockbox on 'HIFI WALKER H2'
- <https://mynoise.net> OMFG fabulous background sounds (forest, waterfall, kitten purring, ringing bowls, etc.)
- <https://hannahilea.com/blog/birdnet-intro> BirdNET-Pi
- <https://sonic-pi.net>
- <https://bespokesynth.com>
- <https://youtube.com/watch?v=JDxhkdm_t1U> DJ Dave
- <https://lmms.io>
- <https://ardour.org>
- <https://tenacityaudio.org>
- <https://audacityteam.org>
- <https://milkytracker.org>
- <https://schismtracker.org>
- <https://renoise.com>
- <https://renoise.com/redux>
- <https://docs.qmk.fm/features/midi>
- <https://docs.qmk.fm/features/sequencer>
- <https://hydrogen-music.org> drum machine
- <https://kx.studio/Applications:Carla>
- <https://qtractor.org>
- <https://famistudio.org> NES native and Linux options
- <https://kvraudio.com/product/stargate-daw-by-stargate-daw>
- <https://github.com/Daninet/mtxt>
- <https://abcnotation.com>
- <https://abcplus.sourceforge.net>


# CAD

- <https://nuxx.net/blog/2025/12/20/openscad-is-kinda-neat>
- <https://grid.space/stem>


# Blender

- <https://gitlab.com/sheepitrenderfarm>
- <https://www.sheepit-renderfarm.com/home>


# Graphics

- <https://raytracing.github.io/books/RayTracingInOneWeekend.html>
- <https://remove.bg> remove background from images automatically
- <https://remove.bg/b/remove-the-background-in-gimp>
- <https://ciechanow.ski/cameras-and-lenses>


# AI

- <https://github.com/Acly/krita-ai-diffusion> Krita plugin for inpaint/outpaint within images!!!
- <https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog>
- <https://www.cloudskillsboost.google/paths/118> generative AI learning path
- <https://github.com/vitoplantamura/OnnxStream> Stable Diffusion on Raspberry Pi Zero
- <https://simonwillison.net/2023/Nov/29/llamafile>
- <https://github.com/CHAITron/sketchdeco-code> auto-colourizing B&W drawings
- <https://stable-diffusion-art.com/qr-code> incorporates a QR code into artwork
- <https://ewintr.nl/posts/2025/building-a-personal-private-ai-computer-on-a-budget>
- <https://muffinman.io/blog/the-tiny-book-of-great-joys> centre-line tracing for pen plotting
- <https://github.com/trycua/cua> containers for AI?
- <https://koomen.dev/essays/horseless-carriages>
- <https://simonwillison.net/2025/Oct/13/nanochat>
- <https://github.com/hkjarral/Asterisk-AI-Voice-Agent>
- <https://news.ycombinator.com/item?id=46549444> Claude Code cleverness


# Other

- <https://github.com/esimov/triangle> make bitmaps look all triangley
- <https://voussoir.net/writing/css_for_printing>
- <https://nfraprado.net/post/vcard-rss-as-an-alternative-to-social-media.html>
- <https://www.blocklayer.com/sundial-popeng> paper horizontal sundial generator (not equatorial ones)
- <https://praxispuzzles.com/calendar_puzzle_rhombus>
- <https://annanay.dev/build-a-signboard> metal signs with cut vinyl overlays


# Printer

- <https://crowdsupply.com/open-tools/open-printer>


# Crafts

- <https://jeremykun.com/2023/04/01/were-knot-friends>


# Commerce

- <https://github.com/yournextstore/yournextstore> open-source Shopify with Stripe?
