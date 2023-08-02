#!/usr/bin/python3

# Script Name:                 401-ops-class17.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     02AUG2023
# Automated Brute Force Wordlist Attack Tool Part 2 of 3. 


# need to finish these below **************
# finish + run 
# password list to reference rockyou-shortened
#  menu for function 


# Import Libraries
import paramiko
import import time 
from getpass import getpass

#Define variables
host - input ("Please provide the IP address you want to SSH to: °)
user = input ("Please provide a username:
password = getpass ("Please provide your password:
port = 22

# Create an object that handles the SSH connection
ssh = paramiko. SSHClient()

# Adding new host key to the local
# Hostkeys object (in case of missing)
# AutoAddPolicy for missing host key to be set before connection setup.

try:
    ssh. connect(host, port, user, password)
# Runs whoami in the other machine we SSH to
    stdin, stdout, stderr - ssh.exec_command ("whoami") 
    time.sleep(3)
    output = stdout. read()
    print (output)
    stdin, stdout, stderr - ssh.exec_command ("ls -1") time. sleep (3)
    output = stdout. read()
    print (output)
    stdin, stdout, stderr = ssh.exec_command ("pwd")
    time.sleep (3)
    output - stdout. read ()
    print (output)
except paramiko. AuthenticationException() as e:
    print("Authentication Failed")
    print(e)

ssh.close()



# references
# MARCO VAZQUEZ - As always an excellent/indepth & informative overview with clear instruction on -why- the while loop & -why- the line = file.readline() must be in that loop
# rstrip https://stackoverflow.com/questions/36969248/how-use-line-rstrip-in-python
# readline https://www.w3schools.com/python/ref_file_readline.asp
# append https://www.w3schools.com/python/ref_list_append.asp
