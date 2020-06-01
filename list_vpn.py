#!/usr/bin/env python3

from tabulate import tabulate
import netifaces
import re
import os

vpns = {
    "tun-uz-dev-euw1": ["uz", "dev", "eu-west-1"],
    "tun-uz-dev-use1": ["uz", "dev", "us-east-1"],
    "tun-uz-pre-euw1": ["uz", "pre", "eu-west-1"],
    "tun-uz-pre-use1": ["uz", "pre", "us-east-1"],
    "tun-uz-pro-euw1": ["uz", "pro", "eu-west-1"],
    "tun-uz-pro-use1": ["uz", "pro", "us-east-1"],
    "tun-uz-mdt-euw1": ["uz", "mdt", "eu-west-1"],
    "tun-uz-sbox-use1": ["uz", "sbox", "us-east-1"],
}


def main_menu():
    stop = False
    opt_action = 0
    while not stop:
        print("Chose an action: \n")
        print("1. Up")
        print("2. Down")
        print("\n0. Exit")

        opt_action = getOption()

        if opt_action != 1 or opt_action != 2:
            if opt_action == 0:
                stop = True
            else:
                print("Chose a correct option")

    stop = False
    opt_vpn = 0
    while not stop:
        print("Chose a VPN connection: \n")
        dict_vpn = {}
        i = 0
        for k in vpns:
            i += 1
            print("{}. {}".format(i, k))
            dict_vpn[i] = k

        print("0. Exit")

        opt_vpn = getOption()

        if opt_vpn < 1 or opt_vpn > i:
            if opt_vpn == 0:
                stop = True
            else:
                print("Chose a correct option")
        else:
            manageVPN(opt_action, dict_vpn[opt_vpn])


def manageVPN(action, vpn):
    keys_path = "/home/gon/Documents/sys/vpn/userzoom"
    config_file = "{}-{}-{}.ovpn".format(vpns[vpn][0],
                                         vpns[vpn][1],
                                         vpns[vpn][2])
    config_path = "{}/{}/{}".format(keys_path, vpns[vpn][0], config_file)

    if not os.path.isfile(config_path):
        print("ERROR: OpenVPN config file '{}' doesn't exists".format(config_path))
        exit(2)

    vpn_running = getVPNAddresses()

    if action == 1:
        if vpn in vpn_running:
            print("VPN '{}' already up!".format(vpn))
        else:
            pass  # TODO


def getOption():
    correct = False
    num = 0
    while(not correct):
        try:
            num = int(input("> "))
            correct = True
        except ValueError:
            print("ERROR: Chose a correct option")

    return num


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

    main_menu()


if __name__ == '__main__':
    main()
