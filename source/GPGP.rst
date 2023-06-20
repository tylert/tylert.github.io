GPG/PGP Magic
-------------

* https://musigma.blog/2021/05/09/gpg-ssh-ed25519.html  SSH and GPG with the same private key???
* https://www.digitalneanderthal.com/post/gpg/  better/paper backups???
* https://serverfault.com/questions/887769/export-private-ed25519-key-from-gnupg-for-use-in-ssh
* https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html
* https://yanhan.github.io/posts/2014-03-04-gpg-how-to-trust-imported-key/
* https://www.g-loaded.eu/2010/11/01/change-expiration-date-gpg-key/
* https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html
* https://latacora.micro.blog/2019/07/16/the-pgp-problem.html  the worst parts about GPG/PGP!!!
* https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key/

::

    # Use a recent version!!!
    $ gpg --version
    gpg (GnuPG) 2.3.8
    ...

    # Definitely need this on macOS!!!
    $ export GPG_TTY=$(tty)

    # Do the key gen thing less interactively and with a better setup???
    $ gpg --quick-gen-key 'Bubba Smith (Wangdoodle) <bubba.smith@example.com>' \
        ed25519 cert 10y
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
    ...
    $ echo "keyid-format long" >> ~/.gnupg/gpg.conf
    $ echo "with-keygrip" >> ~/.gnupg/gpg.conf

    # Change the expiry on things???
    $ gpg --edit-key ${KEY_ID}
    > expire
    ...
    > save

    # Trust things after importing them from backups???
    $ gpg --edit-key ${KEY_ID}
    > trust
    > 5
    > save

    # SSH key magic??? (the "auth" subkey and definitely not the cv25519 one)
    $ for i in $(gpg -k | grep ub | grep -v ring | cut -d '/' -f2 | cut -d ' ' -f1); do
        gpg --export-ssh-key $i\!; done


Backups
-------

* https://www.saminiir.com/paper-storage-and-recovery-of-gpg-keys/
* https://wiki.archlinux.org/title/Paperkey
* https://www.jabberwocky.com/software/paperkey/
* https://github.com/dmshaw/paperkey/

::

    # Export stuff for safe-keeping???
    $ umask 0077 ; gpg --armor --export-secret-key ${KEY_ID} > foop.gpg.priv.asc
    $ umask 0022 ; gpg --armor --export ${KEY_ID} > foop.gpg.pub.asc
    $ if [ $(stat -c %s foop.gpg.pub.asc) -eq 0 ]; then rm foop.gpg.pub.asc ; fi
    $ if [ $(stat -c %s foop.gpg.priv.asc) -eq 0 ]; then rm foop.gpg.priv.asc ; fi
    $ gpg --armor --export-secret-subkeys ${SUBKEY_ID}\!
    # ...

    $ gpg --export foo | gpgsplit
    $ ls -1 000*
    000001-006.public_key
    000002-013.user_id
    000003-002.sig
    000004-014.public_subkey
    000005-002.sig
    000006-014.public_subkey
    000007-002.sig
    000008-014.public_subkey
    000009-002.sig
    $ rm 000*
    $ gpg --export-secret-key | gpgsplit
    $ ls -1 000*
    000001-005.secret_key
    000002-013.user_id
    000003-002.sig
    000004-007.secret_subkey
    000005-002.sig
    000006-007.secret_subkey
    000007-002.sig
    000008-007.secret_subkey
    000009-002.sig
    $ rm 000*


Commit Signing
--------------

* https://git-scm.com/book/tr/v2/Git-Tools-Signing-Your-Work
* https://help.gitkraken.com/gitkraken-client/commit-signing-with-gpg/
* https://confluence.atlassian.com/sourcetreekb/setup-gpg-to-sign-commits-within-sourcetree-765397791.html


Key Discovery
-------------

* https://gist.github.com/kafene/0a6e259996862d35845784e6e5dbfc79


Other ED25519 Stuff
-------------------

You must have LibreSSL 3.7.x+ (or any old OpenSSL 1.1+???) to use ED25519!

::

    openssl genpkey -algorithm ed25519 > priv
    openssl pkey -in priv -out pub -pubout

* https://slsa.dev/provenance/v0.2  needs in-toto
* https://github.com/in-toto/in-toto  in-toto-keygen (pip install in-toto pynacl;  see below for why)
* https://stackoverflow.com/questions/72981536/sign-a-text-with-pynacl-ed25519-importing-a-private-key
* https://github.com/in-toto/in-toto-golang  not quite ready for prime-time yet!!!
* https://github.com/mikalv/anything2ed25519
* https://0xcc.re/2022/02/01/dangerous-toys-anything-to-ed25519-ssh-keys.html


Key Servers
-----------

* https://keys.openpgp.org/
* https://keys.openpgp.org/about/api
* https://keys.openpgp.org/search?q=0x3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
* https://keys.openpgp.org/vks/v1/by-fingerprint/3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C


Golang
------

* https://github.com/golang/go/issues/44226  deprecated library!!!
* https://github.com/ProtonMail/gopenpgp  possible replacement library
* https://pkg.go.dev/github.com/ProtonMail/gopenpgp/v2  docs for possible replacement library
