#!/usr/bin/python3

# Script Name:                 401-ops-class26_event_logging.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     14DEC2023
# Event logging tool Part 1 of 3. 
# Combined Script for ICMP Ping Sweep, TCP Port Range Scanner and Logging

# Import Libraries
import logging
from scapy.all import ICMP, IP, sr1, TCP
from ipaddress import IPv4Network

# Configure Basic Logger Settings
logging.basicConfig(filename="network_scan.log", format='%(asctime)s %(message)s', filemode='w')

# Creating Logger Object
log = logging.getLogger("network_logger")

# Setting the Level of Message to Log
log.setLevel(logging.INFO)

# Function for TCP Port Scanning
def tcp_port_scan(host):
    log.info(f"Starting TCP port scan on {host}")
    for port in range(1, 1025):  # Scanning common ports for brevity
        try:
            response = sr1(IP(dst=str(host))/TCP(dport=port, flags="S"), timeout=1, verbose=0)
            if response is None:
                log.debug(f"{host}:{port} is closed or unresponsive.")
            elif response.haslayer(TCP) and response[TCP].flags == "SA":
                log.info(f"{host}:{port} is open.")
            else:
                log.debug(f"{host}:{port} is closed.")
        except Exception as e:
            log.error(f"Error scanning {host}:{port} - {e}")

# Function for ICMP Ping Sweep
def ping_sweep(host):
    log.info(f"Starting ICMP ping sweep on {host}")
    try:
        response = sr1(IP(dst=str(host))/ICMP(), timeout=1, verbose=0)
        if response is None:
            log.warning(f"{host} is not responding.")
            return False
        elif int(response.getlayer(ICMP).type) == 3:
            log.warning(f"{host} is blocking ICMP traffic.")
            return False
        else:
            log.info(f"{host} is responding.")
            return True
    except Exception as e:
        log.error(f"Error during ping sweep of {host} - {e}")
        return False

# Main Code
while True:
    target_ip = input("Enter the target IP address (or 'exit' to quit): ")
    if target_ip.lower() == 'exit':
        log.info("User requested to exit.")
        break

    if ping_sweep(target_ip):
        tcp_port_scan(target_ip)

log.info("Script execution completed.")
