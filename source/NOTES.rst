Tmux With Terminal Stuff
------------------------

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
* https://aj.codes/posts/be-careful-using-tmux-and-environment-variables/


Game Stuff
----------

* https://github.com/kentonv/lanparty
* https://kilograham.github.io/rp2040-doom/
* https://news.ycombinator.com/item?id=31590724


Video/Audio/Camera Awesome
--------------------------

::

    ffmpeg -i foo.mov -map 0 -c copy foo.mp4
    ffmpeg -i foo.mpg -r 30 -s 960x540 smaller.mp4
    # to alter length of videos, after the -i, add:  '-ss' start time, '-t' duration or '-to' end time
    # put "file 1.mp4\nfile2.mp4" and so on in a list.txt file for the following command...
    ffmpeg -f concat -safe 0 -i list.txt -c copy output.mp4

    cdda2wav -vall cddb=0 speed=4 -paranoia paraopts=proof -B -D /dev/sr0
    flac foo.wav

    ffmpeg -i foo.webm -c copy foo.mp4

Just fix the title of the video file::

    ffmpeg -i input.whatever -copy -map 0 -metadata title='Something else' output.whatever

HandBrake settings for DVDs::

    Summary:
        Format:  MPEG-4 (avformat)
        Web Optimized:  disabled
        Align A/V Start:  enabled
        iPod 5G Support:  disabled
        Passthru Common Metadata:  enabled
    Dimensions:
        Cropping:  None
        Resolution Limit:  720p HD
        Anamorphic:  Automatic
        Optimal Size:  enabled
        Allow Upscaling:  disabled
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
        Constant Framerate:  selected
        RF:  19
        Constant Quality:  selected
        Tune:  None
        Fast Decode:  disabled
        Profile:  hight
        Level:  3.1
    Audio:
        Bitrate:  English (AC3) (5.1 ch) 448 kpbs (48 kHz) -> AAC (avcodec) Stereo 160 kbps
        Gain:  7 dB
        DRC:  4.0
    Subtitles:
        Foreign Audio Scan -> Burned Into Video (Forced Subtitles Only)

* https://frigate.video/
* https://mifi.github.io/lossless-cut/
* https://pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/
* https://people.skolelinux.org/pere/blog/Managing_and_using_ONVIF_IP_cameras_with_Linux.html
* https://ibm-research.medium.com/ibm-open-sources-300-fully-functional-lego-microscope-design-248a6cdc81bf
* https://img.ly/blog/ultimate-guide-to-ffmpeg/
* https://jakecoppinger.com/2022/12/creating-aerial-imagery-with-a-bike-helmet-camera-and-opendronemap/
* https://joshuabird.com/blog/post/3d-printed-film-video-camera


Apt Stuff
---------

* http://www.boehmi.net/index.php/blog/14-how-to-setup-an-apt-cacher-ng-server-in-ubuntu
* https://help.ubuntu.com/community/Apt-Cacher-Server
* https://help.ubuntu.com/community/AutomateAptCacheNgProxySettings?highlight=%28\bCategoryInternet\b%29
* http://docs.docker.com/examples/apt-cacher-ng/

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


Official OS Images
------------------

* https://github.com/debuerreotype/debuerreotype  Debian et al.
* https://github.com/debuerreotype/docker-debian-artifacts  Debian
* https://github.com/tianon/docker-brew-ubuntu-core  Ubuntu
* https://github.com/alpinelinux/docker-alpine  Alpine Linux
* https://partner-images.canonical.com/oci/  Ubuntu root fs tarballs for containers "FROM scratch"
* https://cloud-images.ubuntu.com/  OVA, VDI, IMG, etc.
* https://cloud-images.ubuntu.com/locator/  AMIs, etc.
* https://hub.docker.com/_/debian/  Voldemorthub Debian
* https://hub.docker.com/_/ubuntu/  Voldemorthub Ubuntu
* https://hub.docker.com/_/alpine/  Voldemorthub Alpine

Typical OS container image "Dockerfile"::

    FROM scratch
    ADD ${DISTRO}-${ARCH}-rootfs.tar.gz
    CMD ["bash"]


LDAP/Kerberos
-------------

* http://aput.net/~jheiss/krbldap/howto.html
* http://www.roguelynn.com/words/explain-like-im-5-kerberos/
* https://help.ubuntu.com/lts/serverguide/kerberos-ldap.html
* https://wiki.debian.org/LDAP/Kerberos


Cool Shell Tricks
-----------------

* http://www.theunixschool.com/2012/10/how-to-find-duplicate-records-of-file.html
* http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html
* https://til.simonwillison.net/sqlite/one-line-csv-operations  SQL queries on CSV files
* https://serverfault.com/questions/187712/how-to-determine-if-im-logged-in-via-ssh
* https://github.com/mrmarble/termsvg  Go binary for shell -> asciinema -> SVG
* https://sharats.me/posts/shell-script-best-practices/
* https://github.com/jlevy/the-art-of-command-line
* https://keepachangelog.com/en  old-school changelogs
* https://www.masteringemacs.org/article/keyboard-shortcuts-every-command-line-hacker-should-know-about-gnu-readline
* https://thevaluable.dev/vim-advanced/


Assorted Things-to-Read
-----------------------

* http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
* http://chris.beams.io/posts/git-commit/
* http://lett.be/oauth2/
* http://unix.stackexchange.com/questions/66154/ssh-causes-while-loop-to-stop
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it/
* https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it/
* http://www.velocitypartners.net/blog/2014/04/03/refactoring-and-technical-debt-its-not-a-choice-its-a-responsibility-part-2/
* https://github.com/mitchellh/packer/pull/2962
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0
* https://mergeboard.com/blog/2-qemu-microvm-docker/
* https://plaintextaccounting.org/
* https://www.netmeister.org/blog/inet_aton.html
* https://randsinrepose.com/archives/the-seven-levels-of-busy/
* https://kellycordes.com/2009/11/02/the-fun-scale/
* https://realreturns.blog/2022/05/08/inbox-diary-to-do-list-now-choose-just-two/
* https://sambleckley.com/writing/church-of-interruption.html
* https://tynan.com/letstalk/
* https://www.neelnanda.io/blog/43-making-friends
* http://www.structuredprocrastination.com/index.php
* https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/
* https://blog.jim-nielsen.com/2022/what-work-looks-like/
* https://github.com/milanm/DevOps-Roadmap#learning-resources-for-devops-engineers-mostly-free
* http://www.coding2learn.org/blog/2013/07/29/kids-cant-use-computers/
* https://imgur.com/a/iJD8f  Tales of IT (humour)
* https://imgur.com/a/AOz0d  Tales of IT Part 2 (humour)


MySQL Stuff
-----------

::

    select concat('KILL ',id,';') from information_schema.processlist where command='Sleep';

::

    #!/bin/bash

    echo "Killing existing xlsws_category queries"
    for process_id in `mysql -e "show full processlist" | grep 'xlsws_category' | awk '{print $1}'`
    do
        echo "- process: ${process_id}"
        mysql -e "kill ${process_id}"
    done


Keepass Stuff
-------------

macOS::

    open -a KeePassXC --args --allow-screencapture

* https://keepassxc.org/
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
* https://www.sniptt.com/ots/
* https://github.com/onetimesecret/onetimesecret
* https://onetimesecret.com/
* https://mprimi.github.io/portable-secret/
* https://github.com/mprimi/portable-secret
* https://www.franzoni.eu/password-requirements-myths-madness/


Cool Products
-------------

* http://nwavguy.blogspot.ca/2011/07/o2-headphone-amp.html
* https://teenage.engineering/products/tx-6  pocket mixer/synth
* https://botblox.io/products/speblox-long  10 Mbps Ethernet over 1 km on a page wire fence???
* https://novamostra.com/2022/10/23/byopm/  Pi Zero pocket password manager???


Keyboard CNC
------------

* https://geekhack.org/index.php?topic=65747.0


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

::

    ebook-convert dummy.html .epub

* https://github.com/olup/kobowriter


RPG Stuff
---------

* https://adventurekeep.com/
* https://github.com/stassa/nests-and-insects  TTRPG
* https://gitlab.com/wargames_tex/wargame_tex
* https://gitlab.com/wargames_tex/bfm_tex
* http://www.ericharshbarger.org/dice/go_first_dice.html
* https://elleosiliwood.itch.io/the-missing-locksmith
* https://perchance.org/dnd-draconic-names


Awesome Stuff
-------------

* http://www.1001fonts.com/
* http://hackaday.com/2008/05/29/how-to-super-simple-serial-terminal/
* https://github.com/ncrawforth/VT2040  portable serial terminal based on Pico
* https://github.com/intenthq/anon
* https://nodered.org/
* https://github.com/fluent/fluent-bit
* https://lucperkins.dev/blog/introducing-tract/
* https://learn.hashicorp.com/tutorials/terraform/count
* https://blog.hansenpartnership.com/creating-a-home-ipv6-network/
* https://www.paepper.com/blog/posts/how-to-properly-manage-ssh-keys-for-server-access/
* https://medium.com/faun/self-registering-compact-k3os-clusters-to-rancher-server-via-cloud-init-d4a89028c1f8
* https://www.alvarez.io/posts/living-like-it-s-99/
* https://www.sliderulemuseum.com/SR_Course.htm
* https://www.youtube.com/watch?v=icyTnoonRqI  K3s and Home Assistant
* https://github.com/mwgg/Airports  JSON database of airport codes and locations
* https://github.com/codecrafters-io/build-your-own-x
* https://www.netmeister.org/blog/ops-lessons.html
* https://roadmap.sh/devops
* https://www.shruggingface.com/blog/how-i-used-stable-diffusion-and-dreambooth-to-create-a-painted-portrait-of-my-dog


Microservices
-------------

* https://www.capgemini.com/blog/capping-it-off/2016/02/lego-power-how-to-build-repeatable-microservices-based-infrastructure?utm_content=buffere4cf6&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer


Time-Series and Graphing Considerations
---------------------------------------

* https://www.datadoghq.com/blog/timeseries-metric-graphs-101/
* https://www.datadoghq.com/blog/metric-units-descriptions-metadata/


Crypto
------

* https://arstechnica.com/information-technology/2016/09/meet-pocketblock-the-crypto-engineering-game-for-kids-of-all-ages/
* https://github.com/sustrik/crypto-for-kids
* https://lwn.net/Articles/867158/  PAM duress


More
----

* https://davidoha.medium.com/avoiding-bash-frustration-use-python-for-shell-scripts-44bba8ba1e9e
* https://blog.jez.io/bash-debugger/
* https://johannes.truschnigg.info/writing/2021-12_colodebug/
* https://dzone.com/articles/creating-a-highly-available-k3s-cluster
* https://johansiebens.dev/posts/2020/11/provision-a-multi-region-k3s-cluster-on-google-cloud-with-terraform/
* https://thenewstack.io/tutorial-install-a-highly-available-k3s-cluster-at-the-edge/
* https://github.com/stephank/lazyssh
* https://jamstack.org/
* https://www.wsta.org/wp-content/uploads/2018/09/Best-Practices-for-DevOps-Advanced-Deployment-Patterns.pdf
* https://blog.m3o.com/2020/11/12/netlify-for-the-frontend-micro-for-the-backend.html
* https://blog.linuxserver.io/2021/05/05/meet-webtops-a-linux-desktop-environment-in-your-browser/
* https://bou.ke/blog/formulas/
* https://news.ycombinator.com/item?id=23643096  less bloated Ansible/SaltStack?
* https://pyinfra.com/  another replacement for Ansible?


Container Stuff
---------------

* https://www.kubernetes.dev/blog/2023/03/01/introducing-kwok/
* https://containers.gitbook.io/build-containers-the-hard-way/#walk-through-pulling-an-image-with-bash
* https://github.com/google/go-containerregistry#tools
* https://github.com/ko-build/ko#ko-easy-go-containers
* https://github.com/containers/skopeo
* https://github.com/jpetazzo/registrish
* https://www.gnu.org/software/guix/blog/2018/tarballs-the-ultimate-container-image-format/
* https://blog.yadutaf.fr/2016/04/14/docker-for-your-users-introducing-user-namespace/
* https://42notes.wordpress.com/2015/05/13/replace-boot2docker-with-coreos-and-vagrant-to-use-docker-containers/
* http://www.iron.io/blog/2016/01/microcontainers-tiny-portable-containers.html
* http://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container/
* http://prakhar.me/docker-curriculum/
* http://stackoverflow.com/questions/18274088/how-can-i-make-my-own-base-image-for-docker
* http://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html
* http://www.aossama.com/build-debian-docker-image-from-scratch/
* https://blog.docker.com/2013/06/create-light-weight-docker-containers-buildroot/
* https://developer.atlassian.com/blog/2015/12/atlassian-docker-orchestration/
* https://github.com/openshift-evangelists/openshift-workshops/blob/master/modules/run-as-non-root.adoc#switching-the-user
* https://docs.openshift.org/latest/creating_images/guidelines.html#use-uid
* http://www.projectatomic.io/docs/docker-image-author-guidance/
* https://www.ctl.io/developers/blog/post/gracefully-stopping-docker-containers/
* https://www.ctl.io/developers/blog/post/dockerfile-entrypoint-vs-cmd
* https://blog.feabhas.com/2017/10/introduction-docker-embedded-developers-part-2-building-images/
* https://wiki.apache.org/httpd/NonRootPortBinding
* https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose
* https://erkanerol.github.io/post/how-kubectl-exec-works/
* https://www.youtube.com/watch?v=g4PCTodIm80  Why I use Rancher (2021) - Fleet awesomeness
* https://www.hashicorp.com/resources/hashinetes-combining-kubernetes-hashicorp-kelsey-hightower  Hashinetes
* https://www.youtube.com/watch?v=_dn4c9j7LUo
* https://github.com/containerd/nerdctl
* https://marcusnoble.co.uk/2021-09-01-migrating-from-docker-to-podman/
* https://itnext.io/goodbye-docker-desktop-hello-minikube-3649f2a1c469
* https://github.com/k8s-at-home/charts
* https://github.com/k8s-at-home/awesome-home-kubernetes
* https://billglover.me/2020/01/12/the-sidecar-pattern/
* https://github.com/ramitsurana/awesome-kubernetes
* https://ramitsurana.github.io/awesome-kubernetes
* https://github.com/run-x/awesome-kubernetes
* https://awesome-kubernetes.com/
* https://earthly.dev/blog/aws-lambda-docker/
* https://github.com/cloudposse/charts/tree/master/incubator/monochart  monochart
* https://github.com/itscontained/charts/tree/master/itscontained/raw  rawchart
* https://itnext.io/3-reasons-to-choose-a-wide-cluster-over-multi-cluster-with-kubernetes-c923fecf4644
* https://iximiuz.com/en/posts/container-networking-is-simple/
* https://www.youtube.com/watch?v=k58WnbKmjdA&feature=emb_logo
* https://nix.dev/tutorials/building-and-running-docker-images
* https://ianthehenry.com/posts/how-to-learn-nix/
* https://github.com/tianon/gosu
* https://docs.gocd.org/current/
* https://github.com/routernetes/routernetes  dedicated router with k8s???
* https://k8s.voltaicforge.com/  PXE boot bare metal + install Talos, Sidero, K8s
* https://driftingin.space/posts/complexity-kubernetes
* https://github.com/containers/skopeo/blob/main/docs/skopeo-standalone-sign.1.md#notes
* https://www.ianlewis.org/en/container-runtimes-part-2-anatomy-low-level-contai
* https://blog.ttulka.com/building-container-images-without-dockerfile/
* https://iximiuz.com/en/posts/container-learning-path/
* https://cast.ai/blog/kubernetes-cordon-how-it-works-and-when-to-use-it/
* https://determinate.systems/posts/nix-to-kubernetes
* https://httptoolkit.com/blog/docker-image-registry-facade/


Load-Balancing
--------------

* https://metallb.org/
* https://fabiolb.net/  uses HashiCorp Consul
* https://www.loxilb.io/  uses eBPF
* https://ebpf.io/
* https://samwho.dev/load-balancing/  visualization of different load-balancing strategies


Vault Awesome
-------------

* https://sreeninet.wordpress.com/2016/10/01/vault-use-cases/
* https://austincloud.guru/2020/03/12/using-vault-with-jenkins/


Terraform Awesome
-----------------

* https://learn.hashicorp.com/tutorials/terraform/sensitive-variables
* https://www.terraform.io/docs/commands/state/rm.html
* https://www.baeldung.com/ops/terraform-best-practices


Networking
----------

* https://blog.ikuamike.io/posts/2021/netcat/
* https://spiffe.io/
* https://www.trickster.dev/post/decrypting-your-own-https-traffic-with-wireshark/
* https://sive.rs/com  build a database of domains to make it easier to pick new ones to register
* https://github.com/iovisor/bcc
* https://www.brendangregg.com/blog/2019-08-19/bpftrace.html
* https://www.seekret.io/blog/ebpf-nuances-on-minikube/
* https://wicg.github.io/ua-client-hints/  User-agent info including stuff like GOOS, GOARCH???
* https://www.scientiamobile.com/introducing-user-agent-client-hints-support-in-wurfl-and-a-rant/
* https://docs.google.com/presentation/d/1y_A6VOZy9bD2i0VLHv9ZWr0W3hZJvlTNCDA0itjI0yM/edit?pli=1#slide=id.p19  more WURFL client hints


Go Stuff
--------

::

    go tool list dist            # show supported OS/ARCH combos
    go build                     # compile everything
    go version -m foo            # show build info packed into the binary
    go clean                     # clean up everything

    go get -u all ; go mod tidy  # upgrade all dependencies to latest
    go mod vendor                # vendor (copy) all dependencies locally
    go vet                       # do some linting/checking
    go fmt *.go                  # style the code

* https://opensource.com/article/22/4/go-build-options
* http://howistart.org/posts/go/1
* https://www.youtube.com/watch?v=oyTgx6S87XY
* https://www.youtube.com/watch?v=ysgMlGHtDMo
* https://benhoyt.com/writings/prig/?showhn  Go AWK
* https://towardsdatascience.com/how-to-create-a-cli-in-golang-with-cobra-d729641c7177
* https://jogendra.dev/building-command-line-tools-in-go
* https://coder.com/blog/building-command-line-tools-with-go
* https://gocli.io/
* https://github.com/tmrts/boilr
* https://quii.gitbook.io/learn-go-with-tests/
* https://github.com/jltorresm/otpgo  TOTP
* https://github.com/pquerna/otp  TOTP
* https://go.dev/ref/mod
* https://roberto.selbach.ca/go-proxies/
* https://stackoverflow.com/questions/65921916/why-does-go-module-ssh-custom-private-repo-non-github-config-still-request-htt
* https://awesome-go.com/
* https://www.awesomego.net/
* https://github.com/felixge/fgtrace  Go tracing
* https://github.com/nikolaydubina/go-recipes
* https://golang.ch/a-tiny-web-application-golang-showcases-best-practices-of-running-microservices-in-kubernetes/?amp=1
* https://gist.github.com/fsmv/02c636d4da58106f113049ee45a62f50  go run???
* https://www.arp242.net/flags-config-go.html  config stuff
* https://github.com/arp242/sconfig
* https://paulgorman.org/technical/blog/20171113164018.html  maybe the best config???
* https://paseto.io/  JWT/JOSE stuff
* https://drstearns.github.io/tutorials/gojson/
* https://github.com/awsdocs/aws-lambda-developer-guide/blob/main/sample-apps/blank-go/function/main.go
* https://tailscale.com/blog/netaddr-new-ip-type-for-go/  IP stuff
* https://stackoverflow.com/questions/19882961/go-golang-check-ip-address-in-range  IP stuff
* https://pkg.go.dev/net/netip  IP stuff
* https://pkg.go.dev/net  IP stuff
* https://hmarr.com/blog/go-allocation-hunting/
* https://otterize.com/blog/golang-contexts-and-blocking-functions


Your Mom
--------

* https://arstechnica.com/features/2021/10/securing-your-digital-life-part-1/
* https://arstechnica.com/information-technology/2021/10/securing-your-digital-life-part-2/
* https://www.schneier.com/blog/archives/2014/03/choosing_secure_1.html
* https://mango.pdf.zone/operation-luigi-how-i-hacked-my-friend-without-her-noticing
* https://2018.pycon-au.org/talks/41686-operation-luigi-how-i-hacked-my-friend-without-her-noticing/
* http://infomatimago.free.fr/i/linux/emacs-on-user-mode-linux.html  Emacs-only typewriter???


Ham Stuff
---------

* https://github.com/flwyd/adif-multitool  convert ADIF to/from CSV
* https://github.com/k0swe/adi2cbr  convert ADIF to Cabrillo
* https://github.com/oIdq/qsls  convert ADIF to PDF
* https://github.com/Matir/adifparser
* https://github.com/tzneal/ham-go
* https://pypi.org/project/adif-io/
* https://github.com/xaratustrah/dolphinlog  Python SQLite logger with ADIF 3.x.x export
* https://github.com/sq8kfh/hamutils  another Python library for dealing with logs
* https://github.com/timseed/adif_to_csv
* https://github.com/Ewpratten/adif-rs  no ADIF 3.x.x support
* https://github.com/davepacheco/rust-adif
* http://www.adif.org/
* `https://wikitia.com/wiki/Amateur_Data_Interchange_Format_(ADIF)`
* https://youtu.be/nkUR31fj9Xw  OHIS Open Headset Interconnect Standard
* https://github.com/Halibut-Electronics/Open-Headset-Interconnect-Standard  OHIS
* https://github.com/skuep/AIOC  cheaper APRS?
* https://github.com/phase4ground/opv-cxx-demod
* https://github.com/eleccoder/raspi-pico-aprs-tnc
* https://www.commswg.site/_amateur_radio/mmdvm_duplex.shtml
* https://github.com/VE2ZAZ/VHF_Contest_Logger_Software
* https://github.com/BrucePerens/rigcontrol
* https://www.youtube.com/watch?v=wUQsfDX1AnU  presentation about BrucePerens/rigcontrol
* `https://training.emergencymanagementontario.ca/GTFlex/GTOnline.dll/PublicCourse/COURSENO=COUR2009042216173303341001#`  IMS 100 self-study course
* https://www.onallbands.com/simple-filters-from-transmission-line-stubs/  coax stub filters
* http://www.k1ttt.net/technote/k2trstub.html  coax stub filters
* https://www.n1nc.org/Filters/  ugly filter project
* https://groups.io/g/TXBPF/message/3034  W3NQN-compatible filters with a more reasonable price tag
* https://www.arraysolutions.com/filters/bpf-hpf  insanely-expensive filters
* https://www.youtube.com/watch?v=D1LYLDGknOY  KA9Q-Radio


Ribbit
------

This might actually be awesome if they ever post the source code and put the app up on F-Droid.org (and make some more non-Android versions too).
The current closed-source app is called "Rattlegram" on The Poodle Grey Store.

* https://www.ribbitradio.org/  official site
* https://github.com/aicodix/rattlegram  holy frickin' moley!!! source code!!!
* https://github.com/phase4ground/ribbit  possible location for source code... eventually???
* https://www.youtube.com/watch?v=_jN4IVccIEw  initial presentation video
* https://wze95h.qsotodayhamexpo.com/sessionInfo/ribbit_a_new  presentation slides (PDF)
