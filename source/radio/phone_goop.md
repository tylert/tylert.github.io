![image](example.png)


# Initial Preparations

1. Completely update your phone to the latest official Android load first.
1. Make sure you backup all local data on your phone, if applicable (contacts, photos, ringtones, downloads, etc.).
1. Use Settings, go to About phone, tap Build number 7 times.
1. Use Settings, go to System - Advanced - Developer options, enable USB debugging.
1. Use Settings, go to System - Advanced - Developer options, enable OEM unlocking; May require stupidity like 'adb shell pm uninstall \-\-user 0 com.android.phone', reboot after changing this.
1. Follow all installation instructions for your chosen Android distribution (e.g.: LineageOS, /e/, etc.).
1. Reboot into the new system when you're finished with all the installation steps.


# Factory-Fresh Setup

1. At the welcome screen, hit NEXT.
1. At Language, select English (Canada), hit NEXT.
1. At Date and Time, select your timezone (Eastern Time GMT-4:00), hit NEXT.
1. At Wi-Fi, turn off Open network notification, connect to your Wi-Fi accesspoint, hit NEXT.
1. At Turn on cellular data, enable your service provider, hit NEXT.
1. At Location services, tick Allow apps that have asked your permission, hit NEXT.
1. At LineageOS features, untick Help improve LineageOS, hit NEXT.
1. At Fingerprint setup, hit SKIP.
1. At Protect your phone, hit SET UP, choose PIN, enter it twice, hit NEXT.
1. At the final screen, hit START.
1. Acknowledge the Discover Trust notification, hit GOT IT.
1. Use Settings, go to About phone, tap Build number 7 times.
1. Use Settings, go to System - Advanced - Developer options, enable USB debugging.


# Install Other Apps

1. Use Browser, visit <https://f-droid.org>, download F-Droid app after allowing Browser to access files and media on this device and allow install unknown apps permission.
1. Use Files, complete the installation of F-Droid.
1. Use Files, delete the downloaded copy of the F-Droid app.
1. Use F-Droid, install the following apps after allowing F-Droid to install apps from unknown sources:
    * FFUpdater Thunderbird/Firefox downloader
    * Termux phone productivity enhancer (termux, termux-api)
1. Use FFUpdater, allow access to files and media and allow install apps from unknown sources, hit + to install:
    * Thunderbird Mail email client
    * Firefox Browser web browser

It is very likely that you will also desire/need some apps from
<https://fossify.org/apps> as well.  Fossify Calendar might be a good choice.


# Thunderbird

Fill in the settings you obtained from your email admin/provider and override
the default settings for the app as follows:

    General Settings:
      Display:
        Animation:  Disable Use gaudy visual effects
        Show stars:  Off
        Show correspondent names:  Off
        Show contact pictures:  Off
        Visible message actions: Delete, Move
    Account Settings:
      Fetching mail:
        Local folder size:  all messages
        Fetch messages up to:  any size (no limit)
        Advanced:
          Max folders to check with push:  1000 folders
      Sending mail:
        Message Format:  Plain Text (remove images and formatting)
      Notifications:
        New mail notifications:  On
        Vibration:  Enabled, Vibration pattern = Default pattern, Repeat vibration 2
        Notification light:  Account colour


# Firefox

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


# Osmin

* <https://apt.izzysoft.de/fdroid/repo>
* <https://github.com/janbar/osmin>
* <https://github.com/janbar/osmin/wiki>
* <http://download.openstreetmap.fr/extracts> more-granular maps for osmin (may have trouble writing to needed location)


# Evict Obstinate System Apps

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


# SSH and Rsync

* <https://gitlab.com/d4rcm4rc/MagiskSSH>
* <https://github.com/topjohnwu/Magisk> SU + other stuff?
* <https://cgoldberg.github.io/posts/android-ssh-server>
* <https://izzyondroid.org/quickstart>
* <https://github.com/tfonteyn/Sshd4a>
* <https://github.com/tfonteyn/Sshd4a/wiki>
* <https://howtos.davidsebek.com/android-rsync-termux.html>
* <https://howtos.davidsebek.com/android-rsync-adb.html>

    # Delete files as they are moved
    rsync --remove-source-files ${rsync_opts} /path/to/src/ /path/to/dest


# Others

* <https://rugu.dev/en/blog/debloat-with-adb>
* <https://opensource.com/article/20/12/android-auto-open-source>
* <https://reddit.com/r/fossdroid/comments/fh5jcr/foss_alternative_to_connect_to_android_auto>
* <https://github.com/tomasz-grobelny/AACS>
* <https://rafalgolarz.com/blog/2017/01/15/running_golang_on_android> termux-go?
* <https://schneier.com/blog/archives/2024/03/surveillance-through-push-notifications.html>
* <https://tycrek.github.io/degoogle>
* <https://github.com/tycrek/degoogle>
* <https://anysoftkeyboard.github.io>
* <https://github.com/NeoApplications/Neo-Store> F-Droid alternative?
* <https://mudkip.me/2024/02/28/Spiritual-Successor-to-the-Google-Nexus-7> tablets still suck
* <https://keyboard.futo.org>
* <https://kevinboone.me/lineageos-degoogled.html> making LineageOS a tiny bit less horrible
* <https://plop.at/en/lineageos.html> backup/restore LineageOS stuff?
* <https://gitlab.com/android_translation_layer/android_translation_layer> Android apps on your Linux workstation
* <https://landley.net/toybox> build Android on Android?
* <https://github.com/landley/toybox> build Android on Android?
* <https://androidauthority.com/run-desktop-linux-apps-on-android-how-to-3586539>
* <https://github.com/zenfyrdev/bootloader-unlock-wall-of-shame>
* <https://gioui.org> Android apps in Go?
* <https://arstechnica.com/gadgets/2025/12/i-switched-to-esim-in-2025-and-i-am-full-of-regret> maybe avoid eSIM as long as possible
* <https://arstechnica.com/gadgets/2025/02/google-plans-to-stop-using-insecure-sms-verification-in-gmail> SMS 2FA


# FFUpdater

* <https://f-droid.org/en/packages/de.marmaro.krt.ffupdater>
* <https://github.com/Tobi823/ffupdater>


# GrapheneOS

* <https://github.com/iAnonymous3000/awesome-grapheneos-guide>
* <https://funnymonkey.com/2025/02/configuring-grapheneos-for-daily-use>
* <https://seprand.github.io/articles/best-user-profile-setup>
* <https://theprivacydad.com/using-android-without-a-google-account> F-Droid, Aurora Store
* <https://designed-cybersecurity.com/tutorial/grapheneos-guide> Organic Maps, Obtainium, etc.
