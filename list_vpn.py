#!/usr/bin/env python3

from tabulate import tabulate
import netifaces
import re
import os
import subprocess
import time
import psutil

vpns = {
    "tun-uz-dev-euw1": ["uz", "dev", "eu-west-1"],
    "tun-uz-dev-use1": ["uz", "dev", "us-east-1"],
    "tun-uz-pre-euw1": ["uz", "pre", "eu-west-1"],
    "tun-uz-pre-use1": ["uz", "pre", "us-east-1"],
    "tun-uz-pro-euw1": ["uz", "pro", "eu-west-1"],
    "tun-uz-pro-use1": ["uz", "pro", "us-east-1"],
    "tun-uz-mdt-euw1": ["uz", "mdt", "eu-west-1"],
    "tun-uz-sbox-use1": ["uz", "sbox", "us-east-1"],
    "tun-office-bcn": ["office", "bcn"],
}


def getVPNAddresses():
    vpn_networks = {}
    r = re.compile(r"^tun-")
    interfaces = netifaces.interfaces()
    vpn_interfaces = list(filter(r.match, interfaces))

    if not vpn_interfaces:
        return vpn_networks
    else:
        for vpn in vpn_interfaces:
            addrs = netifaces.ifaddresses(vpn)
            vpn_addr = addrs[netifaces.AF_INET][0]["addr"]
            vpn_networks[vpn] = vpn_addr
        return vpn_networks


def main():
    dict_vpn = getVPNAddresses()
    print()
    print(tabulate(dict_vpn.items(), headers=["Interface", "IP Address"]))
    print()


if __name__ == "__main__":
    main()
