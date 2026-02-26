# NNCP

- <https://changelog.complete.org/archives/10165-asynchronous-email-exim-over-nncp-or-uucp>
- <https://complete.org/building-an-asynchronous-internet-optional-instant-messaging-system>
- <https://complete.org/nncp>
- <https://complete.org/nncpnet-email-network>
- <https://changelog.complete.org/archives/10768-announcing-the-nncpnet-email-network>
- <https://nncp.mirrors.quux.org/UsecaseMail.html> NNCP for email relay?
- <http://nncpgo.org/Use-cases.html> (mandatory 'http' here)
- <https://dataswamp.org/~solene/2024-10-04-secure-file-transfer-with-nncp.html>
- <https://github.com/jgoerzen/nncp-tools> helper shell scripts for maintaining and using NNCP


# Yggdrasil

- <https://willyyangwt.cc/posts/2022/03/08/using-yggdrasil-network-virtual-mesh-ipv6-network.html>
- <https://complete.org/user-yggdrasil-as-an-automatic-mesh-fabric-to-connect-all-your-docker-containers-vms-and-servers>
- <https://changelog.complete.org/archives/10319-make-the-internet-yours-again-with-an-instant-mesh-network>
- <https://cheapskateguide.org/articles/yggdrasil.html>
- <https://github.com/yggdrasil-network/yggdrasil-go>
- <https://yggdrasil-network.github.io>
- <https://yggdrasil-network.github.io/configuration.html>
- <https://wiki.archlinux.org/title/Yggdrasil>
- <https://complete.org/easily-accessing-all-your-stuff-with-a-zero-trust-mesh-vpn>
- <https://github.com/yggdrasil-network/yggdrasil-go/issues/418> how does local peering work?
- <https://reddit.com/r/yggdrasil/comments/ov6hkf/how_do_you_configure_yggdrasil_to_be_a_public_peer>
- <https://reddit.com/r/WireGuard/comments/po56i3/using_wireguard_over_yggdrasilnetwork_how_to>
- <https://medium.com/@mdrahony/how-to-install-yggdrasil-in-debian-stretch-and-find-peers-a9525bf7d2c5>
- <https://apt.izzysoft.de/fdroid/index/apk/com.jbselfcompany.tyr>
- <https://github.com/JB-SelfCompany/Tyr> Yggmail (Yggdrasil email) + DeltaChat/ArcaneChat client
- <https://github.com/JB-SelfCompany/yggmail-android>
- <https://github.com/neilalexander/yggmail>
- <https://delta.chat>
- <https://chatmail.at>
- <https://chtml.ca> Canadian chatmail relay
- <https://github.com/ufm/yggdns64> DNS proxy for Yggdrasil
- <https://codeberg.org/miekg/dns> v2 of libary for yggdns64
- <https://forum.openwrt.org/t/yggdrasil-network-connection/211884> OpenWRT Yggdrasil setup
- <https://nncp.mirrors.quux.org/Yggdrasil.html> NNCP and Yggdrasil
- <https://complete.org/nncp-over-yggdrasil>
- <https://github.com/ScriptNinja-GNU/YggdraSpeed-Mesh-Weaver>
- <https://github.com/ScriptNinja-GNU/TurboTux-BBR-FQ-CoDel-Optimizer>
- <https://github.com/averyanalex/yggdrasil-vanity>
- <https://github.com/averyanalex/ygglkan>
- <https://jacksonchen666.com/posts/2023-06-19/18-19-32> WireGuard over Yggdrasil
- <https://en.wikipedia.org/wiki/Decentralized_network_42> dn42

```
    ufw prepend deny in on tun0 proto ipv6  # put yggdrasil rule first

    # Generate keys (openssl 3.6.0, yggdrasil 0.5.12)
    yggdrasil -genconf > meh.txt
    yggdrasil -useconffile meh.txt -exportkey | openssl pkey -text  # show priv/pub hex strings
    yggdrasil -useconffile meh.txt -exportkey > sec1.key  # extract private key
    openssl pkey -in sec1.key -pubout > pub1.key  # extract public key from private key
    openssl genpkey -algorithm ed25519 -out sec2.key -outpubkey pub2.key  # equivalent keypair
    openssl pkey -in sec2.key -text  # show hex values to pack into yggdrasil config file

    # Generate addresses along with keys
    git clone https://github.com/yggdrasil-network/yggdrasil-go
    cd yggdrasil-go ; go build -o genkeys cmd/genkeys/main.go ; mv genkeys .. ; cd ..
    ./genkeys
```


# Yggdrasil DNS

- <https://github.com/ru-crypto-anarchy/YggNS>
- <https://github.com/zhoreeq/meshname>
- <https://github.com/zhoreeq/coredns-meshname>
- <https://coredns.io/explugins/meshname>
- <https://howto.yggno.de/yggdrasil:dns:meshname>


# CoreDNS

- <https://ivansalloum.com/your-first-authoritative-dns-server-with-coredns>
- <https://blog.idempotent.ca/2018/04/18/run-your-own-home-dns-on-coredns>


# CJDNS

- <https://gathman.org/meshdoc/Cjdns%20-%20Wikipedia.html>
- <https://github.com/ProjectMeshnet>
- <https://github.com/hyperboria>
- <https://wiki.archlinux.org/title/Cjdns>
- <https://github.com/cjdelisle/cjdns>


# Onion Routing

- <https://flower.codes/2025/10/23/onion-mirror.html>


# Other IPv6

- <https://github.com/TheusHen/I6P> another P2P thing


# Mesh

- <https://mango.vg/post/12> 802.11s and WiFi IBSS mesh stuff
- <https://github.com/popura-network/HyperModem/wiki/Ideal-devices-for-Yggdrasil-and-802.11s-mesh> 802.11s devices
- <https://bmaupin.github.io/wiki/other/openwrt/openwrt-80211s.html>
- <https://openwrt.org/docs/guide-user/network/wifi/mesh/802-11s>
- <https://tekovic.com/blog/openwrt-80211s-mesh-networking>
- <https://dn42.dev>
- <https://wireless.docs.kernel.org/en/latest/en/users/drivers/ath10k/mesh.html>


# BBS

- <https://github.com/markqvist/Reticulum/discussions/610> Reticulum BBS notes
- <https://github.com/kc1awv/RetiBBS> Reticulum BBS
- <https://github.com/TheCommsChannel/TC2-BBS-mesh> Meshtastic BBS
- <https://github.com/TechTucson/TT-BBSmesh-Plus> Meshtastic BBS
- <https://unsigned.io/hardware/RNode.html> better than Meshtastic?
- <https://f6fbb.org>
- <http://textfiles.com/hamradio/wreck.ham> (mandatory 'http' here)
- <https://shkspr.mobi/blog/2025/12/a-small-collection-of-text-only-websites> another neat idea
- <https://donuts-are-good.github.io/shhhbb> SSH BBS
- <https://shazow.net/posts/ssh-how-does-it-even> ssh-chat
- <https://github.com/shazow/ssh-chat>
- <https://github.com/quackduck/devzat> another SSH chat thing
- <https://shellbox.dev> return payment details over SSH (QRcode)
- <https://en.wikipedia.org/wiki/FidoNet>
- <https://codeberg.org/AutumnSpark1226/nomadForum>
- <https://github.com/jquast/x84>
- <https://enigma-bbs.github.io>
- <https://github.com/jmbwell/rsbbs>
- <https://github.com/haliphax/xthulu>
- <https://github.com/InterLinked1/lbbs>
- <https://github.com/virtadpt/ebbs>
- <https://github.com/VeggieVampire/MeshBoard>
- <https://retroshed.us/dos-bbs-on-linux>
- <https://github.com/robbiew/retrograde>


# Messaging

- <https://momi.ca/posts/2024-10-09-honeybee.html> XMPP for calls?
- <https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody> run your own XMPP server
- <https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood> view BLE messages?
- <https://neilzone.co.uk/2023/08/a-month-using-xmpp-using-snikket-for-every-call-and-chat>
- <https://snikket.org> XMPP
- <https://マリウス.com/contact> potential XMPP watering hole
- <https://xn--gckvb8fzb.com/contact> potential XMPP watering hole
- <https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server> (mandatory 'www' here)
- <https://profanity-im.github.io> XMPP client
- <https://berty.tech>
- <https://berty.tech/features> BLE and mDNS for messaging?
- <https://fabiensanglard.net/mdns> mDNS
- <https://github.com/berty/berty>
- <https://github.com/berty/weshnet>
- <https://wesh.network>
- <https://bitchat.free> no desktop version
- <https://nostr.com> no desktop version, no instructions for how to run your own relays
- <https://contrapunctus.codeberg.page/the-quick-and-easy-guide-to-xmpp.html>
- <https://jmp.chat> XMPP paid-hosting provider with POTS access?
- <https://molly.im>
- <https://github.com/mollyim/mollyim-android>
- <https://iroh.computer>
- <https://iroh.computer/sendme>
- <https://dumbpipe.dev>
- <https://tryquiet.org>
- <https://github.com/TryQuiet/quiet>
- <https://github.com/TryQuiet/quiet/wiki>
- <https://remark42.com> comment engine thing
- <https://handshake.org>

```
_xmpp-client._tcp.xmpp.example.com  SRV  0 5 5222 xmpp.example.com.
_xmpp-server._tcp.xmpp.example.com  SRV  0 5 5269 xmpp.example.com.
# A/AAAA for xmpp.example.com
# A/AAAA/CNAME for upload.xmpp.example.com
# A/AAAA/CNAME for conference.xmpp.example.com
```


# Email

- <https://cfenollosa.com/blog/after-self-hosting-my-email-for-twenty-three-years-i-have-thrown-in-the-towel-the-oligopoly-has-won.html>
- <https://blog.lopp.net/death-of-decentralized-email>
- <https://blog.sergeantbiggs.net/posts/aerc-a-well-crafted-tui-for-email>
- <https://aerc-mail.org>
- <https://git.sr.ht/~rjarry/aerc>
- <https://sourceforge.net/p/isync/isync> C + Perl replacement for (Python) offlineimap3?
- <https://dev.to/alexbczpro/build-your-own-smtp-server-in-go-5b90>
- <https://mailcatcher.me>
- <https://github.com/sj26/mailcatcher>
- <https://github.com/dynamail/gosmtp>
- <https://github.com/emersion/go-smtp>
- <https://github.com/pimalaya/himalaya> CLI for managing emails
- <https://crates.io/crates/himalaya>
- <https://lostpackets.de/khal> CLI CalDAV client
- <https://stalw.art>
- <https://workaround.org/ispmail-bookworm>
- <https://bitfehler.srht.site/posts/2024-04-15_m2dir-treating-mails-as-files-without-going-crazy.html>
- <https://lib.rs/crates/m2sync> m2dir-imap sync tool
- <https://gist.github.com/chripede/99b7eaa1101ee05cc64a59b46e4d299f> stalwart deployment
- <https://vkttech.com/setup-and-configure-stalwart-email-server-a-comprehensive-guide-for-2025>
- <https://maxadamski.com/blog/2025/10/email.html> self-hosting email
- <https://wiki.archlinux.org/title/S-nail>
- <https://wiki.archlinux.org/title/Isync> IMAP message sync tool
- <https://askubuntu.com/questions/1493425/how-to-convert-multiple-eml-files-into-one-mbox-file>
- <https://github.com/crepererum-oss/tatutanatata> Tuta mail exporter
- <https://addy.io> mail forwarder service
- <https://blog.eppie.io/post/addresses> email ownership
- <https://servury.com/blog/privacy-is-marketing-anonymity-is-architecture> more about identity
- <https://blitiri.com.ar/p/chasquid> Go SMTP server
- <https://github.com/albertito/chasquid> Go SMTP server
- <https://jeffgeerling.com/blog/2026/mailpit-local-email-debugging>
- <https://github.com/axllent/mailpit>

```
    apk add opendkim postfix s-nail
```


# DNS

- <https://atomdns.miek.nl>
- <https://codeberg.org/miekg/dns/src/branch/main/cmd/atomdns>
- <https://codeberg.org/miekg/dns>
- <https://codeberg.org/miekg/dns/src/branch/main/cmd/atomdns/handlers/geoip/README.md> DNS with GeoIP
- <https://mailfud.org/geoip-legacy> GeoIP databases


# Linux Phones

- <https://furilabs.com/shop/flx1> Linux-like phone? (Android HAL underneath?)


# More Tunnel Magic

- <https://haskellforall.com/2024/08/firewall-rules-not-as-secure-as-you.html> holepunch (squid, stunnel, ssh -R, corkscrew)
- <https://github.com/Gabriella439/holepunch> holepunch (squid, stunnel, ssh -R, corkscrew)
- <https://github.com/alebeck/boring> SSH tunnel management
- <https://eli.thegreenplace.net/2022/ssh-port-forwarding-with-go> SSH tunnel management
- <https://ixday.github.io/post/golang_ssh_tunneling>
- <https://github.com/opencoff/go-tunnel>
- <https://github.com/MSSkowron/SSHTunnelHTTP>
- <https://gost.run>
- <https://gost.plus>
- <https://github.com/go-gost/gost>
- <https://github.com/go-gost/gostctl>
- <https://github.com/jpillora/chisel>
- <https://stackoverflow.com/questions/35906991/go-x-crypto-ssh-how-to-establish-ssh-connection-to-private-instance-over-a-ba> jump through a bastion


# Other

- <https://complete.org/interesting-topics>
- <https://olano.dev/blog/software-possession-for-personal-use> local-first software
- <https://inkandswitch.com/essay/local-first>
- <https://inkandswitch.com/local-first>
- <https://inkandswitch.com>
- <https://github.com/coder/wush> WireGuard + Tailscale for sharing files?
- <https://github.com/harsxv/tinystatus> self-hosted statuspage thing?
- <https://gethomepage.dev> self-hosted statuspage thing?
- <https://ploum.net/the-computer-built-to-last-50-years/index.html>
- <https://hackaday.com/2024/09/14/taking-back-the-internet-with-the-tildeverse>
- <https://github.com/ricott1/rebels-in-the-sky> terminal-based game?
- <https://taoshu.in/unix/jool-nat64.html>
- <https://github.com/bypirob/airo> deploy thingy?
- <https://letsdecentralize.org>
- <https://bowshock.nl/irc> start your own internet resiliency club
- <https://startyourownisp.com/posts/network-topology/#gotta-start-somewhere>
- <https://scuttlebutt.nz>
- <https://billdietrich.me/SecureCommunication.html> asynchronous communications options
- <https://iroh.computer> Rust libs for building point-to-point QUIC links?
- <https://iroh.computer/sendme> built with iroh
- <https://dumbpipe.dev> built with iroh
- <https://foks.pub> kv store and git store?
- <https://blog.brixit.nl/dont-pick-weird-subnets-for-embedded-networks> portable network magic?
- <https://github.com/polaroi8d/cactoide> self-hosted RSVP platform
- <https://cactoide.dalev.hu> self-hosted RSVP platform
- <https://tarsnap.com/spiped.html>
- <https://ekzhang.substack.com/p/ssh-hypervisor-simcity-for-vms> unique VMs for each SSH session
- <https://github.com/ekzhang/ssh-hypervisor> unique VMs for each SSH session
- <https://automerge.org>
- <https://github.com/automerge/automerge-go> maybe sucks to build on Linux?


# Git

- <https://anubis.techaro.lol/docs/admin/caveats-gitea-forgejo>
- <https://github.com/antonmedv/gitmal>
- <https://tylercipriani.com/blog/2020/09/22/migrating-git-data-with-rsync>
- <http://www.nncpgo.org/Git.html> (mandatory 'http' and 'www' here)


# Containers Images Backups

- <https://oras.land>
- <https://0pointer.net/blog/a-re-introduction-to-mkosi-a-tool-for-generating-os-images.html>
- <https://dokku.com>
- <https://hamel.dev/blog/posts/dokku>


# Rsync and SSHFS

- <https://media.ccc.de/v/gpn20-41-why-i-wrote-my-own-rsync> router7, distri, gokrazy-rsync, etc.
- <https://github.com/minio/rsync-go>
- <https://github.com/Redundancy/gosync-cmd>
- <https://github.com/Redundancy/gosync>
- <https://github.com/rclone/rclone/issues/7935> rclone pretending to be rsync maybe
- <https://github.com/jbd/msrsync> multiple rsync (Python)
- <https://github.com/nathanhaigh/parallel-rsync>
- <https://strugglers.net/posts/2025/rethinking-my-backups>
- <https://baeldung.com/linux/rsync-parallelize>
- <https://paulgorman.org/technical/gnu-parallel.txt.html>
- <https://blog.ja-ke.tech/2019/08/27/nas-performance-sshfs-nfs-smb.html>
- <https://wiki.archlinux.org/title/SSHFS>
- <https://forums.linuxmint.com/viewtopic.php?t=403971>
- <https://complete.org/an-asynchronous-rsync-with-dar>

One options is to do a dry-run and figure out the list of files, pass it to
split and run rsync on those lists.  Another seems to be passing the list of
file to GNU parallel.


# Publishing

- <https://lmnt.me/blog/how-to-make-a-damn-website.html>
- <https://jvt.me/posts/2019/10/20/indieweb-talk>
- <https://github.com/TimoKats/mdrss> Golang Markdown to RSS converter
- <https://pagedjs.org/made-with-paged.js.html>
- <https://gitlab.coko.foundation/pagedjs/pagedjs>
- <https://gitlab.coko.foundation/pagedjs/pagedjs-cli>
- <https://gitlab.coko.foundation/pagedjs/hugo-pagedjs-plugin>
- <https://github.com/fisodd/hugo-restructured> sexy ReStructuredText markup theme for Hugo
- <https://hugo-restructured-demo.netlify.app/post/using-rest> example of stuff you can do with hugo-restructured
- <https://raw.githubusercontent.com/fisodd/hugo-restructured/master/exampleSite/content/post/using-rest.rst> raw file for page above
- <https://willcrichton.net/notes/portable-epubs> render epubs directly in a web browser???
- <https://krasjet.com/voice/pdf.tocgen> PDF Table Of Contents generation???
- <https://johnfactotum.github.io/foliate> local e-reader app
- <https://github.com/ashishb/wp2hugo> WordPress to Hugo
- <https://github.com/robinmoisson/staticrypt> encrypted static site pages without a server?
- <https://robinmoisson.github.io/staticrypt> encrypted static site pages without a server?
- <https://type.cyhsu.xyz/2024/09/1dollarscan>
- <https://typst.app>
- <https://github.com/typst/typst>
- <https://github.com/typst/packages>
- <https://github.com/typst/typst/issues/2089#issuecomment-3287457743> typst offline docs
- <https://typst.app/universe/package/meander> for typesetting newsletters with images?
- <https://blog.jreyesr.com/posts/typst> typesetting similar to LaTeX
- <https://ydx-2147483647.github.io/best-of-typst> best of Typst links
- <https://github.com/qjcg/awesome-typst> example templates and things for Typst
- <https://github.com/typst/typst/issues/721> Typst HTML output
- <https://github.com/pdf2htmlEX/pdf2htmlEX> PDF to HTML
- <https://pdf2htmlex.github.io/pdf2htmlEX> PDF to HTML
- <https://drewdevault.com/2020/11/01/What-is-Gemini-anyway.html>
- <https://artofmanliness.com/lifestyle/homeownership/butler-s-book>
- <https://imaginarytext.ca/posts/2024/pandoc-typst-tutorial>
- <https://github.com/kr1sp1n/awesome-gemini>
- <https://github.com/pdfcpu/pdfcpu> Go PDF processing tool
- <https://pdfcpu.io> Go PDF processing tool
- <https://medium.com/@ohm.patel1997/command-linetool-to-merge-pdfs-files-in-go-c07e79c2a763> pdfcpu used as a library
- <https://github.com/typst/svg2pdf>
- <https://crates.io/crates/svg2pdf-cli> cargo install svg2pdf-cli
- <https://aur.archlinux.org/packages/svg2pdf> AUR svg2pdf-typst
- <https://aur.archlinux.org/packages/svg2pdf-git> AUR svg2pdf-cairo???
- <https://github.com/wszqkzqk/pdf-svg-conv> yet another svg2pdf (and pdf2svg too)
- <https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly>
- <https://overreacted.io/static-as-a-server> pre-generate output from a web server?
- <https://plainvanillaweb.com/index.html> no framework web pages and simple, single-page applications
- <https://github.com/clawsoftware/clawPDF> pdfcpu/pdftk/tesseract/cups-pdf as a service?
- <https://getzola.org> like Hugo but in Rust
- <https://github.com/getzola/zola> like Hugo but in Rust
- <https://sile-typesetter.org/what-is-sile>
- <https://github.com/sile-typesetter/sile>
- <https://overreacted.io/open-social> AT protocol
- <https://overreacted.io/where-its-at> AT protocol
- <https://マリウス.com/domains-as-internet-handles> why the AT protocol is a bit silly
- <https://xn--gckvb8fzb.com/domains-as-internet-handles> why the AT protocol is a bit silly
- <https://solidproject.org> Solid protocol
- <https://codeberg.org/git-pages/git-pages> codeberg pages
- <https://grebedoc.dev> codeberg pages
- <https://gotosocial.org> ActivityPub self-hosted social network server written in Go
- <https://activitypub.rocks> ActivityPub
- <http://www.nncpgo.org/WARCs.html> (mandatory 'www' here)
- <https://openzim.org/wiki/Build_your_ZIM_file> build zim files for kiwix-desktop
- <https://github.com/typst/typst/issues/2089#issuecomment-3287457743> zim file for typst documentation
- <https://lukaswhite.com/blog/writing-a-book-in-markdown>
- <https://pandoc.org> supports Markdown and Typst
- <https://furlo.sk/blog/odborny/2025-05-07-command-line_tools_for_pdf_processing>
- <https://rsdoiel.github.io/blog/2026/02/21/a_simple_web_we_own.html> tiny web


# Maddy

- <https://maddy.email> Go SMTP server
- <https://github.com/foxcpp/maddy> Go SMTP server
- <https://github.com/foxcpp/maddy/issues/243#issuecomment-655694512> catch-all rule example
- <https://github.com/foxcpp/maddy/blob/master/maddy.conf> default config file

```
    # Catchall example
    destination_in &local_mailboxes {
        deliver_to &local_mailboxes
    }
    destination example.org {
        modify {
            replace_rcpt regexp ".*" "catchall@example.org"
        }
        deliver_to &local_mailboxes
    }
```


# Caddy

- <https://caddyserver.com>
- <https://github.com/caddyserver/certmagic> cert stuff
- <https://github.com/hackfixme/caddy-paseto> auth plugin
- <https://til.jakelazaroff.com/caddy/run-an-https-reverse-proxy-for-local-development>
- <https://blakesite.com/blog/2024-10-03-building-a-markdown-website-with-caddy>
- <https://caddyserver.com/docs/quick-starts/reverse-proxy>
- <https://cloudinfrastructureservices.co.uk/setup-caddy-cdn-on-ubuntu-in-azure-aws-gcp>
- <https://ellen.dev/serve-static-site-using-caddy.html>
- <https://github.com/zhangjiayin/caddy-geoip2> Caddy module for GeoIP
- <https://devguide.dev/blog/routing-requests-in-caddy-to-api-or-file-server-based-on-header>
- <https://caddy.community/t/how-to-return-the-contents-of-a-file-with-the-respond-directive/10458/2>
- <https://caddyserver.com/docs/quick-starts/reverse-proxy>
- <https://github.com/daegalus/caddy-anubis>
- <https://anubis.techaro.lol>
- <https://github.com/TecharoHQ/anubis>
- <https://www.corgijan.dev/2025/05/10/caddy-anubis.html> (mandatory 'www' here)
- <https://anubis.techaro.lol/docs/admin/environments/caddy>
- <https://crispcache.com/help/how-to-setup-cache-on-caddy>
- <https://github.com/caddyserver/cache-handler> might need souin/badger storage
- <https://reddit.com/r/selfhosted/comments/13no9oo/is_it_possible_to_password_protected_reverse_proxy> other caddy-friendly options
- <https://nikstar.me/post/caddy-authelia>
- <https://deuts.org/p/docker-caddy-basic-auth>
- <https://blog.mtaha.dev/security/caddyserver_auth_setup>
- <https://github.com/caddyserver/caddy/issues/4991> Caddy serving Kodi
- <https://caddy.community/t/kodi-compatible-browse-template-again2/16977>
- <https://linuxblog.xyz/posts/caddy-file-server>
- <https://caddyserver.com/docs/caddyfile/directives/file_server>
- <https://caddyserver.com/docs/caddyfile/directives/basic_auth>
- <https://caddyserver.com/docs/automatic-https#local-https> CA root
- <https://kodi.wiki/view/SSL_certificates>
- <https://smallstep.com/docs/step-ca/getting-started> step and step-ca
- <https://smallstep.com/docs/tutorials/acme-protocol-acme-clients/#caddy-v2> step-ca with caddy2
- <https://github.com/smallstep/certificates>
- <https://support.tools/create-certificate-authority-homelab> self-signed certs the old way
- <https://fxgn.dev/blog/anubis> block bots from Caddy without Anubis
- <https://blog.techotom.com/post/2024-02-06-caddy-local-https-snakeoil>
- <https://waitwhat.sh/blog/custom_ca_caddy>
- <https://m0x2a.dreamymatrix.com/caddy-as-internal-ca-and-reverse-proxy>
- <https://unix.stackexchange.com/questions/67568/mount-http-server-as-file-system> replacement for samba
- <https://gitlab.com/BylonAkila/astreamfs> replacement for samba
- <https://github.com/fangfufu/httpdirfs> replacement for samba

/etc/cady/kodi.html

```
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
```

/etc/caddy/Caddyfile

```
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
```


# Web Server

- <https://algernon.roboticoverlords.org>
- <https://github.com/xyproto/algernon>
- <https://github.com/xyproto/permissionbolt> auth module
- <https://github.com/etcd-io/bbolt> bolt database used by Algernon
- <https://github.com/xyproto/wercstyle> entire site as a self-contained Algernon application
- <http://scripting.com/2025/08/28/140604.html> (mandatory 'http' here)
- <https://devever.net/~hl/mildlydynamic>
- <https://it-notes.dragas.net/tags/cdn> DIY CDN magic?
- <https://github.com/mtlynch/picoshare> clicky file sharing thing for non-technical people?
- <https://danburzo.ro/http-caching-refresher>
- <https://github.com/dgraph-io/badger>
- <https://pocketbase.io> backend for web stuff?
- <https://github.com/pocketbase/pocketbase> backend for web stuff?
- <https://git.wntrmute.dev/kyle/caddyhole> geo-blocking fun


# Static Site Generator

- <https://getzola.org>
- <https://getzola.org/documentation/getting-started/overview>
- <https://github.com/getzola/zola>


# Offline Fun

- <https://8chananon.github.io/tut/scraping1.html> scraping web sites using nothing but a web browser???
- <https://jakelazaroff.com/words/a-local-first-case-study> waypoint offline trip planning thing
- <https://github.com/jakelazaroff/waypoint> waypoint offline trip planning thing
- <https://github.com/agersant/polaris> some kind of self-hosted streaming audio server thing
- <https://github.com/ogarcia/docker-polaris> container for polaris
- <https://localfirstweb.dev/blog/2023-05-29-i-wrote-a-static-web-page>
- <https://internet-in-a-box.org> offline learning hotspots


# Wireless

- <https://a.wholelottanothing.org/how-to-build-a-5-acre-wifi-network-cheap-reliable-long-range-wireless-points-make-amazing-things-possible>
- <https://startyourownisp.com>
- <https://wndw.net> Wireless Networks for the Developing World


# Proxies

- <https://github.com/yusing/go-proxy>
- <https://github.com/yusing/go-proxy/wiki>
- <https://github.com/fosrl/pangolin>


# Usenet

```
    Usenet > NZBGet > NZBGeek, NZBPlanet
```


# Backups and File Sharing

- <https://suramya.com/blog/2021/03/syncing-data-between-my-machines-and-phones-using-syncthing>
- <https://blog.jse.li/posts/torrent> Go torrent client
- <http://mikerubel.org/computers/rsync_snapshots> (mandatory 'http' here)
- <https://github.com/WikiBox/snapshot.sh>
- <https://reddit.com/r/selfhosted/comments/1hjqfww/what_are_your_selfhosted_appservice_that_you_cant> doc stuff, etc.
- <https://reddit.com/r/selfhosted/comments/1hlyjv3/what_is_your_selfhosted_discover_in_2024> wiki stuff, doc stuff, etc.
- <https://grdw.nl/2022/10/03/how-to-copy-a-file-between-devices.html>
- <https://github.com/localsend/localsend>
- <https://github.com/9001/copyparty> Python Samba server with uploads and downloads that work from a regular web browser
- <https://opensource.com/article/20/1/create-save-run-rsync-configurations>


# Auth

- <https://github.com/anderspitman/obligator> self-hosted OpenID via email


# Networking

- <https://mjg59.dreamwidth.org/72095.html>
- <https://github.com/juhovh/tailguard>
- <https://garrido.io/notes/wireguard-topologies-for-self-hosting-at-home>
- <https://github.com/net4people/bbs> shouting into the ether
- <https://github.com/net4people/bbs/issues/88#issuecomment-928690089> obfuscating wireguard packets
- <https://computerscot.github.io/wireguard-obfuscated-udp.html>
- <https://btwiusearch.net/posts/wg-over-udp2raw>
- <https://github.com/ClusterM/wg-obfuscator>
- <https://shadowsocks.org>
- <https://github.com/shadowsocks/shadowsocks-rust>
- <https://github.com/shadowsocks/go-shadowsocks2>
- <https://github.com/wangyu-/udp2raw>
- <https://github.com/hrimfaxi/tutuicmptunnel> bpf for doing udp-over-icmp? (replaces udp2raw icmp mode?)
- <https://hysteria.network> censorship-resistant proxy
- <https://github.com/apernet/hysteria> censorship-resistant proxy
- <https://notes.pault.ag/tpl> The Promised LAN Manifesto
- <https://tpl.house> The Promised LAN architecture
- <https://procustodibus.com/blog/2020/10/wireguard-topologies/#hub-and-spoke> WireGuard hub and spoke model diagram


# Sharing

- <https://0x0.st>
- <https://git.0x0.st/mia/0x0>
- <https://hole.0x0.st> webwormhole
- <https://github.com/saljam/webwormhole>
- <https://opengist.io>
- <https://github.com/thomiceli/opengist>


# AI

- <https://getubo.com> personal assitant gimmick?
- <https://github.com/epicenter-so/epicenter/tree/main/apps/whispering>
