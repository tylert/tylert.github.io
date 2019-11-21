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


Custom Cases
------------

* http://fuzzcraft.com/flightcasediy.html
* https://www.amazon.ca/s/ref=bl_dp_s_web_3006902011?ie=UTF8&node=3006902011&field-brandtextbin=Reliable+Hardware


2FA
---

* https://karl-voit.at/2019/03/03/oathtool-otp/
* https://www.sendthemtomir.com/blog/cli-2-factor-authentication


Python PDF + Contacts
---------------------

* http://eventable.github.io/vobject/
* https://github.com/JazzCore/python-pdfkit
* https://github.com/rst2pdf/rst2pdf/blob/master/rst2pdf/createpdf.py
* https://rst2pdf.org/static/manual.html
* http://www.marknagelberg.com/creating-pdf-reports-with-python-pdfkit-and-jinja2-templates/
* http://www.devshed.com/c/a/Python/Python-for-PDF-Generation/


Docker + Alpine Linux
---------------------

* https://www.wezm.net/technical/2019/02/alpine-linux-docker-infrastructure/


VMware + VirtualBox
-------------------

Commands to dump IPs/MACs::

    VBoxManage guestproperty enumerate foo | grep IP
    VBoxManage guestproperty get foo '/VirtualBox/GuestInfo/Net/0/V4/IP'
    VBoxManage showvminfo foo --machinereadable | grep macaddress

    vmrun getGuestIPAddress foo.vmx


Pine64
------

* https://www.linux.com/blog/2019/2/pine64-launch-open-source-phone-laptop-tablet-and-camera
* https://forum.pine64.org/showthread.php?tid=7093&pid=43850#pid43850
* https://archlinuxarm.org/platforms/armv8/rockchip/rock64
* https://www.pine64.org/


Misc
----

* https://www.ckn.io/blog/2017/11/14/wireguard-vpn-typical-setup/
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


AWS
---

::
    aws ec2 describe-images \
        --region=us-east-1 \
        --owners=amazon \
        --filters='Name=name,Values=Windows_Server-2016-English-Full-Base*' \
        --query='sort_by(Images, &CreationDate)[].[Name, ImageId][-1]'


Self-hosted Ngrok
-----------------

nginx conf::

    server {
        server_name tunnel.yourdomain;

        access_log /var/log/nginx/$host;

        # These three lines are new.
        listen 443 ssl;
        ssl_certificate /path/to/tls/cert/fullchain.pem;
        ssl_certificate_key /path/to/tls/cert/privkey.pem;

        location / {
          proxy_pass http://localhost:3333/;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header Host $host;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto https;
          proxy_redirect off;
        }

        error_page 502 /50x.html;
        location = /50x.html {
          root /usr/share/nginx/html;
        }
    }

bash lines::

    python -m http.server 8888
    ssh -R 3333:localhost:8888 yourdomain

* https://jerrington.me/posts/2019-01-29-self-hosted-ngrok.html
