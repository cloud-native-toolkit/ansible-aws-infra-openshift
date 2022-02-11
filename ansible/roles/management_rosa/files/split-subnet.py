#!/usr/bin/python3
# 
# Provides the first available subnets up to the provided quantity needed of a requested subnet prefix
# 
#

import argparse
from array import array
import string
import ipaddress

parser = argparse.ArgumentParser(description='Output a JSON file with the first subnet CIDRs for a given VPC CIDR')
parser.add_argument('--cidr', type=str, help='CIDR for the VPC, minimum of /13')
parser.add_argument('--prefix', type=int, help='Prefix for each subnet')
parser.add_argument('--count', type=int, help='Number of subnets to split into')

args = parser.parse_args()

try: 
    vpc_cidr = ipaddress.ip_network(args.cidr, strict=False)

    all_subnets = list(vpc_cidr.subnets(new_prefix=args.prefix))

    x=0
    while (x<args.count):
        print(str(all_subnets[x]))
        x=x+1

except ValueError:
    print('ERROR: Invalid input CIDR, please check')