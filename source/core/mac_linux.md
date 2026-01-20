# Mac become: Linux

* <https://neilzone.co.uk/2021/07/wi-fi-on-a-2012-mac-mini-running-debian-11>
* <https://kapware.com/blog/repurpose-mac-mini>
* <https://github.com/t2linux/T2-Mint/issues/9> built-in audio might be a lost cause
* <https://asahilinux.org>
* <https://t2linux.org>
* <https://ravynos.com>
* <https://github.com/ravynsoft/ravynos>

    # Get WiFi working again (Debian on Macmini6,1)
    apt install broadcom-sta-dkms

    # Get HP printer working (Debian)
    apt install hplip

    # Get printing working (Debian)
    for user in ${users}; do
        usermod -a -G lp ${user}
    done
