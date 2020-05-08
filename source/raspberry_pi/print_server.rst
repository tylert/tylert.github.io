Pi Print Server
===============


OS
--

Install Raspbian Lite as per the instructions found in first_boot_.
.. _first_boot: first_boot.rst


Setup
-----

::

    sudo apt-get --yes install avahi-daemon cups python-cups
    sudo apt-get --yes install printer-driver-hpijs

::

    # Add user to 'lpadmin' group

::

    wget -c https://njh.eu/Brother-HL-2240D-hpijs-pcl5e.ppd
    mv Brother-HL-2240D-hpijs-pcl5e.ppd /usr/share/ppd/custom

Or, fetch it here at brother_hl-2240d_ppd_.

.. _brother_hl-2240d_ppd: Brother-HL-2240D-hpijs-pcl5e.ppd

::

    sudo cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.orig

    # Comment out all 'Listen' lines
    sudo sed -i '/^Listen /s/^/# /' /etc/cups/cupsd.conf

    # Add 'Port 631' before 'Listen' lines
    if ! grep Port /etc/cups/cupsd.conf; then
        sudo sed -i '/Listen localhost:631/i Port 631' /etc/cups/cupsd.conf
    fi

    # Add 'Allow @Local' after each 'Order allow,deny'
    if ! grep Allow /etc/cups/cupsd.conf; then
        sudo sed -i '/Order allow,deny/a Allow @Local' /etc/cups/cupsd.conf
    fi



Printer Setup
-------------

Visit https://hostname:631/admin/.

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
