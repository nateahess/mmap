#!/usr/bin/env python
# Menus for MMAP

# Using this file to build menus separately from the main functions.

import sys
from banner import *
sys.path.append("/users/nate/appdata/local/programs/python/python39/lib/site-packages")
import colorama
from colorama import init
from colorama import Fore

init()

# ==============MAIN MENU=====================

def mainMenu():

    bannerOne()

    print( Fore.WHITE +

    """
    1. Common scans
    2. Favorites
    3. NSE Scripts
    4. Exit

    """
    )

# ===============COMMON SCANS====================

def commonScans():

    bannerThree()

    # Menu for common scan types

    print( Fore.WHITE +

    """

    1. Basic TCP Scan
    2. SYN Scan (Stealth)
    3. UDP Scan
    4. Detect OS and Services
    5. Standard Service Detection
    6. Scan from List
    7. Scan Single Port
    8. Scan All Ports
    9. Back to Main Menu


    """

    )

# ==================FAVORITES======================


def favoriteScans():

    bannerTwo()

# Describe your favorite scans below
# Add variables for them to nmap.py
# Map them to scanType in favorites.py

    print( Fore.WHITE +

    """

    1. Full Port Scan + Version Info
    2. Service Scan to Load with Searchsploit

    """

    )

# ====================SCRIPTS========================

def scriptScans():

    bannerFour()

    print ( Fore.WHITE +

    """

    1. Banner Grab
    2. DHCP Broadcast Discovery Scan
    3. DNS Brute Scan
    4. Traceroute Geolocation
    5. Host Discovery
    6. HTTP Enumeration 
    7. SMB Brute Scan
    8. SMB OS Discovery
    9. Standard Vulnaerability Scan

    """

    )
