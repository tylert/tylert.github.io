Upgrade Preparations
--------------------

#. Completely update your phone to the latest official Android load first.
#. Make sure you backup all local data on your phone, if applicable (DCIM, Ringtones, Downloads, etc.).
#. Use "Settings", go to "About phone", tap "Build number" 7 times.
#. Use "Settings", go to "System -> Advanced -> Developer options", enable "Android debugging" (ADB USB debugging).
#. Use "Settings", go to "System -> Advanced -> Developer options", enable "OEM unlocking";  May require stupidity like `adb shell pm uninstall --user 0 com.android.phone`, reboot after changing this.
#. Follow all installation instructions for your chosen Android load (e.g.:  LineageOS, /e/, etc.).
#. Reboot into the new system when you're finished with all the installation steps.


Factory-Fresh Setup
-------------------

#. At the welcome screen, hit "NEXT".
#. At "Language", select "English (Canada)", hit "NEXT".
#. At "Date and Time", select your timezone ("Eastern Time GMT-4:00"), hit "NEXT".
#. At "Wi-Fi", turn off "Open network notification", connect to your Wi-Fi accesspoint, hit "NEXT".
#. At "Turn on cellular data", enable your service provider, hit "NEXT".
#. At "Location services", tick "Allow apps that have asked your permission", hit "NEXT".
#. At "LineageOS features", untick "Help improve LineageOS", hit "NEXT".
#. At "Fingerprint setup", hit "SKIP".
#. At "Protect your phone", hit "SET UP", choose PIN, enter it twice, hit "NEXT".
#. At the final screen, hit "START".
#. Acknowledge the "Discover Trust" notification, hit "GOT IT".
#. Use "Settings", go to "About phone", tap "Build number" 7 times.
#. Use "Settings", go to "System -> Advanced -> Developer options", enable "Android debugging" (ADB USB debugging).


Install F-Droid and Other Apps
------------------------------

#. Use "Browser", visit https://f-droid.org, download and install F-Droid app after allowing "Browser" to acces photos and media on this device and allow install unknown apps permission.
#. Use "Files", complete the installation of "F-Droid".
#. Use "Settings", revoke permission for "Browser" to install unknown apps.
#. Use "Files", delete the downloaded copy of the F-Droid app.
#. Use "F-Droid", install the following apps after allowing F-Droid to install apps from unknown sources:
  * "FFUpdater"
  * "Locker"
  * "K-9 Mail"
  * "KeePassDX"
  * "Maps and GPS Navigation OsmAnd+"
#. Use "Locker", toggle "Admin enabled", accept the permission request and set it to Enable after 5 attempts.
#. Use "FFUpdater", hit "+", select "Firefox Browser", allow access photos and media and allow install apps from unknown sources.
#. Use "OsmAnd+", download "World overview map" and "Ontario Standard map.
#. Remove all the junk from your home screen and move your icons around as desired.


Configure Firefox
-----------------

::

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


Configure K-9 Mail
------------------

Fill in the settings you obtained from your email admin/provider.

::

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
        Return to list after delete:  On
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
        Advanced:
          Max folders to check with push:  50 folders
      Sending mail:
        Composition defaults:
          Use Signature:  Off
        Message Format:  Plain Text (remove images and formatting)
      Folders:
        Folders to display:  All
        Move/copy destination folders:  All
        Folders to search:  All
        Archive folder:  -NONE-
      Notifications:
        Vibrate:  On
        Blink LED:  On


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

Battery -> Battery percentage "Next to the icon".

System -> Date & time -> Use 24-hour format ON

Configure the icons that show on the status bar pull-down.  Turn off location,
NFC, Bluetooth.

Set the warning and limit values for the mobile data usage and adjust your
billing cycle period.
