# List of relevant AWS CLI Commands and syntaxs

## VPC Creation

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html)

    $ aws ec2 create-vpc \ 
    --cidr-block {{base_cidr}} \
    --instance-tenancy default \
    --tag-specifications ResourceType=vpc,Tags=[{Key=Name,Value="{{vpc_name}}"}]

Where:

{{base_cidr}}   - Base CIDR (e.g. 10.1.0.0/18) to be used. Add additional CIDR's in subsequent commands. 

{{vpc_name}}    - Name of VPC (e.g. fs-cloud-mgmt)

Output for variables:

VpcId : {{vpc_id}} - Provides the Id of the created VPC needed for future actions.

Use default tenancy (dedicated limits available EC2 instance images). 

## Associate additional CIDR's to VPC

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-vpc-cidr-block.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-vpc-cidr-block.html)

    $ aws ec2 associate-vpc-cidr-block \
    --vpc-id {{vpc_id}} \
    --cidr-block {{cidr_block}}

Where:

{{vpc_id}}      - The identifier of the previously created VPC (e.g. vpc-123456)

{{cidr_block}}  - The CIDR to associate with the VPC (e.g. 10.2.0.0/18)

No required output to populate variables.

## Create Network ACL

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html)

    $ aws ec2 create-network-acl \
    --vpc-id {{vpc_id}} \
    --tag-specifications ResourceType=networkacl,Tags=[{Key=Name,Value="{{acl_name}}"}]

Rules are applied to this ACL separately once it is created.

Where:

{{vpc_id}}      - The identifier of the previously created VPC (e.g. vpc-123456)

{{acl_name}}    - The name to tag the Network ACL (e.g. edge-bastion-acl)

Required Output for variables:

NetworkAclId : {{networkacl_id}} - Identifier for the created Network ACL

## Add rule to Network ACL

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html)

### Add ingress rule

    $ aws ec2 create-network-acl-entry \
    --cidr_block {{cidr_block}} \
    --ingress \
    --network-acl-id {{networkacl_id}} \
    --protocol {{rule_protocol}} \
    --rule-action {{rule_action}} \
    --rule-number {{rule_number}}

Where:

{{cidr_block}}  - The CIDR that applies to the rule (inbound or outbound) (e.g. 0.0.0.0/0)

{{networkacl_id}}   - The identifier for the NetworkACL that the rule will apply (e.g. acl-abcd123)

{{rule_protocol}}   - The protocol number for the rule. 6(TCP), 17(UDP), 1(UCMP). Any other number allows all protocols.

{{rule_action}}     - Action the rule should take. allow or deny.

{{rule_number}}     - The number for the rule (integer). Rules are processed in ascending order (1 through 65535).

No relevant output for variables.

### Add egress rule

    $ aws ec2 create-network-acl-entry \
    --cidr_block {{cidr_block}} \
    --egress \
    --network-acl-id {{networkacl_id}} \
    --protocol {{rule_protocol}} \
    --rule-action {{rule_action}} \
    --rule-number {{rule_number}}

Where:

{{cidr_block}}  - The CIDR that applies to the rule (inbound or outbound) (e.g. 0.0.0.0/0)

{{networkacl_id}}   - The identifier for the NetworkACL that the rule will apply (e.g. acl-abcd123)

{{rule_protocol}}   - The protocol number for the rule. 6(TCP), 17(UDP), 1(UCMP). Any other number allows all protocols.

{{rule_action}}     - Action the rule should take. allow or deny.

{{rule_number}}     - The number for the rule (integer). Rules are processed in ascending order (1 through 65535).

No relevant output for variables.

## Create Subnet

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html)

    $ aws ec2 create-subnet \
    --vpc-id {{vpc_id}} \
    --cidr-block {{cidr_block}} \
    --availability-zone {{availability_zone}}
    --tag-specifications ResourceType=subnet,Tags=[{Key=Name,Value="{{subnet_name}}"}]

Where:

{{vpc_id}}      - The identifier of the previously created VPC (e.g. vpc-123456)

{{cidr_block}}  - The CIDR to associate with the subnet (e.g. 10.2.1.0/24)

{{subnet_name}} - The name of the subnet (e.g. mgmt-workers01)

{{availability_zone}}   - The name of the availability zone to place the subnet (e.g. us-east-1a)

Required output:

SubnetId : {{subnet_id}} - The identifier of the subnet just created

## Change subnet ACL association

This replaces the default ACL with one of the ones created.

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-association.html)

    $ aws ec2 replace-network-acl-association \
    --association-id {{association_id}} \
    --network-acl-id {{networkacl_id}}

Where:

{{association_id}}  - The identifier of the Network ACL and subnet association to be replaced (see xxx)
{{networkacl_id}}   - The identifier of the Network ACL to replace the existing one.

## Create internet gateway

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html)

Creates the gateway. Attach to VPC afterwards. Needed before creating VPN endpoints.

    $ aws ec2 create-internet-gateway \
    --tag-specifications ResourceType=internet-gateway,Tags[{Key=Name},{Value="{{gw_name}}"}]

Where:

{{gw_name}} - The name of the gateway (e.g. egde-gateway)

Required Output:

InternetGatewayId : {{gw_id}} - The internet gateway identifier

## Associate Gateway

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html)

    $ aws ec2 attach-internet-gateway \
    --internet-gateway-id {{gw_id}}
    --vpc-id {{vpc_id}} 

Where:

{{gw_id}}       - The identifier of the previously created internet gateway

{{vpc_id}}      - The identifier of the previously created VPC (e.g. vpc-123456)

No required output.

## Create VPC Peering Connection

Reference [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-peering-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-peering-connection.html)

    $ aws ec2 create-vpc-peering-connection \
    --vpc-id {{vpc_id}} \
    --peer-vpc-id {{peer_vpc_id}}

Where:

{{vpc_id}}      - The identifier of the first VPC
{{peer_vpc_id}} - The identifier the second VPC (this is the one which requires approval from the owner)

Required output:

VpcPeeringConnectionId : {{vpc_peer_id}} - The identifier of the VPC peer just created.