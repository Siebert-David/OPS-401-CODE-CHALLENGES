#!/usr/bin/python3

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
response = sr1(IP(dst="8.8.8.8")/TCP(sport=22))
response = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="S"),timeout=1, verbose=0)

#Verify that data is TCP packet
if (response.haslayer(TCP)):
  if (response.getlayer(TCP).flags == 0x12):
    send_rst = sr1(IP(dst=host)/TCP(sport=scr_port,dport=dst_port,flags="R"),timeout=1, verbose=0)
    print(f"{host}:{dst_port} is open")
    print(host + str(dst_port) + "is open")
else:
  print("Unresponsive Host") 
# 0x14 + notify User
elif  

# no flag received
