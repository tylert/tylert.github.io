GNU Privacy Guard Magic
-----------------------

* https://musigma.blog/2021/05/09/gpg-ssh-ed25519.html  SSH and GPG with the same private key???
* https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html
* https://yanhan.github.io/posts/2014-03-04-gpg-how-to-trust-imported-key/
* https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html
* https://www.g-loaded.eu/2010/11/01/change-expiration-date-gpg-key/
* https://www.digitalneanderthal.com/post/gpg/  better backups???

::

    $ gpg --version
    gpg (GnuPG) 2.3.8
    ...

    # Might need this on macOS
    $ export GPG_TTY=$(tty)

    # Creating a new set of thingies using the defaults
    $ gpg --full-generate-key (sign/cert key 1y + encr sub-key)

    # Do the key gen thing less interactively and with a better setup???
    $ gpg --quick-gen-key 'Bubba Smith (Wangdoodle) <bubba.smith@example.com>' \
        ed25519 cert 5y
    $ gpg --quick-add-key ${KEY_ID} ed25519 auth 1y
    $ gpg --quick-add-key ${KEY_ID} ed25519 sign 1y
    $ gpg --quick-add-key ${KEY_ID} cv25519 encr 1y

    # Change the expiry on things???
    $ gpg --edit-key ${KEY_ID}
    > expire
    ...
    > save

    # Export stuff for safe-keeping???
    $ umask 0077 ; gpg --export-secret-key --armor ${KEY_ID} > foop.gpg.priv.asc
    $ umask 0022 ; gpg --export --armor ${KEY_ID} > foop.gpg.pub.asc
    $ if [ $(stat -c %s foop.gpg.pub.asc) -eq 0 ]; then rm foop.gpg.pub.asc ; fi
    $ if [ $(stat -c %s foop.gpg.priv.asc) -eq 0 ]; then rm foop.gpg.priv.asc ; fi

    # Trust things after import???
    $ gpg --edit-key ${KEY_ID}
    > trust
    > 5
    > save
