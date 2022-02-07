# FSCloud-on-AWS
 This repository is to document the build of a Finacial Services Cloud equivalent on native AWS.

 The environment is built using AWS components Ansible automation.

 ## DRAFT
 It is currently a work in progress.

 Currently working on the Ansible build automation for the edge VPC cluster. 


 Update Feb 7th : The automation currently accepts multiple variable inputs for top level VPC CIDRs, regions and availability zones (which can vary in quantity). From this, it;
 1. calculates the required subnets and associated network CIDRs
 1. creates the VPC if it does not already exist 
 1. once the VPC is in place, it uses the VPC id to create each of the required subnets skipping those that already exist
 1. creates the internet gateway for the VPC if it does not exist
 1. creates the NAT gateways, if they do not exist, for each egress subnet using the egess subnet ids
 1. creates the Network ACLs for each of the Edge security zones (ingress, bastion and egress)

 Next steps:
 - Edge VPC
    - validate that each NAT gateway is in "available" status before collecting private IP details
    - modify the route tables for each subnet
    - create the VPN endpoints to the edge VPC
 - create the management VPC
 - create the workload VPC
 - create the peer to peer networking between the VPCs


 ## Ansible structure
 - site.yaml : main playbook
 - calc_subnets : role to calculate the required ACL and subnet CIDRs from a provided Edge VPC CIDR with variable number of availability zones and network prefixes.
 - create_vpc : Reusable role to create a VPC with various options
 - create_subnet : Reusable role to create a subnet in an availability zone with various options
 - create_igw: Reusable role to create the internet gateway with various options
 - create_nat_gw: Reusable role to create a NAT Gateway and attach to a subnet
 - edge_cidrs: Calculates the network CIDRs for the Edge VPC based upon the provided high level Edge CIDR and the required number of availability zones
 - edge_vpc: Creates the Edge VPC if it does not already exist and registers the VPC id
 - edge_subnets: Creates the Edge subnets if they do not already exist and registers the subnet id's for each
 - edge_igw: Create the Internet Gateway for the Edge VPC if it does not already exist
 - edge_nat: Creates the required NAT Gateways for the Egress subnets if they do not already exist and registers the private IP's of each
 - edge_nacl: Creates the required Network ACL's for each of the Edge network tiers (ingress, bastion and egress) and assigns then to the required subnets in each of those tiers

 The [networking](networking.md) readme contains details of the network configuration for this setup.

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
