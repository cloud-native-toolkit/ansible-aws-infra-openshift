# Build steps for environment

General
    - assumes the environment is in a single AWS region.
    - admin access available for the AWS account
    - AWS CLI setup

1. Create AWS account

1. Create VPCs

    For each the the required VPC's (edge, management and workload)
    1. [Create Edge VPC](AWS-CLI-cmds.md#vpc-creation)
    1. [Add CIDRs](AWS-CLI-cmds.md#Associate-additional-CIDRs-to-VPC)

1. Create Network ACLs

    For each network ACL, create the ACL and then assign the required rules.
    1. [Create Network ACL](AWS-CLI-cmds.md#create-network-acl)
    1. [Add rule to network ACL](AWS-CLI-cmds.md#add-rule-to-network-acl)

1. Create Subnets
    1. [Create subnet](AWS-CLI-cmds.md#create-subnet)
    1. Get existing network ACL association
    1. [Assign Network ACL to subnet](AWS-CLI-cmds.md#change-subnet-acl-association)

1. Create security groups

1. Create Internet Gateways

    For each required gateway
    1. [Create Internet Gateway](AWS-CLI-cmds.md#create-internet-gateway)
    1. [Associate gateway with VPC](AWS-CLI-cmds.md#associate-gateway)

1. Create VPC Peers

    For the link between each VPC, create a peer-to-peer connection. The secondary VPC needs to accept that connection. Once in place, update route tables to connect subnets between the VPC.
    1. Create VPC Peering Connection
    1. Accept VPC Peering Request
    1. Update route tables

1. Create VPN endpoints

1. Create VPC Endpoints
    VPC Endpoints allow connection from AWS services to each VPC.

1. Create Route 53 domain name servers for private DNS

1. Create Red Hat OpenShift on AWS Clusters
    [ROSA Instructions](ROSA-cluster.md)
