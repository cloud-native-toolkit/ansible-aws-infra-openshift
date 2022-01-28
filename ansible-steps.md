# Ansible build tasks for environment

General
    - assumes the environment is in a single AWS region.
    - admin access available for the AWS account
    - assumes use of AWS STS for account access

---

1. Prerequisite actions (manual)
    1. Create STS login tokins and confirm CLI access
    1. Update the inventory.yaml file with the required customizations

---

1. Confirm variables file
    1. Validate variables file schema
    1. Import variables data into facts
    1. Confirm AWS Account credentials
    1. Confirm AWS Account quota
    1. Login to AWS ROSA
    1. Verify quota    
    1. Confirm region availability

---

1. Edge VPC
    1. Create Edge VPCs

        1. [Create Edge VPC with CIDRs](https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_vpc_net_module.html#ansible-collections-amazon-aws-ec2-vpc-net-module)
        1. [Find VPC id for new Edge VPC](https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_vpc_net_info_module.html#ansible-collections-amazon-aws-ec2-vpc-net-info-module)
        1. [Create Network ACL](AWS-CLI-cmds.md#create-network-acl)
        1. [Add rule to network ACL](AWS-CLI-cmds.md#add-rule-to-network-acl)

    1. Create Edge VPC Subnets
        1. [Create subnets](AWS-CLI-cmds.md#create-subnet)
        1. Get existing network ACL association
        1. [Assign Network ACL to subnet](AWS-CLI-cmds.md#change-subnet-acl-association)

    1. Create security groups

    1. Create Internet Gateway

        1. Create fixed IP addresses for incoming connections
        1. [Create Internet Gateway](AWS-CLI-cmds.md#create-internet-gateway)
        1. [Associate gateway with VPC](AWS-CLI-cmds.md#associate-gateway)
        1. Create elastic IP allocations for NAT gateways
        1. Create NAT gateway for egress only subnet

    1. Create VPN endpoints

---

1. Management VPC

    1. If not already created, create account roles
    1. Create ROSA cluster for management VPC

        1. Issue create cluster command (CLI)
        1. Monitor for completion

    1. Register cluster details
    1. Create operator roles
    1. Create OIDC provider
    1. Link to identity provider

---

1. Workload VPC

    1. Create ROSA cluster for workload VPC

        1. Issue create cluster command (CLI)
        1. Monitor for completion

    1. Register cluster details
    1. Create operator roles
    1. Create OIDC provider
    1. Link to identity provider

---

1. VPC Interconnectivity

    1. Create VPC Peer Connection between Workload VPC and Management VPC
    1. Accept VPC peering request for management VPC
    1. Create route table for VPC Peer Connection (Workload - Management)
    1. Create VPC Peer Connection between Edge VPC and Management VPC
    1. Accept VPC peering request for Management VPC
    1. Create route table for VPC Peer Connection (Edge - Management)
    1. Create VPC Peer Connection between Workload VPC and Edge VPC
    1. Accept VPC peering request for Edge VPC
    1. Create route table for VPC Peer Connection (Workload - Edge)

    References
    - [Create and accept VPC Peer Connection (Community Contribution)](https://docs.ansible.com/ansible/latest/collections/community/aws/ec2_vpc_peer_module.html)
    - [Create route table (Amazon Contribution)](https://docs.ansible.com/ansible/latest/collections/amazon/aws/ec2_vpc_route_table_module.html#ansible-collections-amazon-aws-ec2-vpc-route-table-module)

---

1. Corporate Data Center Connectivity

    1. Create transit gateway
    1. Configure transit gateway routes