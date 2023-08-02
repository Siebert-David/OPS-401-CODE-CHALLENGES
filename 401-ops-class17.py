#!/usr/bin/python3

# Script Name:                 401-ops-class17.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     02AUG2023
# Automated Brute Force Wordlist Attack Tool Part 2 of 3. 




# need to finish these below **************
#  password list to reference rockyou-shortened
#  menu for function 


# Import Libraries
import time 
from getpass import getpass


#Declare functions 

#funtion to iterate over word list file 
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
    #word = line #line variable - into word
    print(word)
    print(line)
    time.sleep(1)

# Move to next line in password list
    line = file.readline() #gets next line- must be in while loop > next line 
  file.close()


# funtion to check passwords againt the word list 
def check_password():
    user_password = getpass("Enter your password to verify: ")
    user_wordlist = input("please enter the complete filepath to the wordlist: ")

    print(f"checking password again the words in '{user_wordlist}' please wait")

    file = open(user_worldlist, 'r')  
    line = file.readline()
    wordlist = []  #[] multiple values 

    #while loop
    while line:
       line =line.rstrip()
       worldlist.append(line)     # append TY MARCO adds to wordlist variable 
       line = file.readline()
    file.close()

# checking password against wordlist 
    if user_password not in wordlist:
       print('Password is accepted')
       strenth = True
    elif user_password in worlist:
       print('Password is too Average')
       strength = False

       while strenth is False:
          new_password = getpass("input a stronger password: ")
          if new_password is in wordlist:
             print("Your password is too common")
          elif new_password not in wordlist:
             print("Password not acceptable ")
             strenth = True    #breaks out of this reset password loop

# add menu ( finish the menu *********)
def user_menu():
    while True:
       mode = input("""
Brute FORCE Worldlist Attack Tool Menu
1 - Offensive Dictionary Iterator
2 - Defensive Password Recognised
3 - Exit
    Please enter a number:
"""
                    )



#    Prompt user to select a mode
#      print("Select a mode:")
#      print("1. Offensive; Dictionary Iterator")
#      print("2. Defensive; Password Recognized")    

   

    if mode not in ["1", "2"]:
        print("Invalid mode selection.")
        return

   


    #main
iterator()
check_password

# references
# MARCO VAZQUEZ - As always an excellent/indepth & informative overview with clear instruction on -why- the while loop & -why- the line = file.readline() must be in that loop
# rstrip https://stackoverflow.com/questions/36969248/how-use-line-rstrip-in-python
# readline https://www.w3schools.com/python/ref_file_readline.asp
# append https://www.w3schools.com/python/ref_list_append.asp
