#!/usr/bin/python3

# Script Name:                 401-ops-class31a.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     22AUG2023
# Part 1 of 3



#import libraries
import os, time
import platform 

#define variables

#define functions 

#search for linux
def linuxSearch():
    whichFile = input("what file are you looking for?")
    directory = input("which directory would you like to search")

    #count and print the number of files searched
    os.system("ls " + str(directory) + " | echo \"searched $(wc -l) files.\"")

#search for windows 



#main