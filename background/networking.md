# Network security and routing

The cloud environment consists of 3 virtual private clouds (VPCs).
    - Edge
    - Management
    - Workload

# Edge Cluster

The Edge cluster is used for customer internal traffic ingress and egress with VPN connectivity to remote sites. It consists of 3 security tiers within the VPC.

- Ingress
- Bastion
- Egress

For example, using a CIDR of 10.0.0.0/14 for the VPC and splitting this into three gives:

- Ingress 10.0.0.0/16
- Bastion 10.1.0.0/16
- Egress 10.2.0.0/16

AWS automatically creates a default route table for all the CIDR's provided when the VPC is created. 

## Ingress

The ingress tier consists of a class C subnet in each availability zone. These subnets connect to: 

- VPN Endpoint (inbound)
- Internet Gateway (outbound)
- Load balancer to bastion (outbound)

### VPN Endpoint

### Route table

The following routing table is required.
| Network | Gateway | Description |
| ------------- | ------------------ | ------------------------------------------------------------------ |
| Ingress_CIDR | local | Local network traffic between hosts |
| 0.0.0.0/0 | VPC_Internet_Id | Outbound traffic for VPN return (needed to establish VPN connection) |
| Bastion_CIDR | Bastion_ELB_Id | Outbound traffic to bastion load balancer |

Where

- Ingress_CIDR is the CIDR for the ingress subnet tier (e.g. 10.0.0.0/16 in the above example)
- VPC_Internet_Id is the AWS VPC internet gateway identifier (e.g. vpc-123456789)
- Bastion_CIDR is the CIDR for the bastion tier (e.g. 10.1.0.0/16 in the above example)
- Bastion_ELB_Id is the AWS elastic laod balancer identifier (e.g. elb-1243456789)

### Network ACL

The network ACL controls access to the subnet as a whole. The following Network ACL is required.

<b>Inbound Rules</b>
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | TCP | Allow | 0.0.0.0/0 | null | null | 443 | 443 | OpenVPN connection |
| 200 | UDP | Allow | 0.0.0.0/0 | null | null | 1194 | 1194 | OpenVPN connection |


<b>Outbound Rules</b>
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | All | Allow | 0.0.0.0/0 | null | null | 0 | 65535 | All outbound connections |


## Bastion

### Route table

<i>This needs to be modified to suit the outgoing traffic requirement</i>

The following routing table is required.
| Network | Gateway | Description |
| ------------- | ------------------ | ------------------------------------------------------------------ |
| Ingress_CIDR | local | Local network traffic between hosts |
| Bastion_CIDR | local | Local traffic |

Where

- Ingress_CIDR is the CIDR for the ingress subnet tier (e.g. 10.0.0.0/16 in the above example)
- Bastion_CIDR is the CIDR for the bastion tier (e.g. 10.1.0.0/16 in the above example)

### Network ACL

The network ACL controls access to the subnet as a whole. The following Network ACL is required.

<b>Inbound Rules</b>
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | TCP | Allow | Bastion_CIDR | null | null | 0 | 65535 | Local connections |
| 200 | TCP | Allow | Ingress_CIDR | null | null | 0 | 65535 | Only connections from the ingress subnets |

<i>May need to tighten the list of available ports in future once requirements are finalised</i>


<b>Outbound Rules</b>
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | All | Allow | 0.0.0.0/0 | null | null | 0 | 65535 | All outbound connections |

<i>The open outbound connections may need to be tightened in future.</i>

## Egress

The egress tier consists of a class C subnet in each availability zone. These subnets connect to:
    - NAT Gateway (outbound)

### Route table

Each egress subnet requires a separate route table to direct traffic via it's own NAT gateway. 

The following routing table is required.
| Network | Gateway | Description |
| ------------- | ------------------ | ------------------------------------------------------------------ |
| 0.0.0.0/0 | NAT_GW | Internet traffic |
| Management_CIDR | Mgmt_VPC_Peer_GW | Return connection to Management VPC |
| Workload_CIDR | Workload_VPC_Peer_GW | Return connection to Management VPC |

where

- NAT_GW is the NAT Gateway associated with the subnet
- Management_CIDR is the CIDR for the management VPC
- Workload CIDR is the CIDR for the workload VPC
- Mgmt_VPC_Peer_GW is the VPC Peer gateway with the management VPC
- Workload_VPC_Peer_GW is the VPC Peer gateway with the workload VPC


### Network ACL

The network ACL controls access to the subnet as a whole. The following Network ACL is required.

Inbound Rules
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | TCP | Allow | Management_cidr | null | null | 0 | 65535 | All connections from management VPC |
| 200 | TCP | Allow | Workload_cidr | null | null | 0 | 65535 | All connections from workload VPC |

<b>May need to tighten the list of available ports in future once requirements are finalised<b>


Outbound Rules
|Rule No. | Protocol | Allow/Deny | CIDR | ICMP Type | ICMP Code | From Port | To Port | Description | 
| --------- | --------- | ----------- | --------- | ---------- | --------- | ---------- | --------- | --------------------------- |
| 100 | All | Allow | 0.0.0.0/0 | null | null | 0 | 65535 | All outbound connections |


# Management Cluster

# Workload Cluster



