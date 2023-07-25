#!/usr/bin/python3

# Script Name:                 401-ops-class12.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     26JUL2023
# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed.

#import Libraries
#import ipaddress # to provide subnet
from ipaddress import IPv4Network
from scapy.all import ICMP, IP, sr1, TCP


#define variables 
network="10.0.2.0/24"  #ask user for this action 
ip_list = ipaddress.IPv4NEtework(network).hosts()
print(ip_list)


# Define Functions 

#main
