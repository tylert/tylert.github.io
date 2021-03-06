CLI
---

::

    # Get the list of available instance types
    aws ec2 describe-instance-type-offerings |\
        jq .[][].InstanceType | tr -d '"' | sort | uniq

    # Get the list of available engines
    aws rds describe-db-engine-versions | \
        jq .[][].Engine | sort | uniq

    # Get the list of engine versions available for a given engine
    aws rds describe-db-engine-versions --engine ENGINE |\
        jq .[][].EngineVersion | sort | uniq

    # Get the list of allowed instance types for a given engine
    aws rds describe-orderable-db-instance-options --engine ENGINE |\
        jq .[][].DBInstanceClass | tr -d '"' | sort | uniq


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

Most useful:  "Cloud Practitioner", "System Operator", "Solutions Architect".


IAM
---

* https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-cli/


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


Account Setup
-------------

::

    Payment Currency Preference -> Selected Currency:  CAD - Canadian Dollar

    IAM User and Role Access to Billing Information
    IAM user/role access to billing information is activated.

    Enable MFA for root account and users and so on.
