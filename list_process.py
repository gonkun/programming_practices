#!/usr/bin/env python3

import psutil


def findProcessIdByName(process_name):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''

    list_of_process = []

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            # Check if process name contains the given name string.
            if process_name.lower() in pinfo['name'].lower():
                list_of_process.append(pinfo['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return list_of_process


def getParametersProcessByPid(list_pid):
    for pid in list_pid:
        p = psutil.Process(pid)
        print(p.cmdline())


openvpn_pids = findProcessIdByName("openvpn")
getParametersProcessByPid(openvpn_pids)
