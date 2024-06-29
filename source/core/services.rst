Devices
-------

* https://mikrotik.com/product/crs305_1g_4s_in
* https://lengrand.fr/complete-setup-epaper
* https://github.com/mecparts/PicoWiFiModem  Raspberry Pi Pico W acting as a modem for retro devices
* https://github.com/mecparts/RetroWiFiModem  Same as above but for ESP8266 (ESP32 too?)
* https://codedbearder.com/posts/f3-backplane  TerraMaster F2-221 replacement daughter PCB


TOTP, CA, U2F, FIDO
-------------------

* https://smallstep.com/blog/build-a-tiny-ca-with-raspberry-pi-yubikey
* https://github.com/bulwarkid/virtual-fido
* https://github.com/susam/mintotp
* https://www.reddit.com/r/selfhosted/comments/h02wzr/how_to_adding_totp_to_sudo
* https://www.linuxbabe.com/ubuntu/two-factor-authentication-ssh-key-ubuntu
* https://wiki.archlinux.org/title/Google_Authenticator
* https://github.com/google/google-authenticator-libpam

::

    # Enable TOTP for each USER
    sudo google-authenticator -s /root/.sudo_totp/${USER}/.google_authenticator
    sudo chmod 0600 -R /root/.sudo_totp

    sudo google-authenticator -s /root/.google_authenticator
    sudo chmod 0600 -R /root/.google_authenticator

/etc/pam.d/sudo::

    # Use Google Auth -- Mandatory
    auth required pam_google_authenticator.so secret=/root/.sudo_totp/${USER}/.google_authenticator user=root

    # Use Google Auth -- Only if secret key exists
    # auth required pam_google_authenticator.so secret=/root/.sudo_totp/${USER}/.google_authenticator user=root nullok

/etc/pam.d/su::

    # Use Google Auth -- Mandatory
    auth required pam_google_authenticator.so secret=/root/.google_authenticator user=root


Dynamic DNS
-----------

* https://medium.com/aws-activate-startup-blog/building-a-serverless-dynamic-dns-system-with-aws-a32256f0a1d8
* https://jamesturner.im/2019/01/20/dynamic-dns-using-terraform-aws.html
* https://medium.com/@matzhouse/dynamic-dns-with-terraform-and-route53-3fafe7c68970


Service Mesh
------------

* https://youtu.be/8T8t4-hQY74
* https://www.youtube.com/watch?v=vh1YtWjfcyk
* https://youtu.be/bEFILWrRJJ4


VPN
---

* https://mikkel.hoegh.org/2019/11/01/home-vpn-server-wireguard
* https://blog.gwlab.page/vpn-over-ssh-the-socks-proxy-8a8d7bdc7028


Email
-----

* https://stalw.art  single Rust binary/container for email server stuff
* https://github.com/stalwartlabs/mail-server  single Rust binary/container for email server stuff
* https://cfenollosa.com/blog/after-self-hosting-my-email-for-twenty-three-years-i-have-thrown-in-the-towel-the-oligopoly-has-won.html
* https://www.xomedia.io/blog/a-deep-dive-into-email-deliverability  DMARC, DKIM, SPF generators?
* https://github.com/mjl-/mox
* https://github.com/neilalexander/yggmail
* https://simonandrews.ca/articles/how-to-set-up-spf-dkim-dmarc
* https://gabrielsieben.tech/2024/05/17/thinking-out-loud-2nd-gen-email


Mesh
----

* https://yggdrasil-network.github.io
* https://github.com/yggdrasil-network/yggdrasil-go
* https://yggdrasil-openwrt.github.io
* https://willyyangwt.cc/posts/2022/03/08/using-yggdrasil-network-virtual-mesh-ipv6-network.html
* https://complete.org/user-yggdrasil-as-an-automatic-mesh-fabric-to-connect-all-your-docker-containers-vms-and-servers
* https://changelog.complete.org/archives/10319-make-the-internet-yours-again-with-an-instant-mesh-network


Other
-----

* https://github.com/awesome-selfhosted/awesome-selfhosted
* https://blog.ioces.com/matt/posts/everything-old-is-new-again
* https://github.com/librespeed/speedtest  self-hosted speed tests?
* https://github.com/librespeed/speedtest-go  self-hosted speed tests?
* https://blog.lopp.net/death-of-decentralized-email
* https://notes.volution.ro/v1/2022/09/notes/b08118d8  hosting static sites
* https://github.com/meienberger/runtipi
* https://old.reddit.com/r/selfhosted/comments/xhe5ul/matrix_was_worth_the_effort_to_self_host
* https://news.ycombinator.com/item?id=33095823
* https://github.com/mikeroyal/Self-Hosting-Guide
* https://kevquirk.com/comparing-static-site-hosts-best-host-for-a-static-site
* https://blog.taoetc.org/how_to_publish_a_static_site_over_nncp
* https://fossil-scm.org
* https://indieweb.org/POSSE  Publish Own Site Syndicate Elsewhere
* https://github.com/PhirePhly/micromirrors  mirroring things
* https://blog.randombits.host/monitoring-self-hosted-services  Grafana, Prometheus, Loki, etc.
* https://the-dam.org/docs/explanations/suc.html  awesome local server chat thing (5 lines of bash???)
* https://the-dam.org  pay-for Unix/Linux playground
* https://tildeverse.org  Unix/Linux playground awesome
* http://tilde.club  Unix/Linux playground
* https://rafichaudhury.com/site/blog/Folderbase  Hypercard-like Markdown thing
* https://github.com/thomiceli/opengist  open-source, self-hostable GitHub Gists and/or pastebin
* https://ayende.com/blog/201153-B/building-a-serverless-secured-dead-drop
* https://www.zedng.com/p/harden-linux-self-hosting-vps-dokku-nextjs-migration  Heroku-like thing?


Authentication
--------------

* https://github.com/glauth/glauth  LDAP server in Go with a variety of backends
* https://glauth.github.io  GLAuth docs


SSH
---

* https://nullprogram.com/blog/2019/03/22  endlessssh ssh tarpit in C
* https://github.com/shizunge/endlessh-go  endlessssh ssh tarpit in Go with Prometheus fancy
* https://unsigned.io/articles/2018_06_30_15-kilometre-ssh-link-with-rnode.html  SSH over LoRa


Logging and Metrics
-------------------

* https://matduggan.com/were-all-doing-metrics-wrong
* https://kubernetes.io/docs/concepts/cluster-administration/logging/#cluster-level-logging-architectures
* https://kener.ing  dashboard stuff???
* https://github.com/rcoh/angle-grinder  nifty tool


Winderz
-------

* https://usebottles.com  run Windoze apps on Linux???
* https://github.com/quickemu-project/quickemu  easy-mode QEMU (KVM) bash script stuff


PiHole
------

* https://raspberrypi.stackexchange.com/questions/58732/remove-ssh-warning-about-default-password
* https://github.com/pi-hole/pi-hole/#one-step-automated-install
* https://greg.jeanmart.me/2020/04/13/self-host-pi-hole-on-kubernetes-and-block-ad

::

    # PiHole
    wget -O basic-install.sh https://install.pi-hole.net
    sudo bash basic-install.sh


Bash Magic
----------

Script, know thyself::

    directory="$(dirname $(readlink -f ${BASH_SOURCE[0]}))"

* https://www.die-welt.net/2021/11/i-just-want-to-run-this-one-python-script
* https://github.com/gyf304/dotenv  C tool for populating running environment variables


Ngrok Clone
-----------

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
* https://github.com/pgrok/pgrok
* https://github.com/amalshaji/portr
* https://portr.dev
* https://mrkaran.dev/posts/travel-tailscale
* https://0xda.de/blog/2024/04/can-you-grok-it


Networking Magic
----------------

* http://www.pocketnix.org/posts/Linux%20Networking:%20MAC%20VLANs%20and%20Virtual%20Ethernets
* https://github.com/luainkernel/lunatik  LUA scripting for kernel stuff???
* https://startyourownisp.com
* https://j6b72.de/article/why-you-should-take-a-look-at-traefik
* https://zoraxy.arozos.com/#features  reverse-proxy stuff for homelabs


Crypto Magic
------------

* https://github.com/dehydrated-io/dehydrated  ACMEv2 shell script

::

    # If working on slightly-wacky Unix-like operating systems
    alias openssl=$(brew --prefix openssl@1.1)/bin/openssl

    # RSA
    openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:8192 -out priv
    openssl pkey -pubout -in priv -out pub

    # ED-209
    openssl genpkey -algorithm ed25519 -out priv
    openssl pkey -pubout -in priv -out pub


Webby Stuff
-----------

* https://www.devever.net/~hl/mildlydynamic
* https://devguide.dev/blog/routing-requests-in-caddy-to-api-or-file-server-based-on-header
* https://caddy.community/t/how-to-return-the-contents-of-a-file-with-the-respond-directive/10458/2
