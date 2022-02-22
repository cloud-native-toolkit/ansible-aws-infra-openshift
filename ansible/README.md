# Ansible automation readme

## Pre-requisites

1. Ansible runtime on local terminal 
1. Amazon AWS Ansible collection (should be installed with Ansible)
1. Amazon Community AWS Ansible collection (should be installed with Ansible)
1. AWS Admin Account with quota for ROSA clusters
1. Sufficient elastic IP addresses availabe for intended build (one per egress availability zones)

## Build

1. Ensure that a boto profile is created and AWS CLI is installed (if not follow guide [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))

        $ aws ec2 describe vpcs

Should return information on the current VPCs for your default region.

1. Ensure the aws configuration returns JSON format (this is required for some of the automation steps)

        $ cat ~/.aws/config

        [default]
        ...
        output = json

1. Edit the global variables [groups_vars/all](./group_vars/all)

        $ vi ./groups_vars/all

1. Adjust the inventory file for what is to be created [inventory.yaml](./inventory.yaml)

        $ vi ./inventory.yaml

1. From the ansible directory run

        $ ansible-playbook ./create.yaml



## Roles

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



## References

[Red Hat Ansible collection repository](https://console.redhat.com/ansible/automation-hub)
