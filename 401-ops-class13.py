#!/usr/bin/python3

# Script Name:                 401-ops-class13.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     27JUL2023
# In Python, create an ICMP ping sweep & TCP Port Range Scanner that tests whether a TCP port is open or closed.

#import Libraries
import scapy.all import ICMP, IP, sr1, TCP
from ipaddress import IPv4Network


# Fx for TCP port Scanning
def tcp_port_scan(host):
    # Send TCP SYN request for each host and port (all available ports)
    for port in range(1, 65536):
        response = sr1(IP(dst=str(host))/TCP(dport=port, flags="S"), timeout=1, verbose=0)

        if response is None:
            print(f"{host}:{port} is closed or unresponsive.")
        elif response.haslayer(TCP) and response[TCP].flags == "SA":
            print(f"{host}:{port} is open.")
        else:
            print(f"{host}:{port} is closed.") 

# Fx for ICMP ping sweep.
def ping_sweep(host):
    # Send ICMP request for each host
    response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
    if response is None:
        print(f"{host} is not responding.")
        return False  # Return False if the host is not responsive
    elif int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]:
        print(f"{host} is blocking traffic.")
        return False  # Return False if the host is blocking traffic
    else:
        print(f"{host} is responding.")
        return True  # Return True if the host is responsive

# Main code
while True:
    target_ip = input("Enter the target IP address (or 'exit' to quit): ")
    if target_ip.lower() == 'exit':
        break

    # ICMP ping sweep
    if ping_sweep(target_ip):
        # TCP port scan if the host is responsive to ICMP echo requests
        tcp_port_scan(target_ip)

# references
# 401-ops-class12.py & 401-ops-class11.py
# Marco set up most(if not all) of the script in class demo
# Raphael Chookagain on alt IP request
# https://wiki.sans.blue/Tools/pdfs/ScapyCheatSheet_v0.2.pdf
# https://stackoverflow.com/questions/26174743/making-a-fast-port-scanner
# https://github.com/SwathiPrathaa/TCP-Port-Scan-over-ICMP-Ping-Sweep/blob/main/main.py
# https://stackoverflow.com/questions/68111001/scapy-port-scanner-with-cidr-ip-range-or-single-ip-domain-input
# open.AI menu set up recommendations, scapy command quick searches
# https://stackoverflow.com/questions/66648167/how-to-create-menu-in-python-with-multiple-if-statements
# PY3 continue/break/pass as introduced by marco https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3
