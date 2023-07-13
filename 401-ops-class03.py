#1/usr/bin/python3

# Script Name:                 401-ops-class03.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     11JUL2023
# In Python, create an uptime sensor tool that uses ICMP packets to evaluate if hosts on the LAN are up or down WITH EMAIL SENT UP AND DOWN ALERTS. Part 2 of 2 

#declare functions

#import libraries
import subprocess
import time
from datetime import datetime

#declare variables

up = "host is active"
down = "host is down"

# intialize variables the we are going to use for comparison
last = 0
ping_result = 0

email = input("enter your email: ")
password = getpass("enter your password: ")
ip = input("what IP would you like to monitor? ")

#declare functions

#funtion to handle the up alert Down to UP
def send_upAlert():
    now = datetime.datetime.now()

    #start smtp session
    s = smtplib.SMTP('smtp.gmail.com', '587')

    #TLS FOR ENCRYPTION
    s.starttls()

    #authentication to the email account
    s.login(email, password)

    message = "your Server is UP and Running"

    #senging the email
    s.sendmail("bot@serverwatch.com", email, message)

    #close the session
    s.quit()

#function to handle the down alert. From Up to Down
def send_downAlert():
     now = datetime.datetime.now()

    #start smtp session
    s = smtplib.SMTP('smtp.gmail.com', '587')

    #TLS FOR ENCRYPTION
    s.starttls()

    #authentication to the email account
    s.login(email, password)

    message = "your Server is DEAD DEAD"

    #senging the email
    s.sendmail("bot@serverwatch.com", email, message)

    #close the session
    s.quit()

#function to hadle the ping test
def ping_test():
    now = datetime.datetime.now()

    global ping_result #starts being 0 
    global last #starts being 0

    # ping result check - logic -
    if ((ping_result != last)  and  (ping_result == up)):

        #change value of last
        last = up
        #calling the function to send email.
        send_upAlert()
    elif((ping_result != last) and (ping_result == down)):

        #change the value of the last
        last = down
        #call the Fx to send the email
        send_downAlert()

    #perform the ping + variable for response. 
    response = os.system("ping -c 1 " + ip)

    #eval ping response
    if response == 0:
            pin_result = up 
    else:
        ping_result = down 
    print(str(now) + ping_result + " to "  + ip)

#main

# infinite heartbeat loop 


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

#refernced python.org & open ai to check why it wanst working.
