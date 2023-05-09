Containers
----------

* https://abe-winter.github.io/blues/2017/04/27/config-vs-containers.html
* https://github.com/hobby-kube/guide
* https://iximiuz.com/en/posts/from-docker-container-to-bootable-linux-disk-image/
* https://grahamc.com/blog/nix-and-layered-docker-images

::

    docker rmi $(docker images --filter "reference=myregistry.example.com/*" --quiet)
    docker rmi $(docker images --filter "dangling=true" --quiet)


Linux
-----

* http://blog.alexellis.io/boot-linuxkit-in-10-mins/
* https://github.com/MichielDerhaeg/build-linux
* https://linux-audit.com/using-unattended-upgrades-on-debian-and-ubuntu/


Style
-----

* https://github.com/mvdan/sh
* https://github.com/SixArm/unix-shell-script-tactics/blob/main/README.md


cloud-init
----------

* http://stackoverflow.com/questions/23065673/how-to-re-run-cloud-init-without-reboot
* http://stackoverflow.com/questions/23151425/how-to-run-cloud-init-manually
* http://cloudinit.readthedocs.io/en/latest/topics/modules.html


Python
------

* http://sedimental.org/the_packaging_gradient.html


2FA
---

* https://karl-voit.at/2019/03/03/oathtool-otp/
* https://www.sendthemtomir.com/blog/cli-2-factor-authentication
* https://blog.snapdragon.cc/2019/04/27/using-a-yubikey-to-secure-ssh-on-macos/
* https://www.engineerbetter.com/blog/yubikey-all-the-things/


PDF + Contacts
--------------

* http://eventable.github.io/vobject/
* https://github.com/JazzCore/python-pdfkit
* https://github.com/rst2pdf/rst2pdf/blob/master/rst2pdf/createpdf.py
* https://rst2pdf.org/static/manual.html
* http://www.marknagelberg.com/creating-pdf-reports-with-python-pdfkit-and-jinja2-templates/
* http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/

::

    # Password-protect a PDF
    pdftk unenc.pdf cat output enc.pdf encrypt_128bit user_pw whatever


Docker + Alpine Linux
---------------------

* https://www.wezm.net/technical/2019/02/alpine-linux-docker-infrastructure/


NixOS
-----

* https://nathan-kim.org/writing/nixos-post-mortem


VMware + VirtualBox
-------------------

Commands to dump IPs/MACs::

    VBoxManage guestproperty enumerate foo | grep IP
    VBoxManage guestproperty get foo '/VirtualBox/GuestInfo/Net/0/V4/IP'
    VBoxManage showvminfo foo --machinereadable | grep macaddress

    vmrun getGuestIPAddress foo.vmx


Misc
----

* https://mrkaran.dev/posts/home-server-nomad/
* https://mosh.org/
* https://smallstep.com/blog/everything-pki.html
* https://code.mradford.com/post/the-ubuntu-compiz-desktop/
* https://www.remove.bg/
* https://blog.tjll.net/distributed-homelab-cluster/
* https://ro14nd.de/kubernetes-on-raspberry-pi3
* https://blog.hypriot.com/post/setup-kubernetes-raspberry-pi-cluster/
* https://blog.alexellis.io/serverless-kubernetes-on-raspberry-pi/
* https://sc5.io/posts/a-private-raspberry-pi-cloud-with-arm-docker/
* https://www.instructables.com/id/DIY-Laptop-PowerBank/
* https://spectrum.ieee.org/consumer-electronics/audiovideo/build-your-own-professionalgrade-audio-amp-on-the-sort-of-cheap


Kubernetes
----------

* https://www.digitalocean.com/community/tutorials/an-introduction-to-kubernetes
* https://www.katacoda.com/courses/kubernetes
* https://kubernetes.io/docs/tutorials/kubernetes-basics/
* https://kubernetes.io/docs/tutorials/online-training/overview/
* https://www.freecodecamp.org/news/learn-kubernetes-in-under-3-hours-a-detailed-guide-to-orchestrating-containers-114ff420e882/
* https://www.digitalocean.com/resources/kubernetes/
