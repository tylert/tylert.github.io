Inventory Management
--------------------

* https://dmd.tanna.dev  create a local database of all your software dependencies
* https://github.com/opensbom-generator/spdx-sbom-generator


Tmux With Terminal Stuff
------------------------

* https://arcolinux.com/everything-you-need-to-know-about-tmux-status-bar
* https://man.openbsd.org/tmux
* https://github.com/sbernheim4/dotfiles/blob/master/tmux/.tmux.conf
* https://www.ditig.com/256-colors-cheat-sheet
* https://ianthehenry.com/posts/how-to-configure-tmux

::

    # tmux
    PFX = ctrl + b

    PFX + ?       # show shortcuts
    PFX + :       # enter command mode

    PFX + %       # split pane vertically
    PFX + "       # split pane horizontally
    PFX + { or }  # move pane left or right
    PFX + q       # show pane numbers
    PFX + !       # convert pane to window
    PFX + space   # cycle through pane layouts

    PFX + c       # create new window
    PFX + p or n  # previous or next window
    PFX + 0 to 9  # select window 0 to 9
    PFX + ,       # rename window
    PFX + &       # close current window
    PFX + :swap-window -t -1  # move current window left one

    PFX + s       # show sessions
    PFX + d       # detach from session
    PFX + ( or )  # previous or next session
    PFX + $       # rename session

    # terminal
    gnome-terminal --tab  # open new tab in current terminal

    ctrl + pgup or pgdn  # select previous or next tab

    shift + ctrl + c or v             # tmux pass-through copy or paste
    shift + left/middle/right-button  # tmux pass-through left/middle/right-button
    # etc., etc., etc...

Record terminal commands to an SVG animation::

    pip install termtosvg  # termtosvg is currently abandonware
    echo "PS1='\$ '" > ugh.sh
    termtosvg login.svg --screen-geometry 80x10 --command 'bash --rcfile ugh.sh'

* https://stackoverflow.com/questions/17445100/getting-back-old-copy-paste-behaviour-in-tmux-with-mouse
* https://superuser.com/questions/1336762/how-do-i-copy-paste-from-the-system-clipboard-in-tmux-in-xterm-on-linux
* https://stackoverflow.com/questions/1188959/how-to-open-a-new-tab-in-gnome-terminal-from-command-line
* https://aj.codes/posts/be-careful-using-tmux-and-environment-variables


Game Stuff
----------

* https://github.com/kentonv/lanparty
* https://kilograham.github.io/rp2040-doom
* https://news.ycombinator.com/item?id=31590724
* https://github.com/pod-arcade/pod-arcade  k8s + RetroArch???
* https://bazzite.gg  immutable desktop for Steam Decks?
* https://www.renpy.org/doc/html/build.html#archives  .rpa scripts and images files example
* https://www.reddit.com/r/RenPy/comments/wq6jms/how_to_compress_un_rpa
* https://www.reddit.com/r/RenPy/comments/sv92zp/rpa_files  .rpa files are just Python pickle files maybe?
* https://github.com/Lattyware/unrpa  RenPy data file unpacking
* https://pypi.org/project/unrpa  pip install unrpa
* https://github.com/shizmob/rpatool  RenPy data file repacking thing maybe?


Video/Audio/Camera Awesome
--------------------------

::

    # Convert files to/from other formats
    ffmpeg -i foo.mov -map 0 -c copy foo.mp4
    ffmpeg -i foo.webm -c copy foo.mp4

    # Downsample videos and/or chop off/out sections based on time
    # to alter length of videos, after the -i, add:  '-ss' start time, '-t' duration or '-to' end time
    ffmpeg -i foo.mpg -r 30 -s 960x540 smaller.mp4

    # Concatenate files end-to-end
    # put "file 1.mp4\nfile2.mp4" and so on in a list.txt file and then run
    ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4

    # audio cd -> wav -> flac
    cdda2wav -vall cddb=0 speed=4 -paranoia paraopts=proof -B -D /dev/sr0
    flac --verify foo.wav

    # Stream ripping example (try to keep metadata; needs work)
    ffmpeg -i http://fr.ah.fm:8000/192k -map_metadata 0:s:0 ah_fm.mp3

Just fix the title of the video file::

    ffmpeg -i input.whatever -c copy -map 0 -metadata title='Something else' output.whatever

HandBrake settings for DVDs::

    # Start with settings 'Official -> General -> HQ 1080p30 Surround'
    Summary:
        Format:  MPEG-4 (avformat)
        Web Optimized:  disabled
        Align A/V Start:  enabled
        iPod 5G Support:  disabled
        Passthru Common Metadata:  enabled
    Dimensions:
        Flipping Horizontal:  disabled
        Rotation:  Off
        Cropping:  Conservative or None depending on the disc
        Resolution Limit:  720p HD
        Anamorphic:  Automatic
        Optimal Size:  enabled
        Allow Upscaling:  disabled
        Borders Fill:  None
        Color:  Black
        Final Dimensions Automatic:  enabled
    Filters:
        Detelecine:  Off
        Interlace Detection:  Default
        Deinterlace:  Decomb
        Deinterlace Preset:  Default
        Deblock Filter:  Off
        Denoise Filter:  Off
        Chroma Smooth Filter:  Off
        Sharpen Filter:  Off
        Grayscale:  disabled
        Colorspace:  Off
    Video:
        Video Encoder:  H.264 (x264)
        Framerate:  30
        RF:  19
        Constant Quality:  selected
        Constant Framerate:  selected
        Preset:  slow
        Tune:  None
        Fast Decode:  disabled
        Profile:  high
        Level:  4.0
    Audio:
        Bitrate:  English (AC3) (5.1 ch) 448 kpbs (48 kHz) -> AAC (avcodec) Stereo 160 kbps
        Gain:  7 dB
        DRC:  4.0
    Subtitles:
        Foreign Audio Scan -> Burned Into Video (Forced Subtitles Only)

* https://trac.ffmpeg.org/wiki/Capture/Desktop
* https://img.ly/blog/ultimate-guide-to-ffmpeg
* https://www.mifi.no/losslesscut
* https://github.com/mifi/lossless-cut
* https://en.wikipedia.org/wiki/LosslessCut
* https://frigate.video


Apt Stuff
---------

* http://www.boehmi.net/index.php/blog/14-how-to-setup-an-apt-cacher-ng-server-in-ubuntu
* https://help.ubuntu.com/community/Apt-Cacher-Server
* `https://help.ubuntu.com/community/AutomateAptCacheNgProxySettings?highlight=%28\bCategoryInternet\b%29`
* http://docs.docker.com/examples/apt-cacher-ng
* https://mikecoats.com/debian-packaging-first-principles-part-1-simple

(on apt-cacher-ng server)::

    apt-get install apt-cacher-ng

(on servers and clients, assuming server is 10.0.2.4)
New file /etc/apt/apt.conf.d/98check-proxy::

    APT::Update::Pre-Invoke {
      "ping -c1 -W1 10.0.2.4; if [ $? == \"0\" ]; then echo \"Acquire::http::Proxy 'http://10.0.2.4:3142'\;\" > /etc/apt/apt.conf.d/99use-proxy; else echo \"\" > /etc/apt/apt.conf.d/99use-proxy; fi"
    }

Install it::

    apt-get install unattended-upgrades

Then enable it::

    dpkg-reconfigure -plow unattended-upgrades

Or, do it manually with::

    # /etc/apt/apt.conf.d/20auto-upgrades
    APT::Periodic::Update-Package-Lists "1";
    APT::Periodic::Unattended-Upgrade "1";

Add other architectures::

    sudo dpkg --add-architecture i386
    sudo apt-get update
    sudo apt-get install libc6:i386 libstdc++6:i386

System76 stuff::

    sudo apt-add-repository ppa:system76-dev/stable

Sigh, Debian::

    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10


LDAP/Kerberos
-------------

* http://aput.net/~jheiss/krbldap/howto.html
* http://www.roguelynn.com/words/explain-like-im-5-kerberos
* https://help.ubuntu.com/lts/serverguide/kerberos-ldap.html
* https://wiki.debian.org/LDAP/Kerberos


Cool Shell Tricks
-----------------

* http://www.theunixschool.com/2012/10/how-to-find-duplicate-records-of-file.html
* http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html
* https://serverfault.com/questions/187712/how-to-determine-if-im-logged-in-via-ssh
* https://github.com/mrmarble/termsvg  Go binary for shell -> asciinema -> SVG
* https://github.com/jlevy/the-art-of-command-line
* https://keepachangelog.com/en  old-school changelogs
* https://www.masteringemacs.org/article/keyboard-shortcuts-every-command-line-hacker-should-know-about-gnu-readline
* https://thevaluable.dev/vim-advanced
* https://unix.stackexchange.com/questions/31947/how-to-add-a-newline-to-the-end-of-a-file/161853#161853
* https://jpospisil.com/2023/12/19/the-hidden-gems-of-moreutils
* https://www.dns.toys  do horrible things using DNS
* https://medium.com/sensorfu/escaping-isolated-networks-using-broadcast-dns-5aee866bcaff
* https://tratt.net/laurie/blog/2024/faster_shell_startup_with_shell_switching.html
* https://github.com/hackerb9/lsix  sixels in terminal windows via imagemagick?
* https://righteousit.com/2024/07/24/hiding-linux-processes-with-bind-mounts

::

    git ls-files -z | while IFS= read -rd '' f; do if file --mime-encoding "$f" | grep -qv binary; then tail -c1 < "$f" | read -r _ || echo >> "$f"; fi; done


Assorted Things-to-Read
-----------------------

* http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1
* http://chris.beams.io/posts/git-commit
* http://lett.be/oauth2
* http://unix.stackexchange.com/questions/66154/ssh-causes-while-loop-to-stop
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it
* https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it
* http://www.velocitypartners.net/blog/2014/04/03/refactoring-and-technical-debt-its-not-a-choice-its-a-responsibility-part-2
* https://github.com/mitchellh/packer/pull/2962
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0
* https://mergeboard.com/blog/2-qemu-microvm-docker
* https://plaintextaccounting.org
* https://www.netmeister.org/blog/inet_aton.html
* https://randsinrepose.com/archives/the-seven-levels-of-busy
* https://kellycordes.com/2009/11/02/the-fun-scale
* https://realreturns.blog/2022/05/08/inbox-diary-to-do-list-now-choose-just-two
* https://sambleckley.com/writing/church-of-interruption.html
* https://tynan.com/letstalk
* https://www.neelnanda.io/blog/43-making-friends
* http://www.structuredprocrastination.com/index.php
* https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office
* https://blog.jim-nielsen.com/2022/what-work-looks-like
* https://github.com/milanm/DevOps-Roadmap#learning-resources-for-devops-engineers-mostly-free
* http://www.coding2learn.org/blog/2013/07/29/kids-cant-use-computers
* https://imgur.com/a/iJD8f  Tales of IT (humour)
* https://imgur.com/a/AOz0d  Tales of IT Part 2 (humour)
* https://gist.github.com/textarcana/676ef78b2912d42dbf355a2f728a0ca1  DevOps Borat "fortune" data file
* https://jasonbock.substack.com/p/if-carpenters-were-hired-like-programmers  humour
* https://futurerack.info/main.php#/products_pets  cat server shelf
* https://fmt2.cat  HE datacentre cats
* https://www.universal-radio.com/cats.html  ham radio store cats
* https://learn.sparkfun.com/tutorials/how-does-an-fpga-work/all
* https://www.onedayyoullfindyourself.com
* https://garnix.io/blog/call-by-hash
* https://writings.stephenwolfram.com/2019/02/seeking-the-productive-life-some-details-of-my-personal-infrastructure
* https://neuroclastic.com/weavers-and-concluders-two-communication-styles-no-one-knows-exist
* https://osintteam.blog/mastering-osint-how-to-find-information-on-anyone-680e4086f17f


Keepass Stuff
-------------

macOS::

    open -a KeePassXC --args --allow-screencapture

* https://keepassxc.org
* https://keepassxc.org/docs/KeePassXC_UserGuide.html#_command_line_options  allow screenshots
* https://github.com/keepassxreboot/keepassxc/issues/4555#issuecomment-610626477  merge dbs in GUI
* https://github.com/keepassxreboot/keepassxc/issues/2937#issuecomment-538592022  merge dbs in TUI
* https://github.com/asmpro/keepasspy
* https://github.com/fdemmer/libkeepass
* https://github.com/jamesls/python-keepassx
* https://github.com/keepassx/keepassx
* https://github.com/kindahl/libkeepass
* https://github.com/phpwutz/libkeepass
* https://gist.github.com/lgg/e6ccc6e212d18dd2ecd8a8c116fb1e45#keepass-file-format-explained
* https://github.com/keepassxreboot/keepassxc/issues/8506
* https://keepassxc.org/docs/KeePassXC_UserGuide.html#_command_line_options


Secret Management Stuff
-----------------------

* https://github.com/sniptt-official/ots
* https://www.sniptt.com/ots
* https://github.com/onetimesecret/onetimesecret
* https://onetimesecret.com
* https://mprimi.github.io/portable-secret
* https://github.com/mprimi/portable-secret
* https://www.franzoni.eu/password-requirements-myths-madness
* https://github.com/slok/agebox  works with SSH pub keys even
* https://github.com/getsops/sops  kubernetes-compatible secret stuff???
* https://embrasure.dev


Cool Products
-------------

* http://nwavguy.blogspot.ca/2011/07/o2-headphone-amp.html
* https://teenage.engineering/products/tx-6  pocket mixer/synth
* https://botblox.io/products/speblox-long  10 Mbps Ethernet over 1 km on a page wire fence???
* https://novamostra.com/2022/10/23/byopm  Pi Zero pocket password manager???
* https://transistor-man.com/lenovo_ebike_adapter.html  DIY DC-DC Thiccpad power brick
* https://beepberry.sqfmi.com
* https://bytewelder.com/posts/2023/05/20/building-a-handheld-pc.html
* https://dynomight.net/better-DIY-air-purifier.html
* https://cast.otter.jetzt  open-source streaming audio gizmos
* https://github.com/Ottercast/OtterCastAudioV2  open-source streaming audio gizmos
* https://liliputing.com/build-your-own-nas-with-this-alder-lake-n-motherboard-up-to-6-hard-drives-and-2-ssds
* https://docs.vorondesign.com/hardware.html#voron-2
* https://blog.arduino.cc/2024/04/23/creating-a-low-cost-ev-charging-station-with-arduino
* https://gitlab.com/zephray/sitina1  open-source DSLR body


Woodworking
-----------

* https://aroundhomediy.com/build-roubo-workbench-leg-vise
* https://www.leevalley.com/en-ca/shop/tools/workshop/workbenches/benches-and-tables/117579-bora-centipede-table?item=99W8349


Kobo Stuff
----------

::

    127.0.0.1 host localhost.localdomain localhost localhost localhost.localdomain
    127.0.0.1 www.google-analytics.com ssl.google-analytics.com google-analytics.com

::

    cd KOBOeReader/.kobo
    sqlite3 KoboReader.sqlite
    INSERT INTO user VALUES('', '', '', '', '', '', '', '', '', '', '', '', '');
    .quit

    -- slightly different instruction found somewhere else
    INSERT INTO user(UserID,UserKey) VALUES('1','');

::

    ebook-convert dummy.html .epub

* https://github.com/olup/kobowriter


RPG Stuff
---------

* https://adventurekeep.com
* https://github.com/stassa/nests-and-insects  TTRPG
* https://gitlab.com/wargames_tex/wargame_tex
* https://gitlab.com/wargames_tex/bfm_tex
* http://www.ericharshbarger.org/dice/go_first_dice.html
* https://elleosiliwood.itch.io/the-missing-locksmith
* https://perchance.org/dnd-draconic-names
* http://mewo2.com/notes/terrain  OMG awesome
* http://mewo2.com/notes/naming-language  OMG awesome
* https://github.com/mewo2/deserts  code for 2 items above
* https://github.com/mewo2/terrain  Jabbascript version??
* https://github.com/mewo2/naming-language  more Jabbascript for name generation??
* https://gist.github.com/munificent/b1bcd969063da3e6c298be070a22b604  random dungeon generator on a business card
* https://olano.dev/blog/deconstructing-the-role-playing-videogame  GURPS, TWERPS, Dinky Dungeons, etc.


Art Stuff
---------

* https://github.com/Acly/krita-ai-diffusion  Krita plugin for inpaint/outpaint within images!!!
* https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog
* https://www.cloudskillsboost.google/paths/118  generative AI learning path
* https://github.com/esimov/triangle  make bitmaps look all triangley
* https://stable-diffusion-art.com/qr-code  artwork which incorporates a QR code into the image
* https://simonwillison.net/2023/Nov/29/llamafile
* https://penrose.cs.cmu.edu  web diagrams from text
* https://voussoir.net/writing/css_for_printing
* https://nfraprado.net/post/vcard-rss-as-an-alternative-to-social-media.html
* https://github.com/vitoplantamura/OnnxStream  Stable Diffusion on Raspberry Pi Zero
* https://www.blocklayer.com/sundial-popeng  paper horizontal sundial generator (not equatorial ones)
* https://github.com/CHAITron/sketchdeco-code  auto-colourizing B&W drawings
* https://sallywolf.ca  flute and recorder lessons


Awesome Stuff
-------------

* http://www.1001fonts.com
* http://hackaday.com/2008/05/29/how-to-super-simple-serial-terminal
* https://github.com/ncrawforth/VT2040  portable serial terminal based on Pico
* https://github.com/vha3/Hunter-Adams-RP2040-Demos  Ethernet and VGA for Pico
* https://axio.ms/projects/2024/06/16/MicroMac.html  Mac 128k on a Pico
* https://github.com/intenthq/anon
* https://nodered.org
* https://github.com/fluent/fluent-bit
* https://lucperkins.dev/blog/introducing-tract
* https://learn.hashicorp.com/tutorials/terraform/count
* https://blog.hansenpartnership.com/creating-a-home-ipv6-network
* https://www.paepper.com/blog/posts/how-to-properly-manage-ssh-keys-for-server-access
* https://medium.com/faun/self-registering-compact-k3os-clusters-to-rancher-server-via-cloud-init-d4a89028c1f8
* https://www.alvarez.io/posts/living-like-it-s-99
* https://www.sliderulemuseum.com/SR_Course.htm
* https://www.youtube.com/watch?v=icyTnoonRqI  K3s and Home Assistant
* https://github.com/mwgg/Airports  JSON database of airport codes and locations
* https://github.com/codecrafters-io/build-your-own-x
* https://www.netmeister.org/blog/ops-lessons.html
* https://roadmap.sh/devops
* https://popovicu.com/posts/making-usb-devices
* https://jamesbvaughan.com/southwest-wifi  probing flight info from in-flight wifi without wasting your money
* https://github.com/NalinPlad/OuterFlightTracker  probing flight info from in-flight wifi without wasting your money
* http://infomatimago.free.fr/i/linux/emacs-on-user-mode-linux.html  Emacs-only typewriter???
* https://www.muckrock.com/news/archives/2024/feb/13/release-notes-how-to-make-self-hosted-maps-that-work-everywhere-cost-next-to-nothing-and-might-even-work-in-airplane-mode
* https://blog.waleson.com/2024/07/security-is-our-top-priority-is-bs.html
* https://github.com/wasi-master/13ft  read articles behind paywalls?
* https://phrack.org/issues/71/17.html#article  financing for hackers?
* https://jaycarlson.net/embedded-linux  low-level Linux board-support magic
* https://billwear.github.io  assorted neat stuff


Microservices
-------------

* https://www.capgemini.com/blog/capping-it-off/2016/02/lego-power-how-to-build-repeatable-microservices-based-infrastructure?utm_content=buffere4cf6&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer
* https://slack.engineering/executing-cron-scripts-reliably-at-scale  k8s queues and jobs


Time-Series and Graphing Considerations
---------------------------------------

* https://www.datadoghq.com/blog/timeseries-metric-graphs-101
* https://www.datadoghq.com/blog/metric-units-descriptions-metadata


Crypto
------

* https://arstechnica.com/information-technology/2016/09/meet-pocketblock-the-crypto-engineering-game-for-kids-of-all-ages
* https://github.com/sustrik/crypto-for-kids
* https://lwn.net/Articles/867158  PAM duress


More
----

* https://davidoha.medium.com/avoiding-bash-frustration-use-python-for-shell-scripts-44bba8ba1e9e
* https://blog.jez.io/bash-debugger
* https://news.ycombinator.com/item?id=36605869  binary payloads at the end of bash scripts
* https://johannes.truschnigg.info/writing/2021-12_colodebug
* https://dzone.com/articles/creating-a-highly-available-k3s-cluster
* https://johansiebens.dev/posts/2020/11/provision-a-multi-region-k3s-cluster-on-google-cloud-with-terraform
* https://thenewstack.io/tutorial-install-a-highly-available-k3s-cluster-at-the-edge
* https://github.com/stephank/lazyssh
* https://jamstack.org
* https://www.wsta.org/wp-content/uploads/2018/09/Best-Practices-for-DevOps-Advanced-Deployment-Patterns.pdf
* https://blog.m3o.com/2020/11/12/netlify-for-the-frontend-micro-for-the-backend.html
* https://blog.linuxserver.io/2021/05/05/meet-webtops-a-linux-desktop-environment-in-your-browser
* https://bou.ke/blog/formulas
* https://news.ycombinator.com/item?id=23643096  less bloated Ansible/SaltStack?
* https://purpleidea.com/projects/mgmt-config  possible replacement for Ansible (Go)
* https://github.com/purpleidea/mgmt  possible replacement for Ansible (Go)
* https://pyinfra.com  another replacement for Ansible?
* https://github.com/debauchee/barrier  open replacement for Synergy
* https://www.brendangregg.com/blog/2024-03-24/linux-crisis-tools.html


Vault Awesome
-------------

* https://sreeninet.wordpress.com/2016/10/01/vault-use-cases
* https://austincloud.guru/2020/03/12/using-vault-with-jenkins


OpenTofu Awesome
----------------

* https://learn.hashicorp.com/tutorials/terraform/sensitive-variables
* https://www.terraform.io/docs/commands/state/rm.html
* https://www.baeldung.com/ops/terraform-best-practices
* https://www.terraform-best-practices.com
* https://bit.ly/terraform-youtube  GH antonbabenko
* https://github.com/antonbabenko
* https://serverless.tf
* https://github.com/terralist/terralist  private module registry


Networking
----------

* https://blog.ikuamike.io/posts/2021/netcat
* https://spiffe.io
* https://www.trickster.dev/post/decrypting-your-own-https-traffic-with-wireshark
* https://sive.rs/com  build a database of domains to make it easier to pick new ones to register
* https://github.com/iovisor/bcc
* https://www.brendangregg.com/blog/2019-08-19/bpftrace.html
* https://www.seekret.io/blog/ebpf-nuances-on-minikube
* https://wicg.github.io/ua-client-hints  User-agent info including stuff like GOOS, GOARCH???
* https://www.scientiamobile.com/introducing-user-agent-client-hints-support-in-wurfl-and-a-rant
* https://docs.google.com/presentation/d/1y_A6VOZy9bD2i0VLHv9ZWr0W3hZJvlTNCDA0itjI0yM/edit?pli=1#slide=id.p19  more WURFL client hints
* https://blog.sigma-star.at/post/2023/05/sandbox-netns  using namespaces to isolate processes
* https://github.com/lizrice/ebpf-beginners  eBPF learning awesome
* https://drgn.readthedocs.io  Linux kernel debugger with Python niceities
* https://blog.cloudnativefolks.org/ebpf-for-cybersecurity-part-1
* https://ebpf.io/what-is-ebpf
* https://who.ldelossa.is/posts  more eBPF/TC low-level learning
* https://media.ccc.de/v/gpn20-41-why-i-wrote-my-own-rsync  router7, distri, gokrazy-rsync, etc.
* https://github.com/zhangjiayin/caddy-geoip2  Caddy module for GeoIP
* https://github.com/gojue/ecapture  eBPF SSL/TLS fun
* https://ecapture.cc  eBPF SSL/TLS fun


Family IT Support Calls
-----------------------

* https://arstechnica.com/features/2021/10/securing-your-digital-life-part-1
* https://arstechnica.com/information-technology/2021/10/securing-your-digital-life-part-2
* https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html
* https://keepassxc.org
* https://keepassxc.org/docs
* https://keepassxc.org/docs/KeePassXC_GettingStarted.html
* https://keepassxc.org/docs/KeePassXC_UserGuide.html
* https://en.wikipedia.org/wiki/Diceware
* https://diceware.dmuth.org
* https://www.eff.org/dice
* https://mango.pdf.zone/operation-luigi-how-i-hacked-my-friend-without-her-noticing
* https://2018.pycon-au.org/talks/41686-operation-luigi-how-i-hacked-my-friend-without-her-noticing
* https://lwn.net/Articles/925870  TOTP
