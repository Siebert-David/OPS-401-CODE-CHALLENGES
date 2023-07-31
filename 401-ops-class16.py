#!/usr/bin/python3

# Script Name:                 401-ops-class16.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     01AUG2023
#PArt 1 of 3 


def iterator(): 
  # ask for filepath to the wordlist to utilize
  filepath = input("Enter the Complete Filepath for the Wordlist: ")

  #open the wordlist file
  file = open(filepath, 'r')

  #reads the first line of the wordlist and puts the variable called line
  line = file.readline()

  
  # while loop for password list
  while line:
  
  print(line)
  
  
