#!/usr/bin/python3

import ipaddress
import argparse

parser = argparse.ArgumentParser(description='Output the first and last host from a provided network CIDR')
parser.add_argument('--cidr', type=str, help='CIDR for the VPC')

args = parser.parse_args()

try:
    cidr = ipaddress.ip_network(args.cidr, strict=False)

    # Calculate the last host
    hosts = cidr.num_addresses

    # Calculate list of hosts
    hostList = list(cidr.hosts())

    # Output the result
    print("First host IP =",hostList[0])
    print("Last host IP = ",hostList[hosts-3])
    print("Broadcast address =",cidr.broadcast_address)
    print("Splitting into 2 subnets (prefix offset of 1)\n",list(cidr.subnets()))
    print("Splitting subnet into 4 (prefix offset of 2)\n",list(cidr.subnets(prefixlen_diff=2)))
    print("Supernet is ",cidr.supernet())

except ValueError:
    print('ERROR: Invalid input CIDR, please check')