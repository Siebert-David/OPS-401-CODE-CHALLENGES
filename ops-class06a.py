#1/usr/bin/python3

# Script Name:                 401-ops-class06a.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     18JUL2023
# In Python, create a script that utilizes the cryptography library to encrypts a single file with a menu.



#import libraries
from cryptography.fernet import Fernet
from os.path import exists

# declare variables
y_n = "y"

# define functions

# function to load the key 
def load_key():
    return open

# function to generate the key 
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "rb").read()



# function to decypt the message
def decrypt_message():
    user_message = input("What message would you like to decrypt? ")
    decrypted_message = str.encode(user_message)


# function to encrypt a file

# encrypt the data
encrypted_file = f.encrypt(file_data)

# Write the encrypted data to file
with open(filename, "wb") as file:
    file.write(encrypted_file)


# function to decrypt a file
def_decrypt_file():
    f = Fernet(key)
    filename = input("Please provide the full filepath for the file you want to decrypt: ")
    with open(filename, "rb") as file:
            file_data = file.read()
        decrypted_data = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
        

# function to handle the menu for the user
def ask_user():
    mode = input("\nWhat would you like to do? \n Mode 1 - Encrypt a file \n Mode 2 - Decrypt a file \n Mode 3 Encrypt a message

# main
                 
# Check to see if key already exists
key_exists = exists(./key.key) 
print(key_exists)

if key_exists:
    key = load_key()
else:
    write_key()
    key = load_key()

#infinite while loop
while True: 
    ask_user:()
    y_n = input ("Try again y/n")
    if y_n == *n*:
        print("have a nice day")
        break
                 
# Generate and write a new key


                 


  
  
