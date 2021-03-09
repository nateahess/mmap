#!/usr/bin/env python

# Common scan types

import os
from mmap import *
from nmap import *
from menu import *

def commonScanSelection():

    #Load common scans menu
    commonScans()

    commonSelection = 0
    while commonSelection != 10:

        commonSelection = int(input("Select a Common Scan: "))

        # Map common scans to scanType variable
        if commonSelection == 1:
            scanType = tcpScan
        elif commonSelection == 2:
            scanType = synScan
        elif commonSelection == 3:
            scanType = udpScan
        elif commonSelection == 4:
            scanType = osandServices
        elif commonSelection == 5:
            scanType = serviceScan
        elif commonSelection == 6:
            scanType = listScan
        elif commonSelection == 7:
            scanType = singlePort
        elif commonSelection == 8:
            scanType = allPorts
        elif commonSelection == 9:
            print("Returning to main menu...")
            os.system("python3 mmap.py")


        # Setting up options for common scans
        # File path is currently mapped to user's desktop

        if commonSelection == 6:
            pathToList = input("Enter path to list of targets: ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for output file: ")
                os.system('cmd /k' + "nmap " + "-oN " + fileName + ' ' + scanType + ' ' + pathToList)
            else:
                os.system('cmd /k' + "nmap " + scanType + ' ' + pathToList)

        elif commonSelection == 7:
            ipAddress = input("Enter target IP: ")
            portNumber = input("Enter port to scan (e.g. 80): ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                os.system('cmd /k' + "nmap " + "-oN " + fileName + ' ' + scanType + ' '+ portNumber + ' ' + ipAddress)
            else:
                os.system('cmd /k' + "nmap " + scanType + ' ' + portNumber + ' ' + ipAddress)

        while commonSelection != 6 or 7:
            ipAddress = input("Enter target IP: ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                os.system('cmd  /k' + "nmap " + "-oN " + fileName + ' ' + scanType + ' ' + ipAddress)
            elif fileSave == "n":
                os.system('cmd /k' + "nmap " + scanType + ' ' + ipAddress)
