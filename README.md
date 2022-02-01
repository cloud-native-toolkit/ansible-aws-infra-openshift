# FSCloud-on-AWS
 This repository is to document the build of a Finacial Services Cloud equivalent on native AWS.

 The environment is built using AWS components Ansible automation.

 ## DRAFT
 It is currently a work in progress.

 Currently working on the network elements to determine how to emulate the FS Cloud security features in AWS, including Network ACLs, Security Groups, multiple VPCs, routing tables, internet gateways, VPN endpoints and so forth.

 The [ansible build steps](ansible-steps.md) readme contains the tasks followed by ansible to create the FS Cloud environment on AWS.

 The [build-steps](build-steps.md) readme contains the manual steps using the AWS CLI to create the cloud environment. Will be migrated to Ansible for automation.

 The [Access Guide](access-options.md) provides options tested for users to access provisioned servers in the AWS environment.

 The [Red Hat OpenShift on AWS (ROSA)](ROSA-cluster.md) documents the steps to build the OpenShift clusters. 

 The [AWS-CLI-cmds readme](AWS-CLI-cmds.md) document contains the key AWS CLI commands that would be utilized for a build. These could be included in an Ansible playbook. Per above, investigating if it is easier to use Ansible command line calls to aws cli or aws modules.

 [Architectural Decisions](ADs.md) document the design decisions made and the rationale for each decision.

 [RAID Log](RAID_Log.md) documents the risks, issues, assumptions and dependencies in the design.

 The architectural overview of the environment is as follows:

![Architecture Overview](./static/FS-Cloud-on-AWS.png)

Further details of the Management and Workload VPCs are per the following architecture overview and in the ROSA details [here](./ROSA-cluster.md#Multiple_AZ_cluster_configuration):

![ROSA Multi AZ Overview](./static/multi-az-rosa.png)

## References

Install AWS CLI [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

AWS CLI reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)

Ansible module reference (amazon.aws) [https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)
