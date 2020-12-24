How to Install OSMC (Kodi + Raspbian) on a Raspberry Pi

1.  Download an image file.  Go to osmc.tv (https://osmc.tv/download/-> Disk
mmages) and fetch a new image or else pull a recently downloaded one off your
local storage somewhere.  Make sure to get the one for the appropriate model of
Raspberry Pi (0, 1, 2 or 3).  These instructions should be roughly pertient for
versions circa July 2017 and onwards.

2.  Flash the image file to your desired microSD card.  If you are flashing
this using a machine with an SD card reader, the device below will likely be
named "/dev/mmcblk0".  If you are flashing this on a machine with a USB reader,
the device below will likely be named "/dev/sdb" or "/dev/sdc".  Plug the
device in and then type "sudo dmesg" to look at the last few lines of output to
see the most recent hotplug events for the name of the applicable device.  Make
sure you specify the device itself (e.g.:  "/dev/mmcblk0" or "/dev/sdb") rather
than the partition number (e.g.:  "/dev/mmcblk0p1" or "/dev/sdb1").

Next, pop open a new terminal window and type the following command (again,
make sure the output file or "of" is set to the correct device location
mentioned above;  you may omit the "status=progress" part if your version of dd
doesn't support it or if you don't care about seeing a progress meter):

zcat $(find . -name OSMC*.img.gz) | sudo dd of=/dev/mmcblk0 bs=16M \
status=progress && sync
# ... or something like...
zcat OSMC_TGT_rbp2_20170803.img.gz | sudo dd of=/dev/sdb bs=16M \
&& sync

3.  Once your flashing is complete, plug everything back in again.  After a few
minutes, when the command prompt returns to being interactive again (the
"user@host:~$ " part of the command prompt is again printed on a fresh line to
indicate that it is waiting for new user input), just pop out the microSD card
and reinsert it into the Raspberry Pi.  Next, plug in ALL THE THINGS again and
let the unit boot up fully.

4.  Do the basic configuration steps.  After the units boots, the first thing
you'll be forced to set up is the language, timezone and hostname settings and
so on.  I usually pick "English", "America/Toronto" and "osmc" for mine.  Leave
the SSH service enabled.  Select your desired "Look + Feel" and choose whether
you want to sign up for the email newsletter and then exit the setup wizard
stuff.

5.  Pull in local file sources.  Go to "Videos" -> "Files" -> "Add videos" ->
"Browse".  Enter "smb://booya/somewhere/movie" for the location, hit OK to
accept the new location and then OK to accept the default name to assign to
this location.  "This directory contains" -> "Movies" -> OK.  "Do you want to
refresh information for all items within this path" -> No.  Do the same thing
again for "television".

6.  Fix the default regional settings.  Go to "Settings" -> "Interface" ->
"Regional" -> "Unit Formats" -> "Region default format" -> "USA (24h)".

7.  Fix the default subtitles settings.  Go to "Settings" -> "Player" ->
"Language" -> "Subtitles" -> "Preferred subtitle language" -> "None".

8.  Install a few mundane plug-ins.  Go to "Settings" -> "Add-on browser" and
select "Install from repository".  Go into the "Kodi Add-on repository".  Under
"Video add-ons", install the "HDHomeRun", "HGTV" and "HGTV Canada" plug-ins.


# https://github.com/oss001/KodiStreaming/blob/master/setup.sh
# https://makingstuffwork.net/technology/watch-netflix-amazon-prime-kodi/
# https://raspberrytips.com/install-netflix-on-kodi/
# https://raw.githubusercontent.com/zjoasan/netflix-install-script/master/netflix_prep_install.sh
# https://www.hackster.io/sbcomponentsuk/netflix-and-amazon-prime-video-now-streaming-on-raspberry-pi-44f3cb

#!/bin/bash
echo "Starting setup, this will only work on Kodi V18 or greater..."
apt-get update
apt-get install -y build-essential libnspr4 libnss3 python-crypto python-pip python-setuptools
pip install -U pip setuptools wheel pycryptodomex==3.8.2
# Netflix
wget https://github.com/CastagnaIT/plugin.video.netflix/archive/master.zip
# wget https://github.com/CastagnaIT/repository.castagnait/raw/master/repository.castagnait-1.0.0.zip
# Amazon Prime
# wget https://github.com/Sandmann79/xbmc/releases/download/v1.0.2/repository.sandmann79.plugins-1.0.2.zip

# Enable installation from unknown sources
# Install the zip crap from the add-on browser
