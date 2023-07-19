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

# To decrypt, comment out the previous line and uncomment the following line
# decrypt_folder(folder_path, key)
