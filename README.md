# IBM AWS Reference Architecture
 This repository is to document the build of a cloud reference architecture with OpenShift in AWS with Ansible.

 The environment is built using AWS components with Ansible automation (see the [Red Hat Ansible collection repository](https://console.redhat.com/ansible/automation-hub))

 ## Instructions

 1. clone this repository

      $ git clone https://github.com/cloud-native-toolkit/ibm-aws-reference-arch-ansible

1. If this is the first time running ansible to automate AWS on your local laptop/system, complete the following.

   1. Install the AWS CLI by following the guide [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
   1. Install Ansible by following the guide [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
   1. Configure AWS CLI to output JSON format (the output field in the file ~/.aws/config on Mac/Linux)

1. Change to ansible sub-directory under the cloned repository

      $ cd ./ansible/

1. Edit the variables file to customize the installation

      $ vi ./group_vars/all

1. Run the ansible playbook

      $ ansible-playbook ./site.yaml


 ## DRAFT
 It is currently a work in progress.

 Update Feb 8th : The automation currently accepts multiple variable inputs for top level VPC CIDRs, regions and availability zones (which can vary in quantity). From this, it;
 1. calculates the required subnets and associated network CIDRs
 1. creates the VPC if it does not already exist 
 1. once the VPC is in place, it uses the VPC id to create each of the required subnets skipping those that already exist
 1. creates the internet gateway for the VPC if it does not exist
 1. creates the NAT gateways, if they do not exist, for each egress subnet using the egess subnet ids
 1. creates the Network ACLs for each of the Edge security zones (ingress, bastion and egress)
 1. creates the route tables for each edge subnet (although this needs to be modified once all the network devices are created)

 Work in progress:
 - Edge VPC
    - validate that each NAT gateway is in "available" status before collecting private IP details
    - create the VPN endpoints to the edge VPC
    - create the load balancers for the edge VPC
    - update the route table creation role to point to the created load balancers
 - create the management VPC and ROSA cluster
 - create the workload VPC and ROSA cluster
 - create the peer to peer networking between the VPCs
 - add query to start of each role to make more standalone (will slow down but make more modular)
 - modify edge route creation to occur after the other VPC's have been created and the VPC connection peering has been built in order to set the route via the VPC peer connection

 The [Access Guide](access-options.md) provides options tested for users to access provisioned servers in the AWS environment.

 The [Red Hat OpenShift on AWS (ROSA)](ROSA-cluster.md) documents the steps to build the OpenShift clusters. 

 ## Reference Architecture

 [Architectural Decisions](ADs.md) document the design decisions made and the rationale for each decision.

 [RAID Log](RAID_Log.md) documents the risks, issues, assumptions and dependencies in the design.

 The architectural overview of the environment is as follows:

![Architecture Overview](./static/arch-overview.png)

 The [networking](networking.md) readme contains details of the network configuration for this setup.

Further details of the Management and Workload VPCs are per the following architecture overview and in the ROSA details [here](./ROSA-cluster.md#Multiple_AZ_cluster_configuration):

![ROSA Multi AZ Overview](./static/multi-az-rosa.png)

## External References

Ansible collection repository [https://console.redhat.com/ansible/automation-hub](https://console.redhat.com/ansible/automation-hub)

Install AWS CLI [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

AWS CLI reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)

Ansible module reference (amazon.aws) [https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)
