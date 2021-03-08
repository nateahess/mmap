#!/usr/bin/env python

# Common scan types

import os
import getpass
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
            pathToList = input("Path to list: ")
        elif commonSelection == 7:
            scanType = singlePort
            portNumber = input("Enter port to scan (e.g. '-80'): ")
        elif commonSelection == 8:
            scanType = allPorts
        elif commonSelection == 9:
            print("Returning to main menu...")
            mainMenu()
            menu()


        # Setting up options for common scans
        # File path is currently mapped to user's desktop

        while commonSelection != 6 or 7:
            ipAddress = input("Enter Target IP: ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                userName = getpass.getuser()
                filePath = "C:/users/" + userName + "/desktop/" + fileName + ".txt "
                os.system('cmd /k' + "nmap " + "-oN " + filePath  + scanType + ipAddress)

        if commonSelection == 6:
            if fileSave == "y":
                os.system('cmd /k' + "nmap " + "-oN " + filePath  + scanType + pathToList + ipAddress)
            else:
                os.system('cmd /k' + "nmap " + scanType + pathToList + ipAddress)

        elif commonSelection == 7:
            if fileSave == "y":
                os.system('cmd /k' + "nmap " + "-oN " + filePath  + scanType + portNumber + ipAddress)
            else:
                os.system('cmd /k' + "nmap " + scanType + portNumber + ipAddress)
