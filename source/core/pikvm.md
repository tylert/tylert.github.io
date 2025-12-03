# PiKVM Stuff

* <https://pikvm.org>
* <https://docs.pikvm.org>
* <https://github.com/pikvm/pikvm>
* <https://github.com/pikvm/kvmd>
* <https://blicube.com/blikvm-pcie>

Web default login is: \"admin\" with password \"admin\" SSH default
login is: \"root\" with password \"root\"

Look under \"pages\" in the GitHub repo for additional documentation.


# USB-C OTG + Power Splitter

* <https://tindie.com/products/8086net/usb-cpwr-splitter>
* <https://buyapi.ca/product/usb-c-pwr-splitter>


# ATX Control

* <https://perdeas.bigcartel.com/product/pi-kvm-atx-controller>
* <https://ebay.com/itm/Pi-KVM-ATX-Controller-board-Fully-assembled-and-tested/265214220357>
* <https://reddit.com/r/pikvm/comments/mmiz34/custom_pcb_to_control_atx_without_breadboarding>
* <https://mattmillman.com/info/crimpconnectors/dupont-and-dupont-connectors>


# OLED Display

* <https://github.com/pikvm/pikvm/issues/797>
* <https://reddit.com/r/pikvm/comments/nfit5b/enabling_i2c_for_pioled>
* <https://amazon.ca/WayinTop-Display-SSD1306-3-3V-5V-Raspberry/dp/B085NHM5TC> 128x32, 0.91-inch, 1.49x0.47-inch
* <https://amazon.ca/Elisona-0-96-Serial-Display-Module-Arduino/dp/B074FTQSNH> 128x64, 0.96-inch

    # Add "i2c-dev" into /etc/modules-load.d/kvmd-extra.conf
    # Add "dtparam=i2c_arm=on" into /boot/config.txt

    systemctl enable --now kvmd-oled kvmd-oled-reboot kvmd-oled-shutdown


# Multiplexed Units

* <https://docs.pikvm.org/multiport>
* <https://docs.pikvm.org/wiring_examples>
* <https://blog.ktz.me/pikvm-controlling-up-to-4-servers-simultaneously>
* <https://blog.ktz.me/use-1-pikvm-instance-to-control-4-systems>


# Initial Setup

    # Put the main root filesystem into "writable mode"
    rw

    # Correct the timezone
    # timedatectl show
    # timedatectl list-timezones
    # timedatectl set-timezone UTC

    # Fix /etc/hostname manually or use the following...
    hostnamectl set-hostname pantaloons
    hostname pantaloons
    # Fix host in /etc/kvmd/meta.yaml too for the webUI
    # Replace localhost.localdomain with new hostname

    # Change the default web and ssh passwords
    # Use the local terminal and use su or ssh in, then do...
    kvmd-htpasswd set admin
    passwd root


# Firmware and Updates

    pikvm-update

    pacman --noconfirm --sync rpi4-eeprom  # or rpi5-eeprom
    rpi-eeprom-update -a -d
