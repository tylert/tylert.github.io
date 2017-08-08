* http://www.codeandcompost.com/post/a-safe-place-to-log,-part-01
* https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/
* https://launchbylunch.com/posts/2014/Jan/29/aws-tips/
* http://cloudacademy.com/blog/centralized-log-management-with-aws-cloudwatch-part-3-of-3/
* http://cloudacademy.com/blog/aws-cloudwatch-monitoring/

* http://stable.release.core-os.net/amd64-usr/current/
* http://beta.release.core-os.net/amd64-usr/current/
* http://alpha.release.core-os.net/amd64-usr/current/

* https://coreos.com/os/docs/latest/booting-on-vagrant.html
* https://github.com/coreos/coreos-vagrant.git
* https://github.com/vulcand/vulcand

::

    git clone http://github.com/coreos/coreos-vagrant.git
    vagrant up

    vagrant ssh core-01
    vagrant ssh core-02
    vagrant ssh core-03

    export DOCKER_HOST=tcp://172.17.8.101:2375
    docker run -i -t ubuntu:14.04.4 /bin/bash
    docker run -i -t ubuntu:16.04 /bin/bash


Consul Stuff
------------

::

    consul agent -dev -bind=10.80.0.22


Random Other Docs
-----------------

* http://blog.dixo.net/2015/02/load-balancing-with-coreos
* http://blog.michaelhamrah.com/2014/11/running-consul-on-coreos/
* http://blog.scottlowe.org/2015/02/06/quick-intro-to-consul/
* http://blog.scottlowe.org/2015/03/06/running-own-docker-swarm-cluster/
* http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html
* http://jlordiales.me/2015/01/23/docker-consul/
* http://mmckeen.net/blog/2013/12/27/advanced-docker-provisioning-with-packer/
* http://prakhar.me/docker-curriculum/
* http://stackoverflow.com/questions/18683810/docker-supervisord-and-logging-how-to-consolidate-logs-in-docker-logs
* http://stackoverflow.com/questions/20813486/exploring-docker-containers-file-system
* http://stackoverflow.com/questions/28583665/how-to-use-docker-logs
* http://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html
* http://www.barrymorrison.com/2015/Jan/02/pyall-or-a-docker-container-built-with-packer-and-ansible-with-all-python-versions/
* http://www.recorditblog.com/post/how-to-create-a-web-scale-infrastructure-based-on-docker-coreos-vulcand-and-mesos-and-why-object-storage-becomes-the-de-facto-data-repository/
* https://42notes.wordpress.com/2015/05/13/replace-boot2docker-with-coreos-and-vagrant-to-use-docker-containers/
* https://adetante.github.io/articles/service-discovery-with-docker-2/
* https://blog.docker.com/tag/logging/
* https://coreos.com/rkt/docs/latest/rkt-vs-other-projects.html
* https://coreos.com/using-coreos/clustering/
* https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html
* https://docs.docker.com/engine/admin/logging/overview/
* https://docs.docker.com/engine/userguide/eng-image/baseimages/
* https://docs.docker.com/mac/step_four/
* https://github.com/bradgignac/intro-to-coreos
* https://github.com/coreos/etcd
* https://github.com/coreos/fleet
* https://github.com/darcys22/haproxy
* https://github.com/democracyworks/consul-coreos
* https://github.com/docker/distribution
* https://github.com/giantswarm/kocho
* https://github.com/pires/nomad-vagrant-coreos-cluster
* https://github.com/tcnksm-sample/packer-docker
* https://github.com/wasbazi/coreos-packer
* https://medium.com/@mohitarora/manage-docker-containers-using-coreos-part-2-392544470a1d#.dj4pzkp7g
* https://mesos.apache.org/
* https://www.airpair.com/coreos/posts/coreos-with-docker
* https://www.digitalocean.com/community/tutorial_series/getting-started-with-coreos-2
* https://www.digitalocean.com/community/tutorials/how-to-use-fleet-and-fleetctl-to-manage-your-coreos-cluster
* https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-service-discovery-and-distributed-configuration-stores
* https://www.joyent.com/blog/container-native-discovery
* https://www.linkedin.com/pulse/nomad-multi-vm-cluster-vagrant-coreos-local-paulo-pires
* https://www.vagrantup.com/docs/docker/basics.html
* https://www.vagrantup.com/docs/synced-folders/rsync.html


Other
-----

* http://cloud-images.ubuntu.com/locator/ec2/

::

    aws --profile foo sts assume-role --role-arn \
    arn:aws:iam::564976771545:role/dev/AdminsRole-VJV3HEFA7XQ2 \
    --role-session-name bubba

    AWS_ACCESS_KEY_ID='ASIAASDFASDFASDFASDF' \
    AWS_SECRET_ACCESS_KEY='asdfasdfasdfasdfasdfasdf' \
    AWS_SECURITY_TOKEN='AQoDYXdzEEwagAL++...' \
    packer build -only=base -var version=0.0.1 -var source_ami=ami-415f6d2b \
    -var node_source_file=./authorized_keys \
    -var node_destination_name=authorized_keys base.json


Dumb OS X
=========

::
    export CFLAGS=-Qunused-arguments
    export CPPFLAGS=-Qunused-arguments
