rpi
---

* https://wiki.openwrt.org/toh/raspberry_pi_foundation/raspberry_pi


docker
------

* https://abe-winter.github.io/blues/2017/04/27/config-vs-containers.html
* https://github.com/hobby-kube/guide

::

    docker rmi $(docker images --filter "reference=myregistry.example.com/*" --quiet)
    docker rmi $(docker images --filter "dangling=true" --quiet)


linux
-----

* http://blog.alexellis.io/boot-linuxkit-in-10-mins/
* https://github.com/MichielDerhaeg/build-linux
* https://linux-audit.com/using-unattended-upgrades-on-debian-and-ubuntu/


style
-----

* https://github.com/mvdan/sh


cloud-init
----------

* http://stackoverflow.com/questions/23065673/how-to-re-run-cloud-init-without-reboot
* http://stackoverflow.com/questions/23151425/how-to-run-cloud-init-manually
* http://cloudinit.readthedocs.io/en/latest/topics/modules.html


python
------

* http://sedimental.org/the_packaging_gradient.html
