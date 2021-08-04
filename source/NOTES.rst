LANParty Automation
-------------------

* https://github.com/kentonv/lanparty


Magnetometer
------------

* https://github.com/keepworking/Mecha_QMC5883L
* https://github.com/e-Gizmo/QMC5883L-GY-271-Compass-module


Python Stuff
------------

* http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
* http://flask-restful.readthedocs.org/en/0.3.5/quickstart.html#a-minimal-api
* http://locust.io/
* https://pypi.python.org/pypi/pip2pi/0.6.8
* https://github.com/pypiserver/pypiserver
* http://book.pythontips.com/en/latest/
* http://qpleple.com/add-progress-bars-to-your-python-loops/
* https://click.palletsprojects.com/en/7.x/utils/#showing-progress-bars
* https://codingdose.info/2019/06/15/how-to-use-a-progress-bar-in-python/
* https://github.com/niltonvolpato/python-progressbar/blob/master/examples.py

::

    import itertools

    for perm in itertools.permutations("thing to use for anagram"):
        print(''.join(perm))

    # Examples:
    # "setec astronomy" is an anagram for "too many secrets"
    # "keynote shogun" is an anagram for "not enough keys"


Go Stuff
--------

* http://howistart.org/posts/go/1
* https://www.youtube.com/watch?v=oyTgx6S87XY
* https://www.youtube.com/watch?v=ysgMlGHtDMo


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


Container Stuff
---------------

* https://blog.yadutaf.fr/2016/04/14/docker-for-your-users-introducing-user-namespace/
* https://42notes.wordpress.com/2015/05/13/replace-boot2docker-with-coreos-and-vagrant-to-use-docker-containers/
* http://www.iron.io/blog/2016/01/microcontainers-tiny-portable-containers.html
* http://blog.xebia.com/2014/07/04/create-the-smallest-possible-docker-container/
* http://prakhar.me/docker-curriculum/
* http://stable.release.core-os.net/amd64-usr/current/
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
* https://success.docker.com/article/Docker_Reference_Architecture-_Design_Considerations_and_Best_Practices_to_Modernize_Traditional_Apps_(MTA)_with_Docker_EE
* https://wiki.apache.org/httpd/NonRootPortBinding
* https://nickjanetakis.com/blog/best-practices-around-production-ready-web-apps-with-docker-compose
* https://erkanerol.github.io/post/how-kubectl-exec-works/


Official Docker OS Images
-------------------------

* https://github.com/debuerreotype/debuerreotype
* https://github.com/debuerreotype/docker-debian-artifacts
* https://github.com/CentOS/sig-cloud-instance-build
* https://github.com/CentOS/sig-cloud-instance-images


System76 Stuff
--------------

::

    sudo apt-add-repository ppa:system76-dev/stable


Android Stuff
-------------

::

    sudo dpkg --add-architecture i386
    sudo apt-get update 
    sudo apt-get install libc6:i386 libstdc++6:i386


LDAP/Kerberos
-------------

* http://aput.net/~jheiss/krbldap/howto.html
* http://www.roguelynn.com/words/explain-like-im-5-kerberos/
* https://help.ubuntu.com/lts/serverguide/kerberos-ldap.html
* https://wiki.debian.org/LDAP/Kerberos


Stupid Shell Tricks
-------------------

* http://www.theunixschool.com/2012/10/how-to-find-duplicate-records-of-file.html
* http://www.theunixschool.com/2012/09/grep-vs-awk-examples-for-pattern-search.html


Backups
-------

* http://duplicity.nongnu.org/features.html
* http://www.mikerubel.org/computers/rsync_snapshots/
* https://blog.interlinked.org/tutorials/rsync_time_machine.html


Assorted Things-to-Read
-----------------------

* http://bitquabit.com/post/having-fun-python-and-elasticsearch-part-1/
* http://blogs.aws.amazon.com/security/post/Tx2MUS2R3CMGG8H/Enable-a-New-Feature-in-the-AWS-Management-Console-Cross-Account-Access
* http://chris.beams.io/posts/git-commit/
* http://lett.be/oauth2/
* http://randsinrepose.com/archives/bored-people-quit/
* http://randsinrepose.com/archives/the-update-the-vent-and-the-disaster/
* http://unix.stackexchange.com/questions/66154/ssh-causes-while-loop-to-stop
* http://www.daedtech.com/how-to-keep-your-best-programmers
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it/
* https://aws.amazon.com/blogs/aws/new-amazon-elasticsearch-service/
* https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying
* https://medium.com/swlh/agile-is-the-new-waterfall-f7baef5d026d
* http://redsquirrel.com/dave/work/a2j/patterns/BreakableToys.html
* http://blog.fogcreek.com/how-to-onboard-software-engineers-interview-with-kate-heddleston/
* http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html
* http://redsquirrel.com/dave/work/a2j/patterns/DrawYourOwnMap.html
* http://redsquirrel.com/dave/work/a2j/patterns/SustainableMotivations.html
* http://www.programblings.com/2014/09/17/logstash-you-dont-need-to-deploy-it-to-use-it/
* http://www.velocitypartners.net/blog/2014/04/03/refactoring-and-technical-debt-its-not-a-choice-its-a-responsibility-part-2/
* https://github.com/mitchellh/packer/pull/2962
* https://kateheddleston.com/blog/onboarding-and-the-cost-of-team-debt
* https://www.edx.org/course/introduction-linux-linuxfoundationx-lfs101x-0
* https://www.tinypulse.com/blog/sk-every-employee-onboarding-tip-youll-need
* https://skamille.medium.com/an-incomplete-list-of-skills-senior-engineers-need-beyond-coding-8ed4a521b29f
* https://gettys.wordpress.com/2018/02/11/the-blind-men-and-the-elephant/
* https://mergeboard.com/blog/2-qemu-microvm-docker/


Stuff to watch
--------------

* https://labs.spotify.com/2014/03/27/spotify-engineering-culture-part-1/


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

* http://blog.sharedmemory.fr/en/2014/04/30/keepass-file-format-explained/
* https://github.com/asmpro/keepasspy
* https://github.com/fdemmer/libkeepass
* https://github.com/jamesls/python-keepassx
* https://github.com/keepassx/keepassx
* https://github.com/kindahl/libkeepass
* https://github.com/phpwutz/libkeepass
* https://keepassxc.org/


Cool Products
-------------

* http://nwavguy.blogspot.ca/2011/07/o2-headphone-amp.html


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


Awesome Stuff
-------------

* http://www.1001fonts.com/
* http://hackaday.com/2008/05/29/how-to-super-simple-serial-terminal/
* http://gohugo.io/
* https://www.gnu.org/software/guix/blog/2018/tarballs-the-ultimate-container-image-format/
* https://github.com/intenthq/anon
* https://nodered.org/
* https://en.wikipedia.org/wiki/FreeRTOS
* https://aws.amazon.com/freertos/
* https://adventurekeep.com/
* https://github.com/fluent/fluent-bit
* https://github.com/codahale/sneaker
* https://www.threatstack.com/blog/cloud-security-best-practices-finding-securing-managing-secrets-part-2
* https://lucperkins.dev/blog/introducing-tract/
* https://learn.hashicorp.com/tutorials/terraform/count
* https://blog.hansenpartnership.com/creating-a-home-ipv6-network/
* https://www.paepper.com/blog/posts/how-to-properly-manage-ssh-keys-for-server-access/
* https://www.commswg.site/_amateur_radio/mmdvm_duplex.shtml
* https://medium.com/faun/self-registering-compact-k3os-clusters-to-rancher-server-via-cloud-init-d4a89028c1f8


Git Stuff
---------

::

    # Snip out just a single directory
    git clone foo
    cd foo
    git remote rm origin
    git filter-branch --subdirectory-filter arf --prune-empty -- --all


    # Get rid of files permanently
    for i in foo.svg bar.svg ; do
        git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch $i" --tag-name-filter cat --prune-empty --force -- --all --branches --tags
    done


    # Fix the size of the repository by losing unreferenced things
    git reflog expire --expire=now --all
    git fsck --full --unreachable
    git gc --prune=now --aggressive

    rm -rf .git/refs/original/ .git/refs/remotes/ .git/*_HEAD .git/logs/
    git reflog expire --expire-unreachable=now --all
    git repack -q -A -d
    git gc --aggressive --prune=now

    rm -rf .git/refs/original/*
    git reflog expire --all --expire-unreachable=0
    git repack -A -d
    git prune


    # Fix author/committer user.name/user.email for old commits
    git filter-branch --env-filter 'GIT_AUTHOR_NAME="Tyler Tidman" ; GIT_COMMITTER_NAME="Tyler Tidman"' -f -- --all
    git filter-branch --env-filter 'GIT_AUTHOR_EMAIL="tyler.tidman@draak.ca" ; GIT_COMMITTER_EMAIL="tyler.tidman@draak.ca"' -f -- --all
    git show-ref
    # Delete any refs that have the name "original"
    git update-ref -d refs/original/refs/heads/master


    # Cull a single directory
    git filter-branch --tree-filter 'rm -rf radio/logos/ares' -f HEAD
    git filter-branch --prune-empty -f HEAD


    # Stitch two repos together
    cd Adir
    mkdir Bdir
    git remote add -f Bproject /path/to/Brepo
    git merge --allow-unrelated-histories -s ours --no-commit Bproject/master
    git read-tree --prefix=Bdir -u Bproject/master
    git commit -m "Merge B project as our subdirectory"
    git pull -s subtree Bproject master


    # Rewrite an older commit
    git rebase --interactive deadbeef^
    # edit stuff
    git commit --all --amend --no-edit
    git rebase --continue


Style Guide Stuff
-----------------

* bashate (former bash8)
* https://github.com/bahamas10/bash-style-guide
* http://wiki.bash-hackers.org/scripting/style
* https://google.github.io/styleguide/shell.xml


Elasticsearch
-------------

* https://youtu.be/cn7QLSPB3OA
* http://www.slideshare.net/AmazonWebServices/aws-october-webinar-series-introducing-amazon-elasticsearch-service


Cloud Hybrid
------------

* https://youtu.be/tIDbFTIPolQ
* http://www.slideshare.net/AmazonWebServices/february-2016-webinar-series-use-aws-cloud-storage-as-the-foundation-for-hybrid-strategy


Microservices
-------------

* https://www.capgemini.com/blog/capping-it-off/2016/02/lego-power-how-to-build-repeatable-microservices-based-infrastructure?utm_content=buffere4cf6&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer


SSH
---

::

    Use the undocumented option "UseRoaming=no'  on the command line: 
    example: ssh -oUseRoaming=no pacharest@mc.pubb-it.com

    Or, force the option for all future outgoing connections : 
    Edit the /etc/ssh/ssh_config or ~/.ssh/config file to add "UseRoaming no" under the "Host *" section. 


Time-Series and Graphing Considerations
---------------------------------------

* https://www.datadoghq.com/blog/timeseries-metric-graphs-101/
* https://www.datadoghq.com/blog/metric-units-descriptions-metadata/


Cloud Backup and Recovery
-------------------------

* http://www.slideshare.net/AmazonWebServices/aws-march-2016-webinar-series-best-practices-for-architecting-cloud-backup-and-recovery-solutions


Crypto
------

* https://arstechnica.com/information-technology/2016/09/meet-pocketblock-the-crypto-engineering-game-for-kids-of-all-ages/
* https://github.com/sustrik/crypto-for-kids


Kanban
------

* https://github.com/greggigon/my-personal-kanban
* http://greggigon.github.io/my-personal-kanban/
* https://my-personal-kanban.appspot.com/

::

    cat all-kanbans-export.json | jq -r '.[].columns[].cards[].name' > todo.txt


More
----

* https://davidoha.medium.com/avoiding-bash-frustration-use-python-for-shell-scripts-44bba8ba1e9e
* https://blog.jez.io/bash-debugger/
* https://dzone.com/articles/creating-a-highly-available-k3s-cluster
* https://johansiebens.dev/posts/2020/11/provision-a-multi-region-k3s-cluster-on-google-cloud-with-terraform/
* https://thenewstack.io/tutorial-install-a-highly-available-k3s-cluster-at-the-edge/
* https://github.com/stephank/lazyssh
* https://jamstack.org/
* https://www.wsta.org/wp-content/uploads/2018/09/Best-Practices-for-DevOps-Advanced-Deployment-Patterns.pdf
* https://blog.m3o.com/2020/11/12/netlify-for-the-frontend-micro-for-the-backend.html
* https://blog.linuxserver.io/2021/05/05/meet-webtops-a-linux-desktop-environment-in-your-browser/
* https://bou.ke/blog/formulas/


Books
-----

* https://www.amazon.com/Collaborating-Enemy-People-Agree-Trust/dp/1626568227/ref=sr_1_1?dchild=1&keywords=working+with+the+enemy&qid=1611248468&sr=8-1
* https://www.amazon.com/Ministry-Common-Sense-Eliminate-Bureaucratic/dp/0358272564


Container Awesome
-----------------

* https://iximiuz.com/en/posts/container-networking-is-simple/
* https://www.youtube.com/watch?v=k58WnbKmjdA&feature=emb_logo


Vault Awesome
-------------

* https://sreeninet.wordpress.com/2016/10/01/vault-use-cases/
* https://austincloud.guru/2020/03/12/using-vault-with-jenkins/


Terraform Awesome
-----------------

* https://learn.hashicorp.com/tutorials/terraform/sensitive-variables
* https://www.terraform.io/docs/commands/state/rm.html
* https://www.baeldung.com/ops/terraform-best-practices
