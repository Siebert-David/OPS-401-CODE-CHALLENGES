#1/usr/bin/python3

# Script Name:                 401-ops-class06a.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     19JUL2023
# In Python, create a script that utilizes the cryptography library to encrypts a single file/message/data with a menu option.


#import libraries
from cryptography.fernet import Fernet
from os.path import exists
# or import os/less is more

# declare variables
y_n = "y"

# define all functions

# function to generate the key 
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
      key_file.write(key)
      
# function to load the key 
def load_key():
    return open("key.key", "rb").read()
    
# function to encrypt a message
def encrypt_message():
    user_message = input("What message would you like to encrypt? ")
    encrypted_message = user_message.encode()
    f = Fernet(key)

  
# function to encrypt the message 
    encrypted = f.encrypt(encrypted_message)
    print("your message encrypted: ")
    print(encrypted)
    
# function to decypt the message
def decrypt_message():
    user_message = input("What message would you like to decrypt? ")
    decrypted_message = str.encode(user_message)
#same as previous 
    f = Fernet(key)
    decrypted = f.decrypt(decrypted_message)
    print("Your message decrypted: ")
    print(decrypted)

#function to encrypt a file //, copied/adjusted/added steps from encrypt message- open - read-  put in variable- write data to file
def encrypt_file():
  f = Fernet(key)
  filename = input("Enter Full file path for the file your want to Encrypt: ")
  with open(filename, "rb") as file:
#read the file data
      file_data = file.read()

# encrypt the data
encrypted_file = f.encrypt(file_data)

# Write the encrypted data to file
with open(filename, "wb") as file:
    file.write(encrypted_file)


# function to decrypt a file-same fx as encryption but reverse
def_decrypt_file():
    f = Fernet(key)
    filename = input("Enter Full file-path for the file you want to Decrypt: ")
    with open(filename, "rb") as file:
            file_data = file.read()
        decrypted_data = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        
# Function

# function to create the menu for the user \n = new line  (covered in course by marco) add error messaging for catch all 
def ask_user():
    mode = input("\nWhat would you like to do? \n Mode 1 - Encrypt a file \n Mode 2 - Decrypt a file \n Mode 3 Encrypt a message n\ Mode 4 Decrypt a message n\n Enter a Number to select: ")
  if (mode == "1"):
      encrypt_file():
      print("File has been Encrypted")
  elif (mode == "2"):
      decrypt_file()
      print("File has been Decrypted")
  elif (mode == "3"):
      encrypt_message():
      print("Message has been Encrypted")
  elif (mode == "4"):
      decrypt_message():
      print("Message has been Decrypted")
  else:
      print("chose a valid option")

# Main
                 
# Check to see if key already exists (covered in course by marco)
key_exists = exists(./key.key) 
print(key_exists)

if key_exists:
    key = load_key()
else:
    write_key()
    key = load_key()

#infinite while loop to call ask_user to continue or terminate/break
while True: 
    ask_user:()
    y_n = input ("Try again y/n")
    if y_n == *n*:
        print("Thank you for using my service. Operation ending")
        break
                 


                 


  
  
