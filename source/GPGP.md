# GPG/PGP Magic

* <https://musigma.blog/2021/05/09/gpg-ssh-ed25519.html> SSH and GPG with the same private key???
* <https://serverfault.com/questions/887769/export-private-ed25519-key-from-gnupg-for-use-in-ssh>
* <https://rgoulter.com/blog/posts/programming/2022-06-10-a-visual-explanation-of-gpg-subkeys.html>
* <https://yanhan.github.io/posts/2014-03-04-gpg-how-to-trust-imported-key>
* <https://g-loaded.eu/2010/11/01/change-expiration-date-gpg-key>
* <https://gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html>
* <https://latacora.micro.blog/2019/07/16/the-pgp-problem.html> the worst parts about GPG/PGP!!!
* <https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key>
* <https://stackoverflow.com/questions/56582016/gpg-change-passphrase-non-interactively>
* <https://superuser.com/questions/1478615/extend-the-expiration-date-of-a-gpg-key-non-interactively>

    # Sigh... macOS...
    $ export GPG_TTY=$(tty)

    $ gpg --quick-gen-key 'Bubba Smith (Wangdoodle) <bubba.smith@example.com>' \
        --batch --pinentry loopback --passphrase '' \
            ed25519 cert 3y
    $ gpg -k --with-colons  # get the KEY_ID... tbd
    $ gpg --quick-add-key ${KEY_ID} \
        --batch --pinentry loopback --passphrase '' \
            ed25519 auth 3y
    $ gpg --quick-add-key ${KEY_ID} \
        --batch --pinentry loopback --passphrase '' \
            ed25519 sign 3y
    $ gpg --quick-add-key ${KEY_ID} \
        --batch --pinentry loopback --passphrase '' \
            cv25519 encr 3y

    # List everything
    $ gpg -k  # equivalent to "gpg --list-keys"
    $ gpg -K  # equivalent to "gpg --list-secret-keys"

    # Show extra info
    $ gpg -k --with-keygrip --with-subkey-fingerprint
    $ gpg -K --with-keygrip --with-subkey-fingerprint
    $ ls ~/.gnupg/private-keys-v1.d
    ...
    $ echo "with-keygrip" >> ~/.gnupg/gpg.conf
    $ echo "with-subkey-fingerprint" >> ~/.gnupg/gpg.conf

    # Change the expiry on things???
    $ gpg --edit-key ${KEY_ID}
    > expire
    ...
    > save

    $ gpg --quick-set-expire ${KEY_ID} 5y ${SUBKEY_ID}

    # Trust things after importing them from backups???
    $ gpg --edit-key ${KEY_ID}
    > trust
    > 5
    > save

    # SSH key magic??? (the "auth" subkey and definitely not the cv25519 one)
    $ for i in $(gpg -k | grep ub | grep -v ring | cut -d '/' -f2 | cut -d ' ' -f1); do
        gpg --export-ssh-key $i\!; done


# Backups

* <https://saminiir.com/paper-storage-and-recovery-of-gpg-keys>
* <https://wiki.archlinux.org/title/Paperkey> can't backup public keys
* <https://jabberwocky.com/software/paperkey> can't backup public keys
* <https://github.com/dmshaw/paperkey> can't backup public keys
* <https://github.com/volution/punchcard-key-backup>
* <https://docs.python.org/3/library/binascii.html#binascii.crc_hqx> Python CRC-CCITT CRC-16/XMODEM function
* <https://beebwiki.mdfs.net/CRC-16> C CRC-CCITT CRC-16/XMODEM function
* <https://www.monperrus.net/martin/store-data-paper> (mandatory 'www' here)
* <https://www.monperrus.net/martin/perfect-ocr-digital-data> (mandatory 'www' here)
* <https://qr.blinry.org> reading QR codes without a computer
* <https://ronja.twibright.com/optar> another barcode thing
* <https://github.com/colindean/optar> another barcode thing

    # Export stuff for safe-keeping??? (Don't forget the revcert too!!!)
    $ umask 0077 ; gpg --armor --export-secret-key ${KEY_ID} > foo.gpg.priv.asc
    $ umask 0022 ; gpg --armor --export ${KEY_ID} > foo.gpg.pub.asc
    $ if [ $(stat -c %s foo.gpg.pub.asc) -eq 0 ]; then rm foo.gpg.pub.asc ; fi
    $ if [ $(stat -c %s foo.gpg.priv.asc) -eq 0 ]; then rm foo.gpg.priv.asc ; fi
    $ gpg --armor --export-secret-subkeys ${SUBKEY_ID}\!
    # ...

    # Packets containing 3 subkeys
    $ gpg --export ${KEY_ID} | gpgsplit --prefix "p-${KEY_ID}-"
    $ gpg --export-secret-key ${KEY_ID} | gpgsplit --prefix "s-${KEY_ID}-"
    $ ls -1 *000*
    p-foo-000001-006.public_key
    p-foo-000002-013.user_id
    p-foo-000003-002.sig
    p-foo-000004-014.public_subkey
    p-foo-000005-002.sig
    p-foo-000006-014.public_subkey
    p-foo-000007-002.sig
    p-foo-000008-014.public_subkey
    p-foo-000009-002.sig
    s-foo-000001-005.secret_key
    s-foo-000002-013.user_id
    s-foo-000003-002.sig
    s-foo-000004-007.secret_subkey
    s-foo-000005-002.sig
    s-foo-000006-007.secret_subkey
    s-foo-000007-002.sig
    s-foo-000008-007.secret_subkey
    s-foo-000009-002.sig

    # View the actual contents of the packets
    $ for i in *000* ; do echo ; pgpdump -i $i ; echo ; done


# SSH

* <https://goral.net.pl/post/use-gpg-for-ssh-keys> overview but missing the SSH private key file
* <https://github.com/pinpox/pgp2ssh> actually get a working SSH private key file (tool works but is very cumbersome to use)
* <https://github.com/ProtonMail/go-crypto> dependency of pgp2ssh
* <https://github.com/ProtonMail/gopenpgp> probably a better choice than go-crypto

    # First, ensure you have a key with 'auth' capability
    $ gpg --export-ssh-key ${KEY_ID}  # just get the ssh pub key

    # Get the SSH private key
    $ gpg --armor --export-secret-key ${KEY_ID} > foo.txt
    $ git clone https://github.com/pinpox/pgp2ssh ; cd pgp2ssh ; go build . ; mv pgp2ssh .. ; cd ..
    $ ./pgp2ssh 2>&1 | (umask 0077 && tee bar.txt)
    $ # manually fix the resulting file
    $ rm foo.txt  # get rid of the temporary key export file

    # Compare the private key file contents you just extracted to what comes directly from GPG
    $ gpg --export-ssh-key ${KEY_ID}
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICQ1fY/xz1aoP1MMqLGmB7J4iOh2Qx27268mD2Y6HP8s openpgp:0xCA299433
    $ ssh-keygen -f bar.txt -y
    ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAICQ1fY/xz1aoP1MMqLGmB7J4iOh2Qx27268mD2Y6HP8s


# Commit Signing

* <https://git-scm.com/book/tr/v2/Git-Tools-Signing-Your-Work>
* <https://help.gitkraken.com/gitkraken-client/commit-signing-with-gpg>
* <https://confluence.atlassian.com/sourcetreekb/setup-gpg-to-sign-commits-within-sourcetree-765397791.html>


# Key Discovery

* <https://gist.github.com/kafene/0a6e259996862d35845784e6e5dbfc79>


# Other ED25519 Stuff

You must have LibreSSL 3.7.x+ (or any old OpenSSL 1.1+???) to use
ED25519!

    openssl genpkey -algorithm ed25519 > priv
    openssl pkey -in priv -out pub -pubout

* <https://slsa.dev/provenance/v0.2> needs in-toto
* <https://github.com/in-toto/in-toto> in-toto-keygen (pip install in-toto pynacl; see below for why)
* <https://stackoverflow.com/questions/72981536/sign-a-text-with-pynacl-ed25519-importing-a-private-key>
* <https://github.com/in-toto/in-toto-golang> not quite ready for prime-time yet!!!
* <https://github.com/mikalv/anything2ed25519>
* <https://0xcc.re/2022/02/01/dangerous-toys-anything-to-ed25519-ssh-keys.html>


# Key Servers

* <https://keys.openpgp.org>
* <https://keys.openpgp.org/about/api>
* <https://keys.openpgp.org/search?q=0x3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C>
* <https://keys.openpgp.org/vks/v1/by-fingerprint/3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C>


# Golang

* <https://github.com/golang/go/issues/44226> deprecated library!!!
* <https://github.com/ProtonMail/gopenpgp> possible replacement library
* <https://pkg.go.dev/github.com/ProtonMail/gopenpgp/v2> docs for possible replacement library
* <https://asecuritysite.com/age> go examples
* <https://github.com/yeqown/go-qrcode>
* <https://github.com/gokyle> some other nifty ideas for tiny Go tools


# X.509 Stuff

* <https://github.com/kisom/cert> nifty Go CLI tool for dealing with cert stuff
