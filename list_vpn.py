#!/usr/bin/env python3

from tabulate import tabulate
import netifaces
import re


def getVPNAddresses():
    vpn_networks = {}
    r = re.compile(r'^tun-')
    interfaces = netifaces.interfaces()
    vpn_interfaces = list(filter(r.match, interfaces))

    if not vpn_interfaces:
        return vpn_networks
    else:
        for vpn in vpn_interfaces:
            addrs = netifaces.ifaddresses(vpn)
            vpn_addr = addrs[netifaces.AF_INET][0]['addr']
            vpn_networks[vpn] = vpn_addr
        return vpn_networks


def main():
    dict_vpn = getVPNAddresses()
    print()
    print(tabulate(dict_vpn.items(), headers=["Interface", "IP Address"]))


if __name__ == '__main__':
    main()
