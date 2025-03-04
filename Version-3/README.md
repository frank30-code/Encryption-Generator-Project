# Version 3: RSA Encryption

## Overview
This script demonstrates basic RSA encryption and decryption using the cryptography library. RSA is an asymmetric encryption algorithm that uses a pair of keys: a public key for encryption and a private key for decryption.

## Key Features
- **RSA Encryption:** Utilizes RSA for secure public-key encryption.
- **Key Generation and Storage:** Generates RSA key pairs and saves them in `.pem` files for reuse.
- **Secure Padding:** Implements OAEP padding with SHA-256 hashing for robust security.

## Usage
**Key Generation:**

Generates an RSA key pair (public and private keys).

Saves the keys to files (private_key.pem and public_key.pem).

**Encryption:**

Prompts the user to enter a plaintext message.

Encrypts the message using the public key.

Prints the encrypted message (ciphertext).

**Decryption:**

Prompts the user to specify if they want to decrypt the message.

Decrypts the message using the private key.

Prints the decrypted message (plaintext).

## How to Use
1. **Run the Script:**
   ```bash
   python version3.py

2. **Encrypt a Message:**

Enter a message to encrypt using the public key. The script will display the encrypted message.

3. **Decrypt a Message:**

Optionally decrypt the message using the private key to see the original message.

**Example**

Input: Hello, World!  
Encrypted: b'\x9d\x1a\xfc\xe0...'  
Decrypted: Hello, World!

**Learnings**

Implementing RSA encryption deepened my understanding of public-key cryptography and the use of secure hashing algorithms.
