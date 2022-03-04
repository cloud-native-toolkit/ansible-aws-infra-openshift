# Background material relevant to the architectures.

## Reference Architecture

 [Architectural Decisions](ADs.md) document the design decisions made and the rationale for each decision.

 [RAID Log](RAID_Log.md) documents the risks, issues, assumptions and dependencies in the design.

 The architectural overview of the environment is as follows:

![Architecture Overview](./static/arch-overview.png)

 The [networking](networking.md) readme contains details of the network configuration for this setup.

Further details of the Management and Workload VPCs are per the following architecture overview and in the ROSA details [here](./ROSA-cluster.md#Multiple_AZ_cluster_configuration):

![ROSA Multi AZ Overview](./static/multi-az-rosa.png)

 ## Background Details

 The [Access Guide](access-options.md) provides options tested for users to access provisioned servers in the AWS environment.

 The [Red Hat OpenShift on AWS (ROSA)](ROSA-cluster.md) documents the steps to build the OpenShift clusters and shows the generated architecture. 

## External References

Ansible collection repository [https://console.redhat.com/ansible/automation-hub](https://console.redhat.com/ansible/automation-hub)

Install AWS CLI [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

AWS CLI reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)

Ansible module reference (amazon.aws) [https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)
