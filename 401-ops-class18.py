#!/usr/bin/python3

# Script Name:                 401-ops-class18.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     02AUG2023
# Automated Brute Force Wordlist Attack Tool Part 2 of 3. 


# import libraries 
from zipfile import ZipFile
from getpass import getpass
import time

----------------------------------------------------------
zip_file = input("PRovide Full filepath for zip file: ")
password = getpass("Provide the Password: ")

#Attempt to open the zip file with provided password. 
with ZipFile(zip_file) as zf:
    zf.extractall(pwd=bytes(password,'utf-8'))

---------------------------------------------------------------

#declare functions ( from Marco inclass review) 
def crack_file():
    the_file = input("please input the full path : ")
    filepath = input( "provide filepath for password wordlist: ")
    file = open(filepath, 'r')

    #reads in the first line of wordlist 
    line = file.readline()

    success = "no"

    #if statement 
    if success == "no"
        #do this 
        while line: 
            line = line.rstrip()
            password = line
            print(f"checking '{password}")

            try:
                with ZipFile(the_file) as zf:
                    zf.extractall(pwd=bytes(password, 'utf-8'))
                success = "yes" #breaks out of while loop
                print(f"[*] File opened with '{password}' - retunring to menu. [*]")
                break

            except:
                pass

            time.sleep(.5)
            line = file.readline()
        file.close()

#chmod +x 401-ops-class18.py