# Addon Client VPN Endpoint on AWS

Provisions an AWS OpenVPN client VPN endpoint to an existing VPC. Can pull inventory information from a prior build, or define within this tool.

## Software Dependencies

The module depends upon the following software components being installed on the build machine.

### Command-line Tools

- Ansible version 2.12.1 or higher (follow the guide [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))
- AWS CLI version 2.4.11 or higher (follow the guide [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))

### Subscription Dependencies

- AWS administrative access

## Bill of Materials 

AWS OpenVPN Client VPN Endpoint server with mutual authentication.

## Example Usage

1. Ensure that a boto profile is created and AWS CLI is installed (if not follow guide [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))

        $ aws ec2 describe vpcs

Should return information on the current VPCs for your default region. <i>The default region needs to be the same as the one in which the advanced architecture is to be built.</i>

1. Ensure the aws configuration returns JSON format (this is required for some of the automation steps)

        $ cat ~/.aws/config

        [default]
        ...
        output = json

1. Clone this repository

    $ git clone https://github.com/cloud-native-toolkit/ibm-aws-reference-arch-ansible

1. Create certificate pair and upload to the AWS Certificate Manager

    1. [Create an RSA certificate](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html) 

    1. Go to AWS Certificate Management (ACM) and confirm certificates are uploaded

    ![Uploaded certificates](./static/uploaded-certificates.png)

1. Edit the create-client-cvpn.yaml file for the required configuration.

      vars:
        server_cert: arn:aws:acm:ap-southeast-2:000000000000:certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
        client_cert: arn:aws:acm:ap-southeast-2:000000000000:certificate/ffffffff-cccc-eeee-0000-aaaaaaaaaaaa
        client_cidr: 10.100.0.0/18

        # Uncomment and modify the below to overwrite an existing inventory file (which will use the edge VPC details from inventory)
        #
        #local_name: "recloud-cvpn"
        #resource_group: "recloud"
        #vpc_id: vpc-456789123
        #subnet_list:
        #  - subnet-123456789
        #  - subnet-987654321
        #  - subnet-765438976
        #authorized_cidrs:
        #- 10.0.0.0/16
        #- 10.1.0.0/16

1. Create the Client VPN Endpoint

    $ ansible-playbook ./create-client-vpn.yaml

1. Post installation, logon to the AWS Console and download the client configuration file. Then start an OpenVPN client session on the client.

    1. Connect the client

            $ sudo openvpn --config ~/Documents/vpn-config.ovpn

    ![OpenVPN connection output - begining](./static/openvpn-connection-1.png)
    ![OpenVPN connection output - complete](./static/openvpn-connection-2.png)

1. The client will now appear as a network device in the VPC. 
