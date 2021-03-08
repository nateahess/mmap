#!/usr/bin/env python
#This file contains variables for nmap scans

# Leave a trailing space at the end of options so an IP Address can be added when running.

# Common Scans
tcpScan = "-sT "
synScan = "-sS "
udpScan = "-sU "
osandServices = "-A "
serviceScan = "-sV "
listScan = "-iL "
singlePort = "-p "
allPorts = "-p- "

# Favorite Scans
favoriteOne = "-vv -n -p- -sV "
favoriteTwo = "-sV -oX "

# NSE Scripts
bannerGrab = "-sV --script=banner "
broadcastDHCP = "--script broadcast-dhcp-discover "
dnsBrute = " -p 80 --script dns-brute.nse "
geolocateTrace = "--traceroute --script traceroute-geolocation.nse -p 80 "
hostDiscovery = " -p 80 --script hostmap-bfk.nse "
httpEnum = "--script http-enum "
smbBrute = "-sV -p 445 --script smb-brute "
smbOS = "-p 445 --script smb-os-discovery "
vulnScan = "-sS --script vuln "
