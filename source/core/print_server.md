# Pi Print Server


## Setup

Prepare to use CUPS:

```
    # Install necessary printer packages
    apt-get --yes install avahi-daemon cups
    apt-get --yes install printer-driver-brlaser

    # Add a user to the 'lpadmin' group
    # This is needed for the web admin login for CUPS
    usermod -a -G lpadmin ${USER}
    # Type 'newgrp lpadmin' to refresh login without a reboot/login
```

- <https://packages.debian.org/bullseye/printer-driver-brlaser>

```
    # Ensure the local package index is up-to-date
    pacman --refresh -S --upgrade

    # Install the prerequisites for the printer driver
    pacman --noconfirm -S git

    gpg --keyserver keys.gnupg.net --recv-keys 6AD860EED4598027
    git clone https://aur.archlinux.org/brother-hll2300d.git
    git clone https://aur.archlinux.org/brlaser.git
    pushd brother-hll2300d
    makepkg -si
    popd
    pushd brlaser
    makepkg -si
    popd
```

Then, fix up the CUPS config file to allow remote administration via the
web interface:

```
    cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.orig

    # Comment out all 'Listen' lines
    sed -i '/^Listen /s/^/# /' /etc/cups/cupsd.conf

    # Add 'Port 631' before 'Listen' lines
    if ! grep Port /etc/cups/cupsd.conf; then
        sed -i '/Listen localhost:631/i Port 631' /etc/cups/cupsd.conf
    fi

    # Add 'Allow @Local' after each 'Order allow,deny' or 'Order deny,allow'
    if ! grep Allow /etc/cups/cupsd.conf; then
        sed -i '/Order allow,deny/a Allow @Local' /etc/cups/cupsd.conf
        sed -i '/Order deny,allow/a Allow @Local' /etc/cups/cupsd.conf
    fi
```

## Printer Setup

Visit <https://HOSTNAME:631/admin>.

Select \'Adding Printers and Classes\' and then \'Add Printer\'. Pick
USB printer from \'Local Printers\' and click \'Continue\'. Next to
\'Sharing\', tick the \'Share This Printer\' box. In the \'Model\' list,
pick the \'Brother HL-2240D Foomatic/hpijs-pcl5e (recommended) (en)\'
option and click \'Add Printer\'.

Remove the \'PDF\' printer, choose the new printer and, under
\'Maintenance\', select \'Set As Server Default\'.


## Background

- <https://njh.eu/printer.html>
- <http://blog.pi3g.com/2013/08/using-the-raspberry-pi-as-cups-print-server-for-windows-and-apple-mac-airprint>
- <http://support.brother.com/g/b/downloadlist.aspx?c=us&lang=en&prod=hl2240_us_eu&os=128>


## OMG

- <https://retrohacker.substack.com/p/bye-cups-printing-with-netcat>
- <https://blog.jgc.org/2021/11/making-old-usb-printer-support-apple.html>
