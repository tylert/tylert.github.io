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
* https://www.reddit.com/r/kobo/comments/117zz25/kobo_sage_what_are_these_side_contacts_for
* https://help.kobo.com/hc/en-us/articles/4406292782615-Using-your-Kobo-Sage-PowerCover  PowerCover stuff
* https://www.mobileread.com/forums/showthread.php?t=358080&nojs=1  PowerCover stuff


Broken SSH
----------

* https://github.com/koreader/koreader/wiki/SSH
* https://github.com/koreader/koreader/issues/8370
* https://github.com/koreader/koreader/issues/11698
* https://www.mobileread.com/forums/showthread.php?t=254214
* https://forum.openwrt.org/t/solved-dropbear-and-ed25519-keys-resolved-in-21-02/23539/4  ED25519 support was merged upstream in 2020
* https://github.com/denysvitali/lightsshd  Go SSH server?


Other
-----

* https://takov751.gitlab.io/posts/project_kobodeck  building a Golang application to run on a Kobo?
* https://letsdecentralize.org/tutorials/kobo-terminal.html  browsing Gemini sites on a Kobo?


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
