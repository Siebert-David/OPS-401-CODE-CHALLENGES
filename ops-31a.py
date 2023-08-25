#!/usr/bin/python3

# Script Name:                 401-ops-class31a.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     22AUG2023
# Part 1 of 3



#import libraries
import os, time
import platform 
#from sys import platform 

#define variables
my_os = platform.system()
print(my_os)

#define functions 

#search for linux
def linuxSearch():
    whichFile = input("what file are you looking for?")
    directory = input("which directory would you like to search")

    #count and print the number of files searched
    os.system("ls " + str(directory) + " | echo \"searched $(wc -l) files.\"")
    # $ grabs results \ is an escape character to ignore the "" in this case. also \*
    $(cat demo_file.py)

    #count and print the numbers of files found
    os.system("find " + str(directory) + ' -name' + str(whichFile) + " -print \ echo \"Found $(grep -c/) files that match ")

    print("")
    os.system("find " + str(directory) + ' -name' + str(whichFile))
    print("")


#search for windows 
def windowsSearch():
    whichFile = input("what file are you looking for?")
    directory = input("which directory would you like to search")

    #count Number of files searched reading results of os.system(variable) so we can further process that data (variable)
    searchCount = os.system("dir /a:-d /s /b " + str(directory) + " | find /c \":\\\"").read()

    print("files searched " + searchCount)

    # count number of files found and store as variable 
    foundCount = os.system("dir /b/s " + str(directory) + str(whichFile) + " | find /c \":\\\"").read()
                           
    print("files found " + foundCount)


    #main

linuxSearch()