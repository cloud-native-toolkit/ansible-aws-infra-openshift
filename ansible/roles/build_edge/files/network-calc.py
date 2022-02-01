#!/usr/bin/python3
# 
# This code creates the subnet CIDRs for the FS Cloud breakdown from the input VPC CIDRs
#
#

import argparse
from array import array
import string
import ipaddress

parser = argparse.ArgumentParser(description='Output a JSON file with the subnet CIDRs for a given VPC CIDR')
parser.add_argument('cidr', type=str, help='CIDR for the VPC, minimum of /13')

args = parser.parse_args()

# Parse CIDR into IP address class for processing

try: 
    vpc_cidr = ipaddress.ip_network(args.cidr, strict=False)

    # Check that the provided CIDR is large enough to split into 9 subnets

    ingress_subnet1 = vpc_cidr

    print(ingress_subnet1)

except ValueError:
    print('ERROR: Invalid input CIDR, please check')