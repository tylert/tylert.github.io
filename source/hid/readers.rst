New Kobo Stuff
--------------

::

    $ cat .kobo/Kobo/Kobo\ eReader.conf  # or KoboReader.conf
    [ApplicationPreferences]
    # ...
    SideloadedMode=true

::

    $ mkdir .kobo/screensaver
    # 1264x1680 optimal for B&W images, 632x840 for colour

* https://www.reddit.com/r/kobo/comments/1dl6hym/libra_colour_how_to_bypass_registration
* https://code.mendhak.com/kobo-customizations
* https://github.com/koreader/koreader
* https://koreader.rocks/user_guide
* https://github.com/pgaskin/NickelMenu
* https://pgaskin.net/NickelMenu
* https://pgaskin.net/KoboStuff/kobofirmware.html


Old Kobo Stuff
--------------

::

    127.0.0.1 host localhost.localdomain localhost localhost localhost.localdomain
    127.0.0.1 www.google-analytics.com ssl.google-analytics.com google-analytics.com

::

    cd KOBOeReader/.kobo
    sqlite3 KoboReader.sqlite
    INSERT INTO user VALUES('', '', '', '', '', '', '', '', '', '', '', '', '');
    .quit

    -- slightly different instruction found somewhere else
    INSERT INTO user(UserID,UserKey) VALUES('1','');

::

    ebook-convert dummy.html .epub

* https://github.com/olup/kobowriter
