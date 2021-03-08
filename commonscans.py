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
        elif commonSelection == 7:
            scanType = singlePort
        elif commonSelection == 8:
            scanType = allPorts
        elif commonSelection == 9:
            print("Returning to main menu...")
            mainMenu()
            menu()

        # Setting up options for common scans
        # File path is currently mapped to user's desktop

        if commonSelection == 6:
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for output file: ")
                pathToList = input("Enter path to list of targets: ")
                userName = getpass.getuser()
                filePath = "C:/users/" + userName + "/desktop/" + fileName
                os.system('cmd /k' + "nmap " + "-oN " + filePath  + scanType + pathToList)
            else:
                os.system('cmd /k' + "nmap " + scanType + pathToList)

        elif commonSelection == 7:
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                ipAddress = input("Enter target IP: ")
                portNumber = input("Enter port to scan (e.g. 80): ")
                userName = getpass.getuser()
                filePath = "c:/users/" + userName + "/desktop/" + fileName
                os.system('cmd /k' + "nmap " + "-oN " + filePath  + scanType + portNumber + ipAddress)
            else:
                ipAddress = input("Enter target IP: ")
                portNumber = input("Enter port to scan (e.g. 80): ")
                os.system('cmd /k' + "nmap " + scanType + portNumber + ipAddress)

        while commonSelection != 6 or 7:
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                ipAddress = input("Enter target IP: ")
                fileName = input("Name for file: ")
                userName = getpass.getuser()
                filePath = "C:/users/" + userName + "/desktop/" + fileName
                os.system('cmd  /k' + "nmap " + "-oN " + filePath  + scanType + ipAddress)
            elif fileSave == "n":
                ipAddress = input("Enter target IP: ")
                os.system('cmd /k' + "nmap " + scanType + ipAddress)
