# Diff Tools

- <https://stackoverflow.com/questions/68340820/how-to-set-vscodium-as-git-difftool>
- <https://github.com/will133/vim-dirdiff#vim-dirdiff>
- <https://vi.stackexchange.com/questions/778/how-to-diff-and-merge-two-directories/790#790>


# Binary Goop

- <https://apple.stackexchange.com/questions/429197/how-can-i-distinguish-arm-binaries-from-x86-binaries-on-macos/436911#436911>
- <https://forums.swift.org/t/xtool-cross-platform-xcode-replacement-build-ios-apps-on-linux-and-more/79803>


# Other

- <https://weiyen.net/articles/useful-macos-cmd-line-utilities>
- <https://mac.getutm.app> run VMs on macOS and iOS


# Mac become: Linux

Any Mac mini older than 2014 is considered (by Apple) to be obsolete.  Maybe
Linux can extend the life of these devices.

- <https://neilzone.co.uk/2021/07/wi-fi-on-a-2012-mac-mini-running-debian-11> dual displays and working WiFi on Debian
- <https://ifixit.com/Device/Mac_Mini_Late_2012> how to take things apart and put them back together
- <https://reddit.com/r/linux_on_mac/comments/1hglkvh/any_tips_mac_mini_late_2012> some possible hardware upgrades
- <https://reddit.com/r/technology/comments/1jzzmwj/apple_says_all_mac_minis_with_intel_are_now> how old is too old?
- <https://linuxquestions.org/questions/linux-newbie-8/stopping-a-2011-mac-mini-from-sleeping-with-debian-4175714485> maybe your unit randomly goes to sleep
- <https://kapware.com/blog/repurpose-mac-mini> maybe craft your own boot goop to have WiFi working at installation time
- <https://github.com/t2linux/T2-Mint/issues/9> built-in audio might be a lost cause
- <https://asahilinux.org> Apple silicon can also run Linux if you're stubborn enough
- <https://t2linux.org> Apple silicon can also run Linux if you're stubborn enough
- <https://ravynos.com> future pretty OS that's not quite ready for prime time
- <https://github.com/ravynsoft/ravynos> future pretty OS that's not quite ready for prime time

```
    # Get WiFi working (Debian on Macmini6,1)
    apt-get --yes install broadcom-sta-dkms

    # Get HP printer working (Debian)
    apt-get --yes install hplip

    # Get printing working (Debian)
    for user in ${users}; do
        usermod -a -G lp ${user}
        newgrp lp
    done
```


# Debian Printing Fun

- <https://packages.debian.org/trixie/hplip> dude, you're getting an HP!
- <https://developers.hp.com/hp-linux-imaging-and-printing/supported_devices/index>
