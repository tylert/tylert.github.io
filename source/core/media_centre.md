# LibreELEC

The networking stuff for LibreELEC is 'slightly weird'. Makes it kinda
hard to do a 'send hostname' for DHCP.

* <https://wiki.archlinux.org/index.php/ConnMan>
* <https://git.kernel.org/pub/scm/network/connman/connman.git>
* <https://jeffgeerling.com/blog/2022/using-libreelec-pro-management-ssh>


# Netflix

* <https://itnext.io/the-2021-onward-guide-to-install-netflix-on-raspberry-pi-smartphone-as-the-remote-control-2e7662ccc80>


# OMFG Kodi CLI

* <https://forum.kodi.tv/showthread.php?tid=120248&pid=2664155#pid2664155>
* <https://mankier.com/1/kodi-send>
* <https://github.com/jose1711/kodi-ansible-role>
* <https://github.com/nawar/kodi-cli>


# Caddy for Kodi

* <https://github.com/caddyserver/caddy/issues/4991>
* <https://caddy.community/t/kodi-compatible-browse-template-again2/16977>
* <https://linuxblog.xyz/posts/caddy-file-server>
* <https://caddyserver.com/docs/caddyfile/directives/file_server>
* <https://caddyserver.com/docs/caddyfile/directives/basic_auth>
* <https://caddyserver.com/docs/automatic-https#local-https> CA root
* <https://kodi.wiki/view/SSL_certificates>
* <https://smallstep.com/docs/step-ca/getting-started> step and step-ca
* <https://smallstep.com/docs/tutorials/acme-protocol-acme-clients/#caddy-v2> step-ca with caddy2
* <https://github.com/smallstep/certificates>
* <https://support.tools/create-certificate-authority-homelab> self-signed certs the old way
* <https://fxgn.dev/blog/anubis> block bots from Caddy without Anubis
* <https://blog.techotom.com/post/2024-02-06-caddy-local-https-snakeoil>
* <https://waitwhat.sh/blog/custom_ca_caddy>
* <https://m0x2a.dreamymatrix.com/caddy-as-internal-ca-and-reverse-proxy>

/etc/cady/kodi.html

    {{$useragent := .Req.Header.Get "User-Agent"}}
    {{if regexMatch "^Kodi" $useragent}}
    <!DOCTYPE html>
    <html><body><table><tbody>
    {{range .Items}}
      <tr>
        <td><a href="{{html .URL | replace "./" ""}}">{{html .Name}}</a></td>
        <td>{{.HumanModTime "2006-Jan-02 15:04:05"}}</td>
        <td>{{if .IsDir}}-{{else}}{{.HumanSize | replace " " "" | replace "iB" ""}}{{end}}</td>
        <td>{{if .IsDir}}Directory{{else}}application/octet-stream{{end}}</td>
      </tr>
    {{end}}
    <tbody></table></body></html>
    {{else}}
    ... browse output for other user agents (not kodi) ...
    {{end}}

/etc/caddy/Caddyfile

    {
        pki {
            ca internal {
                name moo_lab
            }
        }
    }
    :80 {
        root * /foo
        tls internal
        file_server * {
            browse /etc/caddy/kodi.html
        }
    }
    :81 {
        root * /foo
        tls internal
        file_server browse
    }


# OSMC on Debian

    #!/usr/bin/env bash

    # http://software.opensuse.org/download.html?project=home:osmc&package=osmc-installer
    # s/8.0/7.0/ for wheezy

    wget -O - \
      http://download.opensuse.org/repositories/home:osmc/Debian_8.0/Release.key |\
      apt-key add -

    echo 'deb http://download.opensuse.org/repositories/home:/osmc/Debian_8.0/ /' \
      > /etc/apt/sources.list.d/osmc-installer.list

    apt-get update
    apt-get install osmc-installer


# Activate MPEG Stuff (DEPRECATED)

Go buy license key(s) from <https://raspberrypi.com/mpeg-2-license-key>
and <https://raspberrypi.com/vc-1-license-key>.

Wait up to 24 hours for an email to arrive with your keys.

FIXME Do this better:

    # Add 'decode_MPG2=0xdeadbeef' to /boot/config.txt
    # Add 'decode_WVC1=0xdeadbeef' to /boot/config.txt

To verify that it worked after a reboot, type:

    vcgencmd codec_enabled MPG2
    vcgencmd codec_enabled WVC1

The less painful way of enabling the codecs:

    cd /boot
    cp start_x.elf start_x.elf.backup && \
        perl -pne 's/\x47\xE9362H\x3C\x18/\x47\xE9362H\x3C\x1F/g' < start_x.elf.backup > start_x.elf

* <https://reddit.com/r/raspberry_pi/comments/5x7xbo/patch_for_mpeg2_vc1_license>
* <https://news.ycombinator.com/item?id=16381331>


# Other

* <https://github.com/oss001/KodiStreaming/blob/master/setup.sh>
* <https://makingstuffwork.net/technology/watch-netflix-amazon-prime-kodi>
* <https://raspberrytips.com/install-netflix-on-kodi>
* <https://raw.githubusercontent.com/zjoasan/netflix-install-script/master/netflix_prep_install.sh>
* <https://hackster.io/sbcomponentsuk/netflix-and-amazon-prime-video-now-streaming-on-raspberry-pi-44f3cb>
* <https://johnlian.net/posts/hdmi-cec> HDMI-CEC
