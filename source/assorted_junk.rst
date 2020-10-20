* http://www.codeandcompost.com/post/a-safe-place-to-log,-part-01
* https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/
* https://launchbylunch.com/posts/2014/Jan/29/aws-tips/
* http://cloudacademy.com/blog/centralized-log-management-with-aws-cloudwatch-part-3-of-3/
* http://cloudacademy.com/blog/aws-cloudwatch-monitoring/
* https://github.com/vulcand/vulcand


Consul Stuff
------------

::

    consul agent -dev -bind=10.80.0.22


Random Other Docs
-----------------

* http://blog.scottlowe.org/2015/02/06/quick-intro-to-consul/
* http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html
* http://jlordiales.me/2015/01/23/docker-consul/
* http://mmckeen.net/blog/2013/12/27/advanced-docker-provisioning-with-packer/
* http://prakhar.me/docker-curriculum/
* http://stackoverflow.com/questions/18683810/docker-supervisord-and-logging-how-to-consolidate-logs-in-docker-logs
* http://stackoverflow.com/questions/20813486/exploring-docker-containers-file-system
* http://stackoverflow.com/questions/28583665/how-to-use-docker-logs
* http://sysadvent.blogspot.ca/2015/12/day-12-introduction-to-nomad.html
* http://www.barrymorrison.com/2015/Jan/02/pyall-or-a-docker-container-built-with-packer-and-ansible-with-all-python-versions/
* https://adetante.github.io/articles/service-discovery-with-docker-2/
* https://blog.docker.com/tag/logging/
* https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html
* https://docs.docker.com/engine/admin/logging/overview/
* https://docs.docker.com/engine/userguide/eng-image/baseimages/
* https://docs.docker.com/mac/step_four/
* https://github.com/darcys22/haproxy
* https://github.com/docker/distribution
* https://github.com/giantswarm/kocho
* https://github.com/tcnksm-sample/packer-docker
* https://mesos.apache.org/
* https://www.digitalocean.com/community/tutorials/the-docker-ecosystem-service-discovery-and-distributed-configuration-stores
* https://www.joyent.com/blog/container-native-discovery
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


Self-Hosting Stuff
------------------

* https://bridge.grumpy-troll.org/2020/07/small-mailserver-bcp/


DVD Ripping
-----------

* https://www.tweaking4all.com/video/rip-dvd-blu-ray/linux-handbrake-copy-a-dvd-to-mp4-or-mkv-file/
