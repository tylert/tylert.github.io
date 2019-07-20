Debian Buster with FDE and BTRFS
================================

The procedure for installing Debian Buster with snapshot-friendly btrfs currently involves using the "expert mode" installer and doing a few manual steps, namely:

- manually adding the subvolumes and remounting everything appropriately
- manually fixing the /etc/fstab and /etc/crypttab
- manually fixing the /etc/cryptsetup-initramfs/conf-hook file to force CRYPTSETUP=y


Partition Layout
----------------

Assuming /dev/sda, the layout is as follows:

- gpt (first 1 MB unused)
- 512 MB on /dev/sda1 for (bootable) vfat32 ESP UEFI System Partition /boot/efi
- 512 MB on /dev/sda2 for ext4 /boot
- everything else on /dev/sda3 for LUKS dm_crypt volume /dev/mapper/sda3_crypt PV -> LVM2 vg0
  - 32 GB (2x RAM) /dev/mapper/vg0-swap as swap (needs to be at least 1x RAM for hibernate)
  - everything else on /dev/mapper/vg0-bwomp for btrfs


BTRFS Subvolumes
----------------

In order to use snapshot capabilities, you must use subvolumes.

Fixing the partition layout is done just after using the installer's partition setup tool and just before the installation of base packages.

For setting up the partitions, the following shell commands were used::

    btrfs subvol list /target
    btrfs subvol create /target/@
    btrfs subvol create /target/@home
    btrfs subvol create /target/@snapshot
    btrfs subvol list /target
    btrfs subvol get-default /target
    btrfs subvol set-default 257 /target
    umount /target/boot/efi
    umount /target/boot
    rm -rf /target/boot
    rm -rf /target/etc
    rm -rf /target/media
    umount /target
    mount /dev/mapper/vg0-bwomp /target -o subvol=@
    mkdir -p /target/boot
    mkdir -p /target/home
    mkdir -p /target/.snapshot
    mount /dev/sda2 /target/boot
    mkdir -p /target/boot/efi
    mount /dev/sda1 /target/boot/efi
    mount /dev/mapper/vg0-bwomp /target/home -o subvol=@home
    mount /dev/mapper/vg0-bwomp /target/.snapshot -o subvol=@snapshot

This will unmount the existing btrfs partition, clean up the root of the volume and create the new subvolumes.


Fstab and Crypttab
------------------

Use the output of blkid to obtain the UUIDs used for the folowing files.

The tool "update-initramfs -k all -c" is used to forcibly-regenerate initramfses provided your /boot is appropriately-mounted first.

/etc/crypttab::

    sda3_crypt UUID=badcabba-6efe-edca-bb1e-5532da8a018f none luks

/etc/fstab::

    UUID=ABCD-1234 /boot/efi vfat umask=0077 0 1
    UUID=decafc0f-feed-eadb-eef0-465f04cb1254 /boot ext4 defaults 0 2
    /dev/mapper/vg0-swap none swap sw 0 0
    /dev/mapper/vg0-bwomp / btrfs defaults,subvol=@ 0 1
    /dev/mapper/vg0-bwomp /home btrfs defaults,subvol=@home 0 1
    /dev/mapper/vg0-bwomp /.snapshot btrfs defaults,subvol=@snapshot 0 1

/etc/cryptsetup-initramfs/conf-hook::

    CRYPTSETUP=y
