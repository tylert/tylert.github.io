Things to do before upgrading your phone
----------------------------------------

1.  Try to update your phone to the latest firmware from your provider
1.  Make sure you backup local data from your phone (photos, messages, etc.)
1.  Go to "Settings -> About phone", tap "Build number" 7 times
1.  Go to "Developer options" and enable "Android debugging" (ADB USB debugging)
1.  Enable OEM unlocking in Developer options
1.  On your computer, download the requisite LineageOS and TWRP images for your phone


Actually upgrading your phone
-----------------------------

1.  Install adb and fastboot
1.  Connect the phone to the computer
1.  ``adb reboot bootloader``
1.  ``fastboot flashing unlock``
1.  ``fastboot flash recovery twrp-bla-bla-bla.img``
1.  ``fastboot boot twrp-bla-bla-bla.img``
1.  Do some stuff in the recovery to wipe/format a bunch of things (follow the instructions for your phone)
1.  Tell the phone to expect a sideload
1.  ``adb sideload lineage-bla-bla-bla.zip``
1.  Do the thing that prevents TWRP from being overwritten again
1.  Reboot into system


First-time setup
----------------

1.  Allow it to encrypt everything automatically and finish booting
1.  At the intro screen, hit NEXT
1.  Select "English (Canada)", hit NEXT
1.  Select your timezone, hit NEXT
1.  Under Wi-Fi preferences, turn off "Open network notification", go back, Connect to Wi-Fi accesspoint, hit NEXT
1.  At "Turn on cellular data" leave it unticked, hit NEXT
1.  Location services leave "Allow apps that have asked your permission" ticked, hit NEXT
1.  Untick "Help improve LineageOS", Tick "Enable Privacy Guard", hit NEXT
1.  At "Fingerprint setup" just hit SKIP
1.  Protect your phone hit SET UP, PIN, Secure start-up YES, punch in your PIN twice, hit NEXT
1.  At the final screen, hit START


Enable mobile networking
------------------------

If you don't have any phone network access after booting, go into "Settings ->
Security & privacy" and set your screen lock to none then reboot.  After
rebooting, go back in and restore your screen lock protection again.

Then go under "Network & Internet -> Mobile network -> Mobile data" and turn it
on.


Make the keyboard less annoying
-------------------------------

Under Sound turn off all the other sounds and vibrations.

Under System -> Languages & input -> Virtual keyboard -> Android Keyboard
(AOSP) -> Preferences turn off Auto-capitalisation, Double-space full stop and
Vibrate on keypress Then go under Text correction and turn off everything.
Also set the Appearance & Layouts -> Theme -> Matieral Dark.


Make some other customizations
------------------------------

Set the default ringtone, notification and alarm sounds.

Battery -> Battery percentage ON

System -> Date & time -> Use 24-hour format ON

Configure the icons that show on the status bar pull-down.  Turn off location,
NFC, Bluetooth.

Set the warning and limit values for the mobile data usage and adjust your
billing cycle period.


Install F-Droid and apps
------------------------

Visit https://f-droid.org then download and install the F-Droid app.

Install the following apps:

* Barcode Scanner
* FFUpdater (to automatically yank down Firefox/Fennec apk)
* FreeOTP or FreeOTP+ (to handle TOTP stuff since KeePassDroid doesn't)
* K-9 Mail
* KeePassDroid
* OpenKeychain (to handle encrypted/signed emails)
* OsmAnd+ (for navigation goodness)


Downloading maps for Osmand
---------------------------

The in-app download function seems to be horribly slow.  Visit
https://download.osmand.net/list.php and fetch your desired maps.  You may then
connect for a USB file transfer and load these .obf files directly into the
osmand folder on your phone.


Configure K-9 Mail
------------------

Fill in the settings you obtained from your email admin/provider.

Global Settings:
  Display:
    Theme:  Dark
    Animation:  Do not use gaudy visual effects
    Show stars:  Off
    Multi-select checkboxes:  On
    Show correspondent names:  Off
    Correspondent above subject:  On
    Show contact pictures:  Off
  Interaction:
    Return to list after delete:  Off
  Notifications:
    Show Delete button:  Always
  Cryptography:
    OpenPGP app:  OpenKeychain
Account Settings:
  Fetching mail:
    Local folder size:  all messages
    Fetch messages up to:  any size (no limit)
    Folder poll frequency:  Every hour
    Poll folders:  All
    Push folders:  All
  Sending mail:
    Composition defaults:
      Use Signature:  Off
    Message Format:  Plain Text (remove images and formatting)
  Folders:
    Archive folder:  -NONE-
  Notifications:
    Vibrate:  On
    Blink LED:  On


Configure Firefox
-----------------

Set Firefox as default browser
Search
  DuckDuckGo:  Default
  Delete all other engines
  Show search history:  Off
Privacy
  Do not track ON
  Tracking protection:  Enabled
  Cookies:  Enabled, excluding 3rd party
  Clear private data on exit:  Select all
  Remember logins:  Off
  Crash Reporter:  Off
  Firefox Health Report:  Off
Notifications -> Product and feature tips OFF
