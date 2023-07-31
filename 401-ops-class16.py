#!/usr/bin/python3

# Script Name:                 401-ops-class16.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     01AUG2023
#Part 1 of 3 

# Define Variables 

# Import Libraries


def iterator(): 
  # ask for filepath to the wordlist to utilize
  filepath = input("Enter the Complete Filepath for the Wordlist: ")

  #open the wordlist file
  file = open(filepath, 'r')

  #reads the first line of the wordlist and puts the variable called line
  line = file.readline()

  
  # while loop for password list
  while line:
    line = line.rstrip() #removes empty spaces
    word = line #line variable - into word
    print(word)
    print(line)
    time.sleep(1)

# Move to next line in password list
    line = file.readline() #ogets next line- must be in wile loop > next line 
  file.close()
  
  
  
#references
#MARCO VAZQUEZ - As always an excellent/indepth & informative overview with clear instruction on -why- the while loop & -why- the line = file.readline() must be in that loop
#