#1/usr/bin/python3

# Script Name:                 401-ops-class11.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     25JUL2023
# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed.

#import libraries
import sys
import scapy.all as scapy 

# define target host and TCP port to scan 
host = "scanme.nmap.org"
port_range = 22
scr_port = 22
dst_port = 22

#Single PING plus print the response packet
p=sr1(IP(dst=host)/ICMP())
if p:
  p.show()

#TCPpacket 
response= sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)
