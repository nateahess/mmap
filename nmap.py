#!/usr/bin/env python
#This file contains variables for nmap scans

#Common Scans
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
