Pi Print Server
===============


OS
--

Install Raspbian Lite as per the instructions found in first_boot_.
.. _first_boot: first_boot.rst


Setup
-----

Prepare to use CUPS::

    # Install necessary printer packages
    sudo apt-get --yes install avahi-daemon cups python-cups
    sudo apt-get --yes install printer-driver-brlaser

    # Add a user to the 'lpadmin' group (and refresh list without logging out)
    # This is needed for the web admin login for CUPS
    sudo usermod -a -G lpadmin ${USER}
    newgrp lpadmin

If you're using a printer that is well-supported by the
"printer-driver-brlaser" package
(https://packages.debian.org/bullseye/printer-driver-brlaser) you won't need to
do anything here.  If not, you might need to fetch a PPD file like this::

    wget -c https://njh.eu/Brother-HL-2240D-hpijs-pcl5e.ppd
    mv Brother-HL-2240D-hpijs-pcl5e.ppd /usr/share/ppd/custom

Or, fetch it here at brother_hl-2240d_ppd_.

.. _brother_hl-2240d_ppd: Brother-HL-2240D-hpijs-pcl5e.ppd

Then, fix up the CUPS config file to allow remote administration via the web
interface::

    sudo cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.orig

    # Comment out all 'Listen' lines
    sudo sed -i '/^Listen /s/^/# /' /etc/cups/cupsd.conf

    # Add 'Port 631' before 'Listen' lines
    if ! grep Port /etc/cups/cupsd.conf; then
        sudo sed -i '/Listen localhost:631/i Port 631' /etc/cups/cupsd.conf
    fi

    # Add 'Allow @Local' after each 'Order allow,deny' or 'Order deny,allow'
    if ! grep Allow /etc/cups/cupsd.conf; then
        sudo sed -i '/Order allow,deny/a Allow @Local' /etc/cups/cupsd.conf
        sudo sed -i '/Order deny,allow/a Allow @Local' /etc/cups/cupsd.conf
    fi

    sudo /etc/init.d/cupsd restart



Printer Setup
-------------

Visit https://${HOSTNAME}:631/admin/.

Select 'Adding Printers and Classes' and then 'Add Printer'.  Pick USB printer
from 'Local Printers' and click 'Continue'.  Next to 'Sharing', tick the 'Share
This Printer' box.  In the 'Model' list, pick the 'Brother HL-2240D
Foomatic/hpijs-pcl5e (recommended) (en)' option and click 'Add Printer'.

Remove the 'PDF' printer, choose the new printer and, under 'Maintenance',
select 'Set As Server Default'.



Background
----------

* https://njh.eu/printer.html
* http://blog.pi3g.com/2013/08/using-the-raspberry-pi-as-cups-print-server-for-windows-and-apple-mac-airprint/
* http://support.brother.com/g/b/downloadlist.aspx?c=us&lang=en&prod=hl2240_us_eu&os=128


OMG
---

* https://retrohacker.substack.com/p/bye-cups-printing-with-netcat
