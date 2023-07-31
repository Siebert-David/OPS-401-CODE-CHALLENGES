#!/usr/bin/python3

# Script Name:                 401-ops-class16.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     01AUG2023
# Automated Brute Force Wordlist Attack Tool Part 1 of 3. 

# Define Variables 
import time

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
    line = file.readline() #gets next line- must be in while loop > next line 
  file.close()
  
# add menu


def main():
    # Prompt user to select a mode
    print("Select a mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")
    

    # Get user input for the selected mode
    mode = input("Enter mode (1/2): ")

    if mode not in ["1", "2"]:
        print("Invalid mode selection.")
        return

   

if __name__ == "__main__":
    main()

# references
# MARCO VAZQUEZ - As always an excellent/indepth & informative overview with clear instruction on -why- the while loop & -why- the line = file.readline() must be in that loop
# https://stackoverflow.com/questions/36969248/how-use-line-rstrip-in-python