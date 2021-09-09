Debian 11 Install
=================


Partitions
----------

1 MB unused guard partition (GPT)
256 MB vfat ESP bootable
512 MB btrfs for boot at /boot
rest of drive for crypt with LVM inside
  17 GB (RAM + 1 GB) swap for vg0-swap
  100 GB btrfs for vg0-root at /
  rest of space btrfs for vg0-home at /home


Aftwerwards
-----------

add "contrib non-free" to sources

install the following to appease the robots:
  firmware-iwlwifi
  firmware-misc-nonfree
  intel-microcode

install the following to appease humans:
  ditaa
  git
  gitk
  myrepos
  rename
  rsync
  vim-gtk3
  wireguard


Python
------

* https://realpython.com/intro-to-pyenv/

install dependencies for working with pyenv:
  build-essential
  curl
  libbz2-dev
  libffi-dev
  liblzma-dev
  libncurses5-dev
  libncursesw5-dev
  libreadline-dev
  libsqlite3-dev
  libssl-dev
  llvm
  make
  tk-dev
  wget
  xz-utils
  zlib1g-dev

curl https://pyenv.run | bash


Zoom
----

Install the Zoom package and then "apt --fix-broken install" (:facepalm:).


Bugs
----

Error in the "Software" program::

    Unable to get list of updates:
    Failed to update metadata for lvfs: checksum failure: failed to verify data, expected ababababababababababa...

Remove the error in "Software" program by typing::

    fwupdmgr --force refresh
