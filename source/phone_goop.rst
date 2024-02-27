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
  * "FFUpdater" Firefox downloader
  * "K-9 Mail" email client
  * "KeePassDX" password manager
  * "Libera" document reader thingy
#. Use "FFUpdater", hit "+", select "Firefox Browser", allow access photos and media and allow install apps from unknown sources.
#. Remove all the junk from your home screen and move your icons around as desired.
#. (Optional) Use "F-Droid", install the following additional apps:
  * "Syncopoli" for auto-syncing photos
  * "WireGuard" for pushing photos

::

    # Add repo to F-Droid
    https://apt.izzysoft.de/fdroid/repo
    # Then you can install stuff like "osmin"


Configure Firefox
-----------------

::

    Search:  select DuckDuckGo, delete the rest of the engines
      Autocomplete URLs:  Off
      Show clipboard suggestions:  Off
      Search browsing history:  Off
      Search bookmarks:  Off
      Show search suggestions:  Off
    Customize:
      Toolbar:  Top
      Show most visited sites:  Off
    Logins and passwords:
      Save logins and passwords:  Never save
      Autofill:  Off
    Set as default browser:  On
    Private browsing:
      Open links in a private tab:  On
      Allow screenshots in private browsing:  On
    Delete browsing data on quit:  On, select all types
    Data collection:
      Usage and technical data:  Off
      Marketing data:  Off
      Experiments:  Off


Configure K-9 Mail
------------------

Fill in the settings you obtained from your email admin/provider and configure
the settings for the app as follows:

::

    General Settings:
      Display:
        Animation:  Disable Use gaudy visual effects
        Show stars:  Off
        Show correspondent names:  Off
        Show contact pictures:  Off
        Visible message actions: Delete, Move
      Interaction:
        Return to list after delete:  On
    Account Settings:
      Fetching mail:
        Local folder size:  all messages
        Fetch messages up to:  any size (no limit)
        Folder poll frequency:  Every hour
        Poll folders:  All
        Push folders:  All
        Advanced:
          Max folders to check with push:  1000 folders
      Sending mail:
        Composition defaults:
          Use Signature:  Off
        Message Format:  Plain Text (remove images and formatting)
      Folders:
        Folders to display:  All
        Move/copy destination folders:  All
        Archive folder:  -NONE-
        Drafts folder:  Drafts
        Sent folder:  Sent
        Spam folder:  Junk
        Trash folder:  Trash
      Notifications:
        Vibration:  Enabled, Vibration pattern = Default, Pattern 1, Repeat vibration 2
        Notification light:  Account colour


Make the keyboard less annoying
-------------------------------

Under Sound turn off all the other sounds and vibrations.

Under System -> Languages & input -> Virtual keyboard -> Android Keyboard
(AOSP) -> Preferences turn off Auto-capitalisation, Double-space full stop and
Vibrate on keypress Then go under Text correction and turn off everything.
Also set the Appearance & Layouts -> Theme -> Material Dark.


Make some other customizations
------------------------------

Set the default ringtone, notification and alarm sounds.

Battery -> Battery percentage "Next to the icon".

System -> Date & time -> Use 24-hour format ON

Configure the icons that show on the status bar pull-down.  Turn off location,
NFC, Bluetooth.  Set bluetooth device name.  Set hostname in Developer Options
too.

Set the warning and limit values for the mobile data usage and adjust your
billing cycle period.


Evict Obstinate System Apps
---------------------------

::

    # adb shell
    # pm list packages -3  # only show 3rd-party apps (non-system)
    # pm list packages -d  # only show disabled apps
    # pm list packages -e  # only show enabled apps
    # pm list packages -s  # only show system apps

    packages='
    com.android.chrome
    com.coloros.childrenspace
    com.coloros.weather.service
    com.google.android.apps.googleassistant
    com.google.android.apps.magazines
    com.google.android.apps.maps
    com.google.android.apps.nbu.files
    com.google.android.apps.photos
    com.google.android.apps.podcasts
    com.google.android.apps.restore
    com.google.android.apps.tachyon
    com.google.android.apps.walletnfcrel
    com.google.android.apps.youtube.music
    com.google.android.calendar
    com.google.android.feedback
    com.google.android.gm
    com.google.android.googlequicksearchbox
    com.google.android.videos
    com.google.android.wellbeing
    com.google.android.youtube
    com.google.ar.lens
    com.heytap.accessory
    com.netflix.mediaclient
    com.netflix.partner.activation
    com.oneplus.membership
    com.oneplus.store
    com.oplus.customize.coreapp
    com.oplus.games
    com.oplus.omoji
    com.qti.qcc
    net.oneplus.forums
    net.oneplus.weather
    '
    for package in ${packages}; do
        pm uninstall --user 0 ${package}
    done


Others
------

* https://rugu.dev/en/blog/debloat-with-adb
* https://github.com/janbar/osmin
* https://apt.izzysoft.de/fdroid  osmin app
* http://download.openstreetmap.fr/extracts  maps for osmin
* https://opensource.com/article/20/12/android-auto-open-source
* https://www.reddit.com/r/fossdroid/comments/fh5jcr/foss_alternative_to_connect_to_android_auto
* https://github.com/tomasz-grobelny/AACS
* http://rafalgolarz.com/blog/2017/01/15/running_golang_on_android
