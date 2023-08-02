#!/usr/bin/python3

# Script Name:                 401-ops-class18.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     02AUG2023
# Automated Brute Force Wordlist Attack Tool Part 2 of 3. 

# import libraries 
from zipfile import ZipFile
from getpass import getpass

zip_file = input("PRovide Full filepath for zip file: ")
password = getpass("Provide the Password: ")

#Attempt to open the zip file with provided password. 
with ZipFile(zip_file) as zf:
    zf.extractall(pwd=bytes(password,'utf-8'))
