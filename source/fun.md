# Containers

* <https://abe-winter.github.io/blues/2017/04/27/config-vs-containers.html>
* <https://github.com/hobby-kube/guide>
* <https://iximiuz.com/en/posts/from-docker-container-to-bootable-linux-disk-image>
* <https://grahamc.com/blog/nix-and-layered-docker-images>
* <https://git.sr.ht/~bitfehler/notariat> TLS manager ACME thingy for k8s

    docker rmi $(docker images --filter "reference=myregistry.example.com/*" --quiet)
    docker rmi $(docker images --filter "dangling=true" --quiet)


# Linux

* <https://blog.alexellis.io/boot-linuxkit-in-10-mins>
* <https://github.com/MichielDerhaeg/build-linux>
* <https://linux-audit.com/using-unattended-upgrades-on-debian-and-ubuntu>
* <https://plop.at/en/bootmanager/full.html> other low-level boot goop?
* <https://anemos.io> build custom initramfs installers
* <https://github.com/liquidmetal-dev/flintlock> containerd-backed micro VMs?
* <https://wiki.debian.org/ThomasChung/CloudImage>
* <https://libguestfs.org>
* <https://cloud.debian.org/images/cloud>
* <https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html>
* <https://asciinema.org/a/132009> debian cloud image demo with cloud-init nocloud
* <https://gist.github.com/wngtk/5c616dc16fd84ac69f14bd5e12a595a8#disk-partition-structure>
* <https://ventoy.net/en/doc_search_path.html> skip entire directories with a .ventoyignore file
* <https://github.com/FlyGoat/csmwrap> BIOS wrapped in fancy-pants UEFI
* <https://dataswamp.org/~solene/2025-05-31-linux-killswitch-on-power-disconnect.html>


# Alpine Linux

* <https://alpinelinux.org>
* <https://wiki.alpinelinux.org/wiki/Setting_up_a_laptop>
* <https://battlepenguin.com/tech/alpine-linux-with-full-disk-encryption>
* <https://whynothugo.nl/journal/2023/11/19/setting-up-an-alpine-linux-workstation>
* <https://github.com/ErikSchlyter/alpine-scripts/blob/master/sys_alpine_with_full_disk_encryption_on_btrfs.md>
* <https://words.filippo.io/dispatches/frood> initramfs Alpine NAS
* <https://whynothugo.nl/journal/2023/11/19/setting-up-an-alpine-linux-workstation>
* <https://willhbr.net/2025/03/09/a-slim-home-server-with-alpine-linux>
* <https://blog.bythewood.me/posts/minimal-automated-updates-for-alpine-linux> Alpine actually provides a way to do automatic upgrades (unlike Arch)
* <https://codentium.com/guides/alpine> Alpine server setup
* <https://wildtechgarden.ca/doc/server-alpine-linux-docs4web> Alpine server setup
* <https://regrow.earth/diy-server/installation> Alpine server setup
* <https://wiki.alpinelinux.org/wiki/Installation> official Alpine install procedure
* <https://wiki.alpinelinux.org/wiki/Uncomplicated_Firewall> ufw on Alpine
* <https://vixalien.com/blog/an-alpine-setup>
* <https://linuxmind.dev/2025/09/02/how-to-install-the-operating-system-alpine-linux>
* <https://krython.com/post/resolving-alpine-linux-installation-errors>
* <https://linuxiac.com/how-to-install-alpine-linux>


# Laptop Distros

* <https://kennethjorgensen.com/blog/2022/encrypted-btrfs-array-with-luks>
* <https://devuan.org>
* <https://artixlinux.org>
* <https://github.com/matleborgne/archlinux-full-disk-encryption>
* <https://github.com/icecmach/artix_installation_guide>


# UEFI

* <https://linuxbabe.com/command-line/how-to-use-linux-efibootmgr-examples>
* <https://github.com/usbarmory/go-boot> UEFI shell unikernel and OS loader
* <https://github.com/usbarmory/tamago> bare metal Go


# Style

* <https://github.com/mvdan/sh>
* <https://github.com/SixArm/unix-shell-script-tactics/blob/main/README.md>


# cloud-init

* <https://stackoverflow.com/questions/23065673/how-to-re-run-cloud-init-without-reboot>
* <https://stackoverflow.com/questions/23151425/how-to-run-cloud-init-manually>
* <https://cloudinit.readthedocs.io/en/latest/topics/modules.html>
* <https://raspberrypi.com/news/cloud-init-on-raspberry-pi-os>


# Python

* <https://sedimental.org/the_packaging_gradient.html>


# 2FA and HSM

* <https://karl-voit.at/2019/03/03/oathtool-otp>
* <https://www.sendthemtomir.com/blog/cli-2-factor-authentication> (mandatory 'www' here)
* <https://blog.snapdragon.cc/2019/04/27/using-a-yubikey-to-secure-ssh-on-macos>
* <https://wiki.debian.org/GNUK>
* <https://blog.danman.eu/2-usb-crypto-token-for-use-with-gpg-and-ssh>
* <https://blog.dan.drown.org/gnuk-open-source-gpg-ssh-hardware-key-storage>
* <https://www.fsij.org/doc-gnuk/index.html> GNUK documentation
* <https://git.gniibe.org/cgit/gnuk/gnuk.git>
* <https://salsa.debian.org/gnuk-team/gnuk/gnuk>
* <https://github.com/ran-sama/stm32-gnuk-usb-smartcard>


# PDF + Contacts

* <https://eventable.github.io/vobject>
* <https://github.com/jszwec/csvutil>
* <https://github.com/JazzCore/python-pdfkit>
* <https://github.com/rst2pdf/rst2pdf/blob/master/rst2pdf/createpdf.py>
* <https://rst2pdf.org/static/manual.html>
* <https://marknagelberg.com/creating-pdf-reports-with-python-pdfkit-and-jinja2-templates>
* <https://en.wikipedia.org/wiki/VCard>
* <https://en.wikipedia.org/wiki/ICalendar>
* <https://datatracker.ietf.org/doc/html/rfc3275> XML
* <https://datatracker.ietf.org/doc/html/rfc4627> JSON
* <https://datatracker.ietf.org/doc/html/rfc5545> iCalendar
* <https://datatracker.ietf.org/doc/html/rfc6321> xCal = XML iCalendar
* <https://datatracker.ietf.org/doc/html/rfc6350> vCard 4.0
* <https://datatracker.ietf.org/doc/html/rfc6351> xCard = XML vCard
* <https://datatracker.ietf.org/doc/html/rfc6868> vCard/iCalendar encodings
* <https://datatracker.ietf.org/doc/html/rfc7095> jCard = JSON vCard
* <https://datatracker.ietf.org/doc/html/rfc7265> jCal = JSON iCalendar
* <https://github.com/emersion/go-vcard>
* <https://support.mozilla.org/en-US/questions/1380134> Thunderbird SQLite3 address books
* <https://github.com/andystiller/address-book/blob/main/address-db.py>
* <https://github.com/Shravendra/address_book> neat address book API thingy
* <https://realpython.com/contact-book-python-textual> tutorial creating an address book management tool in Python
* <https://zupzup.org/go-example-ical/index.html> creating an iCal feed with Go
* <https://github.com/zupzup/example-go-ical> example code from iCal feed article above
* <https://github.com/arran4/golang-ical>
* <https://pkg.go.dev/github.com/arran4/golang-ical>
* <https://github.com/samedi/caldav-go> abandoned library
* <https://candid.dev/blog/many-hells-of-webdav> state of the world for Go and WebDAV
* <https://github.com/emersion/go-webdav>

    # Password-protect a PDF
    pdftk unenc.pdf cat output enc.pdf encrypt_128bit user_pw whatever


# Docker + Alpine Linux

* <https://wezm.net/technical/2019/02/alpine-linux-docker-infrastructure>


# NixOS

* <https://nathan-kim.org/writing/nixos-post-mortem>


# VMware + VirtualBox

Commands to dump IPs/MACs:

    VBoxManage guestproperty enumerate foo | grep IP
    VBoxManage guestproperty get foo '/VirtualBox/GuestInfo/Net/0/V4/IP'
    VBoxManage showvminfo foo --machinereadable | grep macaddress

    vmrun getGuestIPAddress foo.vmx


# Misc

* <https://mrkaran.dev/posts/home-server-nomad>
* <https://mosh.org>
* <https://smallstep.com/blog/everything-pki.html>
* <https://code.mradford.com/post/the-ubuntu-compiz-desktop>
* <https://github.com/basecamp/omarchy> Linux desktop tweaks (Hyprland window manager, etc.)
* <https://blog.tjll.net/distributed-homelab-cluster>
* <https://ro14nd.de/kubernetes-on-raspberry-pi3>
* <https://blog.hypriot.com/post/setup-kubernetes-raspberry-pi-cluster>
* <https://blog.alexellis.io/serverless-kubernetes-on-raspberry-pi>
* <https://sc5.io/posts/a-private-raspberry-pi-cloud-with-arm-docker>
* <https://instructables.com/id/DIY-Laptop-PowerBank>
* <https://spectrum.ieee.org/consumer-electronics/audiovideo/build-your-own-professionalgrade-audio-amp-on-the-sort-of-cheap>
* <https://hillelwayne.com/post/randomness> brain PRNG?
* <https://waxbanks.wordpress.com/2025/08/01/bare-metal-the-emacs-essay>


# Kubernetes

* <https://digitalocean.com/community/tutorials/an-introduction-to-kubernetes>
* <https://katacoda.com/courses/kubernetes>
* <https://kubernetes.io/docs/tutorials/kubernetes-basics>
* <https://kubernetes.io/docs/tutorials/online-training/overview>
* <https://freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882>
* <https://digitalocean.com/resources/kubernetes>
