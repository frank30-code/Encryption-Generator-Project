# Version 1: Substitution Cipher

## Overview
This script uses a basic substitution cipher, where each character in the plaintext is replaced with a corresponding character from a shuffled key. Both encryption and decryption processes rely on the random and string libraries to generate the key and handle character transformations.

## Key Features
- **Basic Encryption/Decryption:** A straightforward implementation of a substitution cipher.
- **Randomized Key Generation:** A new key is generated every time the script runs, ensuring unique encryption for each session.

## Usage

**Encryption:** 

The script prompts the user to enter a plaintext message.

Each character in the plaintext is replaced with a corresponding character from the shuffled key.

The encrypted message (ciphertext) is printed.

**Decryption:** 

The script prompts the user to enter an encrypted message (ciphertext).

Each character in the ciphertext is replaced with the corresponding character from the original character set.

The decrypted message (plaintext) is printed.

## How to Use
1. **Run the Script:**
   ```bash
   python version1.py
   
2. **Enter a Message to Encrypt:**

The script will prompt you to input a message. It will then display the encrypted version of the message.

3. **Enter a Message to Decrypt:**

You can enter the previously encrypted message to see the original message.

**Example**

Input: Hello, World!  
Encrypted: %X1o*,&Jk/z8

**Learnings**

This version helped me understand the fundamentals of cryptography and how to use Python's random and string modules to manipulate data.
