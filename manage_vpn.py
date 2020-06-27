#!/usr/bin/env python3

from tabulate import tabulate
import netifaces
import re
import os
import subprocess
import time
import psutil
import sys

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


def main_menu():
    stop = False
    opt_action = 0
    while not stop:
        print()
        print()
        print()
        print("Chose an action: \n")
        print("1. Up")
        print("2. Down")
        print("\n0. Exit")

        opt_action = getOption()
        if opt_action != 1 and opt_action != 2:
            if opt_action == 0:
                exit(0)
            else:
                print("ERROR: Chose a correct option")
        else:
            stop = True

    stop = False
    opt_vpn = 0
    while not stop:
        print()
        print()
        print()
        print("Chose a VPN connection: \n")
        dict_vpn = {}
        i = 0
        for k in vpns:
            i += 1
            print("{}. {}".format(i, k))
            dict_vpn[i] = k

        print("\n0. Exit")

        opt_vpn = getOption()

        if opt_vpn < 1 or opt_vpn > i:
            if opt_vpn == 0:
                exit(0)
            else:
                print("ERROR: Chose a correct option")
        else:
            manageVPN(opt_action, dict_vpn[opt_vpn])
            stop = True


def manageVPN(action, vpn):
    keys_path = "/home/gon/Documents/sys/vpn/userzoom"
    if vpn == "tun-office-bcn":
        daemon_name = "{}-{}".format(vpns[vpn][0], vpns[vpn][1])
        config_file = "{}.ovpn".format(daemon_name)
        config_path = "{}/{}/{}".format(keys_path, vpns[vpn][0], config_file)
        subfolder = "{}".format(vpns[vpn][0])
    else:
        daemon_name = "{}-{}-{}".format(vpns[vpn][0], vpns[vpn][1], vpns[vpn][2])
        config_file = "{}.ovpn".format(daemon_name)
        config_path = "{}/{}/{}".format(keys_path, vpns[vpn][0], config_file)
        subfolder = "{}".format(vpns[vpn][0])

    if not os.path.isfile(config_path):
        print("ERROR: OpenVPN config file '{}' doesn't exists".format(config_path))
        exit(2)

    vpn_running = getVPNAddresses()

    if action == 1:
        if vpn in vpn_running:
            print("VPN '{}' already up!".format(vpn))
        else:
            print("Go to start VPN '{}'".format(vpn))
            subprocess.run(
                [
                    "openvpn",
                    "--config",
                    config_file,
                    "--daemon",
                    "tun-{}".format(daemon_name),
                    "--log-append",
                    "/var/log/{}.log".format(daemon_name),
                ],
                cwd="{}/{}".format(keys_path, subfolder),
            )
            time.sleep(7)
            if getPidVPN("tun-".format(daemon_name)) == 0:
                print("Error starting VPN!")
                exit(2)

            print("\nVPN started!\n")

    elif action == 2:
        if vpn not in vpn_running:
            print("VPN '{}' already down!".format(vpn))
        else:
            print("Go to stop VPN '{}'".format(vpn))
            vpn_pid = getPidVPN("tun-".format(daemon_name))
            p = psutil.Process(vpn_pid)
            p.terminate()
            print("VPN '{}' finished!".format(vpn))


def getPidVPN(vpn_name):
    """
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    """

    list_process = []
    pid = 0

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name"])
            # Check if process name contains the given name string
            if "openvpn".lower() in pinfo["name"].lower():
                list_process.append(pinfo["pid"])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for pid in list_process:
        p = psutil.Process(pid)
        if vpn_name == p.cmdline()[4]:
            break

    return pid


def getOption():
    correct = False
    num = 0
    while not correct:
        try:
            num = int(input("> "))
            correct = True
        except ValueError:
            print("ERROR: Chose a correct option")

    return num


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


def checkSudo():
    # This script must be run as root!
    if not os.geteuid() == 0:
        sys.exit("ERROR: This script must be run as root!")


def main():
    checkSudo()
    dict_vpn = getVPNAddresses()
    print()
    print(tabulate(dict_vpn.items(), headers=["Interface", "IP Address"]))
    print()
    main_menu()


if __name__ == "__main__":
    main()
