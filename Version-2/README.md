# Version 2: Simple Substitution Cipher with Persistent Key and Input Validation

## Overview
This script uses a substitution cipher where each character in the plaintext is replaced with a corresponding character from a shuffled key. The key is saved to a file (encryption_key.txt) for reuse in future sessions. The script also includes input validation to ensure only valid characters are encrypted and decrypted.

## Key Features
- **Key Persistence:** The encryption key is saved to a file and reused if available.
- **Input Validation:** Ensures that only supported characters are processed for encryption and decryption.

## Usage  
**Key Management:**

The script attempts to load the encryption key from a file (encryption_key.txt).

If the key file is not found, a new shuffled key is generated, saved to the file, and used for encryption and decryption.

**Encryption:**

Prompts the user to enter a plaintext message.

Validates the input to ensure all characters are part of the valid character set.

Each character in the plaintext is replaced with the corresponding character from the shuffled key.

The encrypted message (ciphertext) is printed.

**Decryption:**

Prompts the user to enter an encrypted message (ciphertext).

Validates the input to ensure all characters are part of the shuffled key.

Each character in the ciphertext is replaced with the corresponding character from the original character set.

The decrypted message (plaintext) is printed.

## How to Use
1. **Run the Script:**
   ```bash
   python version2.py

2. **Enter a Message to Encrypt:**

The script will prompt you to input a message. It will validate the input and display the encrypted version.

3. **Enter a Message to Decrypt:**

Enter the previously encrypted message to see the original message. The script will validate the input before decrypting.

**Example**

Input: Hello, World!  
Encrypted: %X1o*,&Jk/z8

**Learnings**

This version taught me how to handle file I/O in Python and the importance of validating user input to prevent errors.
