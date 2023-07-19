#1/usr/bin/python3

# Script Name:                 401-ops-class07.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     19JUL2023
# In Python create a script that utilizes OS.WALK to crawl the tree hierarchy. Recursively encrypt a single folder and all its contents. Recursively decrypt a single folder that was encrypted by this tool.

#root: Prints out directories only from what you specified
#dirs: Prints out sub-directories from root
#files: Prints out all files from root and directories

import os
from cryptography.fernet import Fernet
from os.path import exists

# Function to generate the key
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a message
def encrypt_message():
    user_message = input("What message would you like to Encrypt? ")
    encrypted_message = user_message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encrypted_message)
    print("Your message encrypted: ")
    print(encrypted)

# Function to decrypt a message
def decrypt_message():
    user_message = input("What message would you like to Decrypt? ")
    decrypted_message = str.encode(user_message)
    f = Fernet(key)
    decrypted = f.decrypt(decrypted_message)
    print("Your message Decrypted: ")
    print(decrypted)

# Function to encrypt a file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_file)

# Function to decrypt a file
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    decrypted_file = f.decrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_file)

# Function to recursively encrypt a folder and its contents
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Function to recursively decrypt a folder and its contents
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path, topdown=True):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Main
key_exists = exists("key.key")

if key_exists:
    key = load_key()
else:
    write_key()
    key = load_key()

folder_path = input("Enter the path of the folder to encrypt/decrypt: ")
encrypt_folder(folder_path, key)

#add function/menu option to decrypt: reference previous line
# decrypt_folder(folder_path, key)

#references:
#Course CFops401d8 covered by marco in class
#https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/
#https://appdividend.com/2020/01/20/python-list-of-files-in-directory-and-subdirectories/
#https://github.com/Siebert-David/OPS-401-CODE-CHALLENGES/blob/main/401-ops-class07prepOS.walk.py
#open.ai.com (how to stage/combine the encyrpt/decrypt with OS.walk)
