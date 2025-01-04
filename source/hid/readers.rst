New Kobo Stuff
--------------

::

    $ cat .kobo/Kobo/Kobo\ eReader.conf
    [ApplicationPreferences]
    # ...
    SideloadedMode=true

::

    $ mkdir .kobo/screensaver
    # 1440x1920 px images in PNG or JPEG or GIF format

* https://www.reddit.com/r/kobo/comments/1dl6hym/libra_colour_how_to_bypass_registration
* https://code.mendhak.com/kobo-customizations
* https://github.com/koreader/koreader
* https://github.com/koreader/koreader/wiki/Installation-on-Kobo-devices
* https://koreader.rocks/user_guide
* https://github.com/NiLuJe/kfmon
* https://github.com/pgaskin/NickelMenu
* https://pgaskin.net/NickelMenu
* https://pgaskin.net/KoboStuff/kobofirmware.html
* https://www.mobileread.com/forums/showthread.php?t=295612  list of Kobo hacks and utilities
* https://www.mobileread.com/forums/showthread.php?t=274231  Kute File Monitor (KFM) for Kobo
* https://www.mobileread.com/forums/showthread.php?t=314220  One-Click Packages (OCP) for Kobo and a helpful install.sh script
* https://github.com/olup/kobowriter


Old Kobo Stuff
--------------

::

    127.0.0.1 host localhost.localdomain localhost localhost localhost.localdomain
    127.0.0.1 www.google-analytics.com ssl.google-analytics.com google-analytics.com

::

    cd KOBOeReader/.kobo
    sqlite3 KoboReader.sqlite
    INSERT INTO user VALUES ('', '', '', '', '', '', '', '', '', '', '', '', '');
    .quit

    -- slightly different instruction found somewhere else
    INSERT INTO user (UserID, UserKey) VALUES ('1', '');

::

    ebook-convert dummy.html .epub
