#!/usr/bin/env python3

# import psutil
# from tabulate import tabulate
# import netifaces
# import re
# import pprint
import argparse


# def findProcessIdByName(process_name):
#     '''
#     Get a list of all the PIDs of a all the running process whose name contains
#     the given string processName
#     '''

#     list_of_process = []

#     # Iterate over the all the running process
#     for proc in psutil.process_iter():
#         try:
#             pinfo = proc.as_dict(attrs=['pid', 'name'])
#             # Check if process name contains the given name string.
#             if process_name.lower() in pinfo['name'].lower():
#                 list_of_process.append(pinfo['pid'])
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass

#     return list_of_process


# def getParametersProcessByPid(list_pid):
#     list_of_parameters = []
#     for pid in list_pid:
#         p = psutil.Process(pid)
#         list_of_parameters.append(p.cmdline()[2])
#     # print(list_of_parameters)
#     return list_of_parameters


# def getVPNAddresses():
#     vpn_networks = {}
#     r = re.compile(r'^tun-')
#     interfaces = netifaces.interfaces()
#     vpn_interfaces = list(filter(r.match, interfaces))

#     if not vpn_interfaces:
#         return vpn_networks
#     else:
#         for vpn in vpn_interfaces:
#             addrs = netifaces.ifaddresses(vpn)
#             vpn_addr = addrs[netifaces.AF_INET][0]['addr']
#             vpn_networks[vpn] = vpn_addr
#         return vpn_networks


# openvpn_pids = findProcessIdByName("openvpn")
# list_openvpn_parameters = getParametersProcessByPid(openvpn_pids)


# pprint.pprint(dict_vpn)
# print(tabulate(list_openvpn_parameters))

def up():
    return "up"


def down():
    return "down"


def status():
    return "status"


def main():
    parser = argparse.ArgumentParser(description='Turn up/down different VPNs')
    parser.add_argument("-p", "--platform",
                        choices=['uz', 'px', 'se', 'it'],
                        help="Set platform to connect")
    parser.add_argument("-e", "--environment",
                        choices=['dev', 'pre', 'pro', 'sbox', 'mdt'],
                        help="Set environment to connect")
    parser.add_argument("-r", "--region",
                        choices=['eu-west-1', 'eu-central-1', 'us-east-1'],
                        help="Set region to connect")
    parser.add_argument("-a", "--action",
                        choices=['up', 'down', 'status'])
    args = parser.parse_args()

    switcher = {
        "up": up(),
        "down": down(),
        "status": status()
    }


if __name__ == '__main__':
    main()
