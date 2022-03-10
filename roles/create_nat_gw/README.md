# AWS Create NAT Gateway

This role creates a NAT Gateway with an elastic IP and attached to a provided. If no region is specified, the default region for the profile is utilized.

it calls the amazon.aws.ec2_vpc_nat_gateway module.

## Input Variables


| Variable     | Description |
|--------------|-------------------------------------------------|

| ngwName      | Name of the gateway to be created |
| subnetId   | The id of the subnet that the NAT gateway will be attached to (e.g. subnet-123456789) |
| usrProfile   | Based upon boto configuration, the AWS user profile to be utilized (default: 'default')|
| reqRegion    | The AWS region into which to create the VPC. Default is that associated with the provided AWS profile. |
| wait_for_complete | Determines whether to wait for a successfully creation (which can take a few minutes), or return after AWS request sent |

## Returned Variables

| Variable   | Description |
|--------------|-------------------------------------------------|
| ngwReturnedInfo | Register return from the AWS module call |

## Internal Variables

| Variables | Description |
|--------------|-------------------------------------------------|
| defaultRegion | Boolean flag to determine if region has been explicitly specified or not |
| returnedInfo_region | AWS module return info for creation using a specified region |
| returnedInfo_default | AWS module return info for creation using no specified region |