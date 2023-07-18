#1/usr/bin/python3

# Script Name:                 401-ops-class06.py               
# Class Name:                  Ops 401d8
# Author Name:                 David Siebert 
# Date of latest revision:     18JUL2023
# In Python, In Python, create a script that utilizes the cryptography library to:

#Prompt the user to select a mode:
#Encrypt a file (mode 1)
#Decrypt a file (mode 2)
#Encrypt a message (mode 3)
#Decrypt a message (mode 4)

Of course! Here's the Python script with explanations above each line:

```python
# Encryption of data at rest is a common need in security operations. Today you will begin development
# of a Python script that encrypts a single file.

# Resources
# PyPi: cryptography 3.1.1


from cryptography.fernet import Fernet
import os

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Load the encryption key from a file
def load_key(key_path):
    with open(key_path, "rb") as key_file:
        return key_file.read()

# Save the encryption key to a file
def save_key(key_path, key):
    with open(key_path, "wb") as key_file:
        key_file.write(key)

# Encrypt the contents of a file using the provided encryption key
def encrypt_file(key, file_path):
    cipher_suite = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)

    with open(file_path, "wb") as file:
        file.write(encrypted_data)

# Decrypt the contents of a file using the provided decryption key
def decrypt_file(key, file_path):
    cipher_suite = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()

    decrypted_data = cipher_suite.decrypt(file_data)

    with open(file_path, "wb") as file:
        file.write(decrypted_data)

# Encrypt a string using the provided encryption key
def encrypt_message(key, message):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())

    print("Encrypted Message:")
    print(encrypted_message.decode())

# Decrypt a string using the provided decryption key
def decrypt_message(key, encrypted_message):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message.encode())

    print("Decrypted Message:")
    print(decrypted_message.decode())

def main():
    # Prompt user to select a mode
    print("Select a mode:")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")

    # Get user input for the selected mode
    mode = input("Enter mode (1/2/3/4): ")

    if mode not in ["1", "2", "3", "4"]:
        print("Invalid mode selection.")
        return

    key_path = "encryption_key.key"

    # For mode 1 and 2, prompt user for file path
    if mode in ["1", "2"]:
        file_path = input("Enter the file path: ")
        if not os.path.exists(file_path):
            print("File not found.")
            return

    # For mode 1 and 3, generate a new encryption key and save it to a file
    if mode in ["1", "3"]:
        key = generate_key()
        save_key(key_path, key)
    else:
        # For mode 2 and 4, load encryption key from a file
        if not os.path.exists(key_path):
            print("Encryption key not found. Please encrypt a file or message first.")
            return
        key = load_key(key_path)

    # Perform the selected action based on the mode
    if mode == "1":
        encrypt_file(key, file_path)
        print("File encrypted successfully.")
    elif mode == "2":
        decrypt_file(key, file_path)
        print("File decrypted successfully.")
    elif mode == "3":
        message = input("Enter the cleartext message: ")
        encrypt_message(key, message)
    elif mode == "4":
        encrypted_message = input("Enter the encrypted message: ")
        decrypt_message(key, encrypted_message)

if __name__ == "__main__":
    main()
```

