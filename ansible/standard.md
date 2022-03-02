# Standard OpenShift on AWS

Provisions OpenShift onto a VPC per the reference architecture defined [here](https://github.com/cloud-native-toolkit/automation-solutions/blob/aws-ref-arch-entry/architectures/awscloud.md) using Ansible automation.

## Software Dependencies

The module depends upon the following software components being installed on the build machine.

### Command-line Tools

- Ansible version 2.12.1 or higher (follow the guide [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))
- AWS CLI version 2.4.11 or higher (follow the guide [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))
- ROSA CLI version 1.1.7 or higher (follow the guide [here](https://docs.openshift.com/rosa/rosa_getting_started/rosa-installing-rosa.html))

## Module Dependences

This module makes use of the following Ansible modules.

- amazon.aws
- amazon.community.aws

## Example usage

1. Clone this repository

    $ git clone https://github.com/cloud-native-toolkit/ibm-aws-reference-arch-ansible

1. Edit the standard.yaml file for required configuration if different than the default.


    vars:
        awsProfile: default         # The boto profile to be utilized
        awsRegion: ap-southeast-2   # Region into which to create the VPC and cluster
        availZones:                 # Add availability zones as required (must all be part of the above region)
        - 'ap-southeast-2a'
        - 'ap-southeast-2b'
        - 'ap-southeast-2c'
        resourceGroup: 'recloud'    # This is used to identify deployed resources
        vpcCIDR: 10.0.0.0/16        # The VPC subnet to be used (Subnets will be calculated from this)
        subnetPrefix: 24            # The prefix to be used for the required subnets
        openshift_version: 4.9.21   # The openshift version to deploy

1. Run the ansible playbook

    $ ansible-playbook ./standard.yaml

When complete, the automation will output the discovered and/or created resources into the inventory.yaml file in the root directory.

    # Cloud Inventory

    arch_type: 'Standard'
    inventory:
    Last_Update: Wed  2 Mar 2022 13:36:37 AEDT
    cidrs:
        ec2:
            cidr: 10.0.128.0/18
            subnets:
            - 10.0.128.0/24
            - 10.0.129.0/24
            - 10.0.130.0/24
        private:
            cidr: 10.0.64.0/18
            subnets:
            - 10.0.64.0/24
            - 10.0.65.0/24
            - 10.0.66.0/24
        public:
            cidr: 10.0.0.0/18
            subnets:
            - 10.0.0.0/24
            - 10.0.1.0/24
            - 10.0.2.0/24
        vpc: 10.0.0.0/16
    ec2_rtbs:
    -   id: rtb-06b46a5aa225921b0
        name: recloud-ec2-rtb-2
        subnet_id: subnet-00c68d43695112810
    -   id: rtb-03b4a967d238bf531
        name: recloud-ec2-rtb-1
        subnet_id: subnet-0d3b9d3a9799787db
    -   id: rtb-0e92922d3f69d23a0
        name: recloud-ec2-rtb-0
        subnet_id: subnet-0dda8ac8b5a824336
    ec2_subnets:
    -   availability_zone: ap-southeast-2a
        cidr: 10.0.128.0/24
        id: subnet-0dda8ac8b5a824336
        name: recloud-ec2-0
    -   availability_zone: ap-southeast-2b
        cidr: 10.0.129.0/24
        id: subnet-0d3b9d3a9799787db
        name: recloud-ec2-1
    -   availability_zone: ap-southeast-2c
        cidr: 10.0.130.0/24
        id: subnet-00c68d43695112810
        name: recloud-ec2-2
    igw:
        id: igw-0e6f023a421dd994d
        name: recloud-igw
    nacl:
    -   id: acl-0acadc8749fff0ed9
        name: recloud-ec2-nacl
        subnets:
        - subnet-0dda8ac8b5a824336
        - subnet-00c68d43695112810
        - subnet-0d3b9d3a9799787db
    -   id: acl-002ad12fc85393776
        name: recloud-private-nacl
        subnets:
        - subnet-0ecaede6b638b07fc
        - subnet-0b201e0178e4e3d78
        - subnet-0f0aa5a62c9de53a8
    ngw:
    -   addresses:
        -   allocation_id: eipalloc-0a090fa1a102a6bb3
            network_interface_id: eni-01331ba66d795c3be
            private_ip: 10.0.0.201
            public_ip: 13.239.168.125
        id: nat-00e45e3b74a1505d7
        name: recloud-ngw-0
        state: available
        subnet_id: subnet-0ed5773c5450b5d61
    -   addresses:
        -   allocation_id: eipalloc-054c1eb94c0266c5d
            network_interface_id: eni-0764abbdeee3fec9b
            private_ip: 10.0.2.96
            public_ip: 54.79.61.158
        id: nat-0e716994c7feb5174
        name: recloud-ngw-2
        state: available
        subnet_id: subnet-0ae6f639a9fbdc434
    -   addresses:
        -   allocation_id: eipalloc-0a97dde99042d0d5b
            network_interface_id: eni-06f84ad93d27e2013
            private_ip: 10.0.1.16
            public_ip: 54.79.230.154
        id: nat-0fe3be13cf0b7fe03
        name: recloud-ngw-1
        state: available
        subnet_id: subnet-020c6b76cfc125b0c
    profile: default
    region: ap-southeast-2
    rosa:
        console: https://console-openshift-console.apps.recloud-rosa.otqj.p1.openshiftapps.com
        dns: recloud-rosa.otqj.p1.openshiftapps.com
        id: 1qm3urqdhs21f9jql1v7et59d11mla3r
        name: recloud-rosa
        state: ready_
    rtbs:
    -   id: rtb-0245d080655aa7595
        name: recloud-private-rtb-1
        subnet_id: subnet-0b201e0178e4e3d78
    -   id: rtb-0d6a7a72484019e6e
        name: recloud-private-rtb-0
        subnet_id: subnet-0f0aa5a62c9de53a8
    -   id: rtb-096adc7aded3e52a1
        name: recloud-private-rtb-2
        subnet_id: subnet-0ecaede6b638b07fc
    -   id: rtb-01ee1519ff260d689
        name: recloud-public-rtb-4
        subnet_id: subnet-020c6b76cfc125b0c
    -   id: rtb-0745b0de64741e298
        name: recloud-public-rtb-3
        subnet_id: subnet-0ed5773c5450b5d61
    -   id: rtb-04f66b922f2f31f6a
        name: recloud-public-rtb-5
        subnet_id: subnet-0ae6f639a9fbdc434
    subnets:
    -   availability_zone: ap-southeast-2a
        cidr: 10.0.64.0/24
        id: subnet-0f0aa5a62c9de53a8
        name: recloud-private-0
    -   availability_zone: ap-southeast-2b
        cidr: 10.0.65.0/24
        id: subnet-0b201e0178e4e3d78
        name: recloud-private-1
    -   availability_zone: ap-southeast-2c
        cidr: 10.0.66.0/24
        id: subnet-0ecaede6b638b07fc
        name: recloud-private-2
    -   availability_zone: ap-southeast-2a
        cidr: 10.0.0.0/24
        id: subnet-0ed5773c5450b5d61
        name: recloud-public-0
    -   availability_zone: ap-southeast-2b
        cidr: 10.0.1.0/24
        id: subnet-020c6b76cfc125b0c
        name: recloud-public-1
    -   availability_zone: ap-southeast-2c
        cidr: 10.0.2.0/24
        id: subnet-0ae6f639a9fbdc434
        name: recloud-public-2
    vpc:
        cidr: 10.0.0.0/16
        id: vpc-0558f9b9b2050dc79
        name: recloud-vpc
        state: available


The above inventory can be shown in the following diagram.

![Standard AWS OpenShift Architecture](../static/std-arch.png)