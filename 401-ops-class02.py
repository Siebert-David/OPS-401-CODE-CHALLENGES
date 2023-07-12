#1/usr/bin/python3

# Script Name:                 401-ops-class02.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     11JUL2023
# In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down. Part 1 of 2 

#declare functions

#import libraries
import subprocess
import time
from datetime import datetime

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
def ping_host(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip])
        return True
    except subprocess.CalledProcessError:
        return False

# Evaluate the response as either success or failure.
# Assign success or failure to a status variable.
def main():
    ip = '8.8.8.8'  # IP address to ping
    while True:
        # For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        status = "Network Active" if ping_host(ip) else "Network Inactive"
        print(f"{timestamp} {status} to {ip}")
        time.sleep(2)

#call/run fx
if __name__ == "__main__":
    main()
