#!/usr/bin/env python
# MMAP 1.0
# Author: @nahberry
# Description: Python script for running go-to nmap scans

from banner import *
from menu import *
from commonscans import *
from favorites import *
from scripts import *

def main():

    selectionOne = 0

    while selectionOne != 4:

        selectionOne = int(input("Please Select an Option: "))

        if selectionOne == 1:
            commonScanSelection()

        elif selectionOne == 2:
            favoriteSelection()

        elif selectionOne == 3:
            scriptSelection()

        elif selectionOne == 4:
            print("Exiting...")
            os.system('cmd /k')

mainMenu()
main()
