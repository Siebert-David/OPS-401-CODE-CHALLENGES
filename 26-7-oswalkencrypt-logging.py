#!/usr/bin/python3

# Script Name:                 401-ops-class26-7-oswalkencrypt-logging.py              
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     14AUG2023
# Event logging tool Part 1 of 3. os walk encrpt single file with logging

import os
import logging
from cryptography.fernet import Fernet
from os.path import exists

# Configure the basic logger, formatting messages, file mode write
logging.basicConfig(filename="demo.log", format='%(asctime)s %(message)s', filemode='w')

# Creating log object
log = logging.getLogger("my_logger")

# Setting the level of message to log
log.setLevel(logging.WARNING)

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

# Generate a set of test log messages
log.debug("Harmless Debug")
log.info("An Information Message")
log.warning("A WARNING")
log.error("AN ERROR")
log.critical("Worst Case Scenario")

def do_things():
    log.debug("doing things")

do_things()

