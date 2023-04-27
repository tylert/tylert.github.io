Other
-----

* https://awsregion.info/
* https://instances.vantage.sh/ former ec2instances.info
* http://cloud-images.ubuntu.com/locator/ec2/
* https://wiki.debian.org/Cloud/AmazonEC2Image/
* https://www.uplinklabs.net/projects/arch-linux-on-ec2/
* https://gitlab.com/anemos-io/archlinux-ec2
* http://mathcom.com/arch.aws.ami.html
* https://wiki.archlinux.org/title/Arch_Linux_AMIs_for_Amazon_Web_Services
* https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

::

    aws sts assume-role \
        --role-arn arn:aws:iam::123456789012:role/dev/AdminRole \
        --role-session-name bubba

    AWS_ACCESS_KEY_ID='ASIAASDFASDFASDFASDF...' \
    AWS_SECRET_ACCESS_KEY='asdfasdfasdfasdfasdfasdf...' \
    AWS_SECURITY_TOKEN='AQoDYXdzEEwagAL++...' \
    packer build ...

    # AWS_DEFAULT_PROFILE???


CLI
---

::

    # Get the list of available instance types
    aws ec2 describe-instance-type-offerings |\
        jq .[][].InstanceType | tr -d '"' | sort | uniq

    # Get the list of available engines
    aws rds describe-db-engine-versions | \
        jq .[][].Engine | tr -d '"' | sort | uniq

    # Get the list of engine versions available for a given engine
    aws rds describe-db-engine-versions --engine ${ENGINE} |\
        jq .[][].EngineVersion | tr -d '"' | sort | uniq

    # Get the list of allowed instance types for a given engine
    aws rds describe-orderable-db-instance-options --engine ${ENGINE} |\
        jq .[][].DBInstanceClass | tr -d '"' | sort | uniq

::

    # Get info about an AMI (Reminder:  AMIs live in a single region)
    aws ec2 describe-images \
        --region=ca-central-1 \
        --image-ids ami-abcd1234567890

    # Get just the OwnerId of an AMI
    aws ec2 describe-images \
        --image-ids ami-abcd1234567890 |\
        jq -r .Images[0].OwnerId

    # Amzon Linux AMIs (show only the last one)
    aws ec2 describe-images \
        --owners=amazon \
        --filters='Name=name,Values=amzn2-ami-hvm*' \
        --query='sort_by(Images, &CreationDate)[].[Name, ImageId, OwnerId][-1]'

    # Winderz AMIs (show all of them with newest last)
    aws ec2 describe-images \
        --owners=amazon \
        --filters='Name=name,Values=Windows_Server-*-English-Full-Base*' \
        --query='sort_by(Images, &CreationDate)[].[Name, ImageId, OwnerId]'

    # Ubuntu AMIs for ARM
    aws ec2 describe-images \
        --owners=099720109477 |\
        jq '.Images[] | select(.ImageType | contains("machine"))' |\
        jq '. | select(.VirtualizationType | contains("hvm"))' |\
        jq '. | select(.Architecture | contains("arm"))'

    # owner "amazon" for AmazonLinux/Windows AMIs from "Amazon"
    # owner "099720109477" for Ubuntu AMIs from "Canonical"
    # owner "136693071363" for Debian AMIs from "Debian"
    # owner "093273469852" for ArchLinux AMIs from "Uplink Labs"

::

    jq '.Accounts[] | {"alias": .Alias, "acctid": .Account}' accounts.json | jq -s . > accounts_better.json


TGW/TF
------

* https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html#cfn-route53-recordset-name
* https://dev.to/rolfstreefkerk/how-to-setup-a-serverless-application-with-aws-sam-and-terraform-33m9
* https://docs.aws.amazon.com/vpc/latest/tgw/tgw-best-design-practices.html
* https://aws.amazon.com/blogs/networking-and-content-delivery/zendesks-global-mesh-network-how-we-lowered-operational-overhead-and-cost-by-migrating-to-aws-transit-gateway/
* https://mechanicalrock.github.io/2020/02/24/transit-gateway.html
* https://www.aws.training/Details/eLearning?id=40275


EC2
---

* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html
* https://labs.sogeti.com/building-aws-golden-image-with-ec2-image-builder/
* https://aws.amazon.com/blogs/aws/troubleshoot-boot-and-networking-issues-with-new-ec2-serial-console/


VPC
---

* https://aws.amazon.com/blogs/networking-and-content-delivery/vpc-sharing-key-considerations-and-best-practices/
* https://aws.amazon.com/blogs/aws/new-vpc-ingress-routing-simplifying-integration-of-third-party-appliances/
* https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-network-traffic-inspection-using-aws-gateway-load-balancer/


Exam Prep
---------

* https://www.examtopics.com/exams/amazon/aws-certified-cloud-practitioner/
* https://www.aws.training/Details/eLearning?id=60697
* https://aws.amazon.com/s3/storage-classes/
* https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/
* https://jayendrapatil.com/tag/aws/
* https://aws.amazon.com/premiumsupport/plans/
* https://d1.awsstatic.com/whitepapers/aws_pricing_overview.pdf
* https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf
* https://aws.amazon.com/snow/
* https://aws.amazon.com/premiumsupport/knowledge-center/estimating-aws-resource-costs/
* https://aws.amazon.com/compliance/shared-responsibility-model/
* https://aws.amazon.com/blogs/apn/the-5-pillars-of-the-aws-well-architected-framework/
* https://digitalcloud.training/aws-cheat-sheets/
* https://dev.to/aws-builders/which-aws-certification-exam-should-i-sit-hah

Most useful:  "Cloud Practitioner", "System Operator", "Solutions Architect".


IAM
---

* https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/
* http://blogs.aws.amazon.com/security/post/Tx2MUS2R3CMGG8H/Enable-a-New-Feature-in-the-AWS-Management-Console-Cross-Account-Access


AWS STS
-------

* http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html


Continuous Delivery on EC2
--------------------------

* https://youtu.be/I6ApIARoMxE
* http://www.slideshare.net/AmazonWebServices/aws-december-2015-webinar-series-continuous-delivery-to-amazon-ec2-container-service


ECS
---

* https://www.youtube.com/watch?v=MRoPaHUttoA
* http://www.slideshare.net/AmazonWebServices/aws-april-webinar-series-getting-started-with-amazon-ec2-container-service
* https://aws.amazon.com/blogs/compute/managing-secrets-for-amazon-ecs-applications-using-parameter-store-and-iam-roles-for-tasks/


ECR
---

* https://aws.amazon.com/blogs/compute/authenticating-amazon-ecr-repositories-for-docker-cli-with-credential-helper/


Account Setup
-------------

::

    Payment Currency Preference -> Selected Currency:  CAD - Canadian Dollar

    IAM User and Role Access to Billing Information
    IAM user/role access to billing information is activated.

    Enable MFA for root account and users and so on.


Assorted
--------

* https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started/
* https://launchbylunch.com/posts/2014/Jan/29/aws-tips/
* http://cloudacademy.com/blog/centralized-log-management-with-aws-cloudwatch-part-3-of-3/
* http://cloudacademy.com/blog/aws-cloudwatch-monitoring/
* https://aws.amazon.com/freertos/
* https://en.wikipedia.org/wiki/FreeRTOS
* https://github.com/codahale/sneaker
* https://www.threatstack.com/blog/cloud-security-best-practices-finding-securing-managing-secrets-part-2


Cloud Backup and Recovery
-------------------------

* http://www.slideshare.net/AmazonWebServices/aws-march-2016-webinar-series-best-practices-for-architecting-cloud-backup-and-recovery-solutions
* http://docs.aws.amazon.com/cli/latest/reference/s3/sync.html


DynamoDB
--------

* http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html


OpenSearch
----------

* https://youtu.be/cn7QLSPB3OA
* http://www.slideshare.net/AmazonWebServices/aws-october-webinar-series-introducing-amazon-elasticsearch-service
* https://aws.amazon.com/blogs/aws/new-amazon-elasticsearch-service/


Cloud Hybrid
------------

* https://youtu.be/tIDbFTIPolQ
* http://www.slideshare.net/AmazonWebServices/february-2016-webinar-series-use-aws-cloud-storage-as-the-foundation-for-hybrid-strategy


IPAM
----

Nowadays, you'd just use AWS IPAM instead of rolling your own.

* https://github.com/netbox-community/netbox
* https://netbox.readthedocs.io/en/stable/
* https://registry.terraform.io/search/providers?q=netbox
* https://www.phillhocking.com/terraform-netbox-ipam-aws/


Lambda
------

* https://djharper.dev/post/2018/01/27/running-go-aws-lambda-functions-locally/
* https://github.com/djhworld/go-lambda-invoke
* https://medium.com/nagoya-foundation/running-and-debugging-go-lambda-functions-locally-156893e4ed0d
* https://github.com/blmayer/awslambdarpc
* https://stackoverflow.com/questions/70925966/can-we-run-an-aws-lambda-locally-without-deployment
* https://dev.bitolog.com/run-aws-lambda-locally/
* https://github.com/raisebook/run-go-lambda
* https://docs.aws.amazon.com/lambda/latest/dg/golang-package.html
* https://djharper.dev/post/2018/01/27/running-go-aws-lambda-functions-locally/
* https://medium.com/nagoya-foundation/running-and-debugging-go-lambda-functions-locally-156893e4ed0d
* https://github.com/blmayer/awslambdarpc
* https://harishkm.in/2020/06/16/run-bash-scripts-in-aws-lambda-functions/
* https://github.com/aws/aws-lambda-runtime-interface-emulator
