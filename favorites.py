#!/usr/bin/env python
#Favorite Nmap Commands
# Use this file to build your favorite commands.

import os
import getpass
from mmap import *
from nmap import *
from menu import *

def favoriteSelection():

    favoriteScans()

    favoriteSelection = 0
    while favoriteSelection != 4:

        favoriteSelection = int(input("Select a Common Scan: "))

        # Map favorite commands from nmap.py to the menu options from menu.py
        # May automate all of this in the future but this code is so simple it didn't feel worth it

        if favoriteSelection == 1:
            scanType = favoriteOne
        elif favoriteSelection == 2:
            scanType = favoriteTwo
        elif favoriteSelection == 3:
            print('Returning to Main Menu...')

        # Setting up options for your Commands
        # Filepath is currently mapped to the user's Desktop
        # Pay attention to the order of filePath, scanType, etc. on the os.system line.

        while favoriteSelection != 2 or 3:
            ipAddress = input("Enter Target IP: ")
            fileSave = input("Save output? (y/n): ")
            if fileSave == "y":
                fileName = input("Name for file: ")
                userName = getpass.getuser()
                filePath = "C:/users/" + userName + "/desktop/" + fileName + ".txt "
                os.system('cmd /k' + "nmap " + "-oN " + filePath + scanType + ipAddress)

        # My second favorite command outputs and XML file for searchploit.
        # I've separated it here since it does not require a "Y/N answer for fileSave"

        if favoriteSelection == 2:
            ipAddress = input("Enter Target IP: ")
            fileName = input("Name for file: ")
            userName = getpass.getuser()
            filePath = "C:/users/" + userName + "/desktop/" + fileName + ".txt"
            os.system('cmd /k' + "nmap " + scanType + filePath + ipAddress)
