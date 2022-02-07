# AWS Create Network ACL and associate with one or more subnets

This role creates a Network ACL and associates it with one or more supplied subnets.

It calls the <i>community.aws.ec2_vpc_nacl</i> module.

## Input Variables


| Variable     | Description |
|--------------|-------------------------------------------------|

| naclName      | Name of the Network ACL to be created |
| subnetIdList   | The list of subnet id to which the NACL will be associated (e.g. [subnet-123456789, subnet-987654321]) |
| usrProfile   | Based upon boto configuration, the AWS user profile to be utilized (default: 'default')|
| reqRegion    | The AWS region into which to create the VPC. Default is that associated with the provided AWS profile. |
| vpcId | Identifier for the VPC into which to create the Network ACL (e.g. vpc-123456789) |


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