#!/usr/bin/python3

# Script Name:                 401-ops-class12.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     26JUL2023
# In Python, create a ICMP ping sweep & TCP Port Range Scanner that tests whether a TCP port is open or closed.

# havtn run yet so im sure there is a bug in here... for the life of me vscode has something against me. 

#import Libraries
#import ipaddress ( to provide subnet lists ) 
#scapy 
from ipaddress import IPv4Network
from scapy.all import ICMP, IP, sr1, TCP


#define variables -global-
network =input("Enter IP/CIDR block address")  #ask user for this action 
#ip_list = Ipaddress.ip_network(network)# Reference Raphael in class chat
#ip_list = Ipaddress.IPv4Network(network)
ip_list = list(IPv4Network(network).hosts())  # Get a list of all addresses in the network
host_count = 0  # starting number for ping sweep fx 
for ip in ip_list: # each item needs command to print.  
  print(i)


# Define Functions 

#Fx for TCP port Scanning. Reference global 
 def tcp_port_scan():
    global ip_list
    global host_count

    # Send TCP SYN request for each host and port (all available ports)
    for host in ip_list:
        if host in (ip_list[0], ip_list[-1]):  # Skip network and broadcast addresses
            continue

        for port in range(1, 65536):  # Scan all available ports (maybe limit this)
            response = sr1(IP(dst=str(host))/TCP(dport=port, flags="S"), timeout=1, verbose=0)

            if response is None:
                print(f"{host}:{port} is closed or unresponsive.")
            elif response.haslayer(TCP) and response[TCP].flags == "SA":
                print(f"{host}:{port} is open.")
                host_count += 1
            else:
                print(f"{host}:{port} is closed.") 



# Fx for ICMP ping sweep. reference global variables 
def ping_sweep():
  # Add menu to request use CIDR block
  #Generate IP list 
  global ip_list
  global host_count

  # Send ICMP request for each host
  for host in ip_list:
      if (host in (ip_list.network_address, ip_list.boradcast_address)):# calculates network address 
          #skip 0 & 255 send icmp packet
          continue #Marco advised
          # Sends ICMP packet to host Variable then places it into a variable. sr1 -send one recieve one
          response +sr1(IP(dst=str(host))/ICMP(),timeout=12, verbose=0  #destinations dst host/ converts IP in the host variable to string format. sends icmp packet, verbose to remain silent

      elif(int(response.getlater(ICMP).type) == 3 and int(response.getlayet(ICMP).code) in [1,2,3,9,10,13] ): #https://www.geeksforgeeks.org/internet-control-message-protocol-icmp/
          print ("host is blocking traffic") #failure
        
      else:               
          print("host is responding") #positive
          host_count += 1 #redefine variable, adds 1 to the host count variable as we started with 0

                   
                    
#Menu 
print("Choose an Option:")
print("1. TCP Port Range Scanner")
print("2. ICMP Ping Sweep")
choice = int(input("Enter 1 or 2: "))

if choice == 1:
    tcp_port_scan()
    print(f"{host_count} hosts have open ports.")
elif choice == 2:
    ping_sweep()
    print(f"{host_count} hosts are online.")
else:
    print("Pay attention and Choose 1 or 2.")


# references
# Marco set up most(if not all) of the script in class demo
# Raphael Chookagain on alt IP request
# https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
# https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
# https://github.com/SwathiPrathaa/TCP-Port-Scan-over-ICMP-Ping-Sweep/blob/main/main.py
# https://stackoverflow.com/questions/68111001/scapy-port-scanner-with-cidr-ip-range-or-single-ip-domain-input
# open.AI menu set up recommendations, scapy command quick searches
# https://stackoverflow.com/questions/66648167/how-to-create-menu-in-python-with-multiple-if-statements
# PY3 continue/break/pass as introduced by marco https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
