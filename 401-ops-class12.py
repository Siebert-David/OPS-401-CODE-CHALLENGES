#!/usr/bin/python3

# Script Name:                 401-ops-class12.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     26JUL2023
# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed.

#import Libraries
#import ipaddress ( to provide subnet lists ) 
from ipaddress import IPv4Network
from scapy.all import ICMP, IP, sr1, TCP


#define variables -global-
network="10.0.2.0/24"  #ask user for this action 
#ip_list = Ipaddress.ip_network(network)# thank you Raphael in class chat
ip_list = Ipaddress.IPv4Network(network)
host_count = 0  # for poing sweep fx 
for ip in ip_list: # each item needs command to print.  
  print(i)


# Define Functions 

# Fx for ICMP ping sweep. reference gloabl variables 
def ping_sweep():
  # Add menu to request use CIDR block
  #IP list to reference- Generate IP list 
  global ip_list
  global host_count

  # Send ICMP request for each host
  for host in ip_list:
      if (host in (ip_list.network_address, ip_list.boradcast_address)):# calculates network address 
          #skip 0 & 255 and move to send icmp packet
          continue
          # Sends ICMP packet places it into a variable. 
          response +sr1(IP(dst=str(host))/ICMP(),timeout=12, verbose=0  #destinations host add value  ( only strings )  send icmp packet, verbose to get more infomration 

      elif(int(response.getlater(ICMP).type) == 3 and int(respose.getlayet(ICMP).code) in [1,2,3,9,10,13] ):
          print ("host is blocking traffic") #failure
        
      else:               
          print("host is responding") #positive
          host_count += 1 #redefine variable, adds 1 to the host count variable as we started with 0
                    #main
