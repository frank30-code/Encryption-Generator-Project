# Version 3: RSA Encryption

## Overview
This version replaces the substitution cipher with RSA encryption, a widely adopted public-key encryption standard. The script generates and uses RSA keys to encrypt and decrypt messages securely.

## Key Features
- **RSA Encryption:** Utilizes RSA for secure public-key encryption.
- **Key Generation and Storage:** Generates RSA key pairs and saves them in `.pem` files for reuse.
- **Secure Padding:** Implements OAEP padding with SHA-256 hashing for robust security.

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
