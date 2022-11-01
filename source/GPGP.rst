GNU Privacy Guard Magic
-----------------------

* https://musigma.blog/2021/05/09/gpg-ssh-ed25519.html  SSH and GPG with the same private key???
* https://www.digitalneanderthal.com/post/gpg/  better/paper backups???
* https://serverfault.com/questions/887769/export-private-ed25519-key-from-gnupg-for-use-in-ssh
* https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html
* https://yanhan.github.io/posts/2014-03-04-gpg-how-to-trust-imported-key/
* https://www.g-loaded.eu/2010/11/01/change-expiration-date-gpg-key/
* https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html
* https://latacora.micro.blog/2019/07/16/the-pgp-problem.html  the worst parts about GPG/PGP!!!

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

    # List everything
    $ gpg -k  # equivalent to "gpg --list-keys"
    $ gpg -K  # equivalent to "gpg --list-secret-keys"

    # Show extra info
    $ gpg -k --with-keygrip --keyid-format long
    $ gpg -K --with-keygrip --keyid-format long
    $ ls .gnupg/private-keys-v1.d/
    $ echo "keyid-format long" >> ~/.gnupg/gpg.conf

    # Change the expiry on things???
    $ gpg --edit-key ${KEY_ID}
    > expire
    ...
    > save

    # Trust things after importing it???
    $ gpg --edit-key ${KEY_ID}
    > trust
    > 5
    > save

    # Export stuff for safe-keeping???
    $ umask 0077 ; gpg --armor --export-secret-key ${KEY_ID} > foop.gpg.priv.asc
    $ umask 0022 ; gpg --armor --export ${KEY_ID} > foop.gpg.pub.asc
    $ if [ $(stat -c %s foop.gpg.pub.asc) -eq 0 ]; then rm foop.gpg.pub.asc ; fi
    $ if [ $(stat -c %s foop.gpg.priv.asc) -eq 0 ]; then rm foop.gpg.priv.asc ; fi
    $ gpg --armor --export-secret-subkeys ${SUBKEY_ID}\!
    # ...

    # SSH key magic??? (the "auth" subkey and definitely not the cv25519 one)
    $ for i in $(gpg -k | grep ub | grep -v ring | cut -d '/' -f2 | cut -d ' ' -f1); do
        gpg --export-ssh-key $i\!; done
