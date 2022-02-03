# AWS Create VPC role

This role creates a VPC based upon the following variables. If no region is specified, the default region for the profile is utilized.

Two tags are added to the created VPC.
- environemnt. 
- name

## Input Variables


| Variable     | Description |
|--------------|-------------------------------------------------|
| envName      | Used to tag the VPC with environment (default: 'ibm')   |
| vpcName      | Identifier for VPC within environment, full name takes the form "(envName)-(vpcName)-vpc" (default: 'default') |
| cidr_block   | A list of CIDR's to associate with the VPC (default: '10.0.0.0/16') |
| usrProfile   | Based upon boto configuration, the AWS user profile to be utilized (default: 'default')|
| reqRegion    | The AWS region into which to create the VPC. Default is that associated with the provided AWS profile. |

## Returned Variables

| Variable   | Description |
|--------------|-------------------------------------------------|
| vpcData | VPC object with the returned creation information |

## Internal Variables

| Variables | Description |
|--------------|-------------------------------------------------|
| defaultRegion | Boolean flag to determine if region has been explicitly specified or not |
| returnedInfo_region | AWS module return info for creation using a specified region |
| returnedInfo_default | AWS module return info for creation using no specified region |