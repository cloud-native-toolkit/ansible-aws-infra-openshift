# IBM AWS Reference Architecture
 This repository is to document the build of a cloud reference architecture with OpenShift in AWS with Ansible.

 The environment is built using AWS components Ansible automation.

 ## DRAFT
 It is currently a work in progress.

 Currently working on the Ansible build automation for the edge VPC cluster. 


 Update Feb 8th : The automation currently accepts multiple variable inputs for top level VPC CIDRs, regions and availability zones (which can vary in quantity). From this, it;
 1. calculates the required subnets and associated network CIDRs
 1. creates the VPC if it does not already exist 
 1. once the VPC is in place, it uses the VPC id to create each of the required subnets skipping those that already exist
 1. creates the internet gateway for the VPC if it does not exist
 1. creates the NAT gateways, if they do not exist, for each egress subnet using the egess subnet ids
 1. creates the Network ACLs for each of the Edge security zones (ingress, bastion and egress)
 1. creates the route tables for each edge subnet (although this needs to be modified once all the network devices are created)

 Next steps:
 - Edge VPC
    - validate that each NAT gateway is in "available" status before collecting private IP details
    - create the VPN endpoints to the edge VPC
    - create the load balancers for the edge VPC
    - update the route table creation role to point to the created load balancers
 - create the management VPC
 - create the workload VPC
 - create the peer to peer networking between the VPCs
 - add query to start of each role to make more standalone (will slow down but make more modular)
 - modify edge route creation to occur after the other VPC's have been created and the VPC connection peering has been built in order to set the route via the VPC peer connection


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

 The [Access Guide](access-options.md) provides options tested for users to access provisioned servers in the AWS environment.

 The [Red Hat OpenShift on AWS (ROSA)](ROSA-cluster.md) documents the steps to build the OpenShift clusters. 

 [Architectural Decisions](ADs.md) document the design decisions made and the rationale for each decision.

 [RAID Log](RAID_Log.md) documents the risks, issues, assumptions and dependencies in the design.

 The architectural overview of the environment is as follows:

![Architecture Overview](./static/arch-overview.png)

Further details of the Management and Workload VPCs are per the following architecture overview and in the ROSA details [here](./ROSA-cluster.md#Multiple_AZ_cluster_configuration):

![ROSA Multi AZ Overview](./static/multi-az-rosa.png)

## References

Install AWS CLI [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/)

AWS CLI reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html)

Ansible module reference (amazon.aws) [https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html](https://docs.ansible.com/ansible/latest/collections/amazon/aws/index.html)
