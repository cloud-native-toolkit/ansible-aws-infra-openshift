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




## References

[Red Hat Ansible collection repository](https://console.redhat.com/ansible/automation-hub)
