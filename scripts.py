#!/usr/bin/env python
#script Nmap Commands
# Use this file to build your script commands.

import os
import getpass
from mmap import *
from nmap import *
from menu import *

def scriptSelection():

    scriptScans()

    scriptSelection = 0
    while scriptSelection != 4:

        scriptSelection = int(input("Select a script: "))

        if scriptSelection == 1:
            scanType = bannerGrab
        elif scriptSelection == 2:
            scanType = broadcastDHCP
        elif scriptSelection == 3:
            scanType = dnsBrute
        elif scriptSelection == 4:
            scanType = geolocateTrace
        elif scriptSelection == 5:
            scanType = hostDiscovery
        elif scriptSelection == 6:
            scanType = httpEnum
        elif scriptSelection == 7:
            scanType = smbBrute
        elif scriptSelection == 8:
            scanType = smbOS
        elif scriptSelection == 9:
            scanType = vulnScan
        elif scriptSelection == 10:
            print("Returning to main menu...")
            os.system("python3 mmap.py")

        if scriptSelection == 2:
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                os.system('cmd /k' + "nmap " + "-oN " + fileName + ' ' + scanType)
            elif fileSave == "n":
                os.system('cmd /k' + "nmap " + fileName + ' ' + scanType)

        while scriptSelection != 2 or 10:
            ipAddress = input("Enter Target IP: ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                os.system('cmd /k' + "nmap " + "-oN " + fileName + ' ' + scanType + ' ' + ipAddress)
            elif fileSave == "n":
                os.system('cmd /k' + "nmap " + scanType + ' ' + ipAddress)
