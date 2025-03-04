# Version 2: Key Persistence & Input Validation

## Overview
Building on the first version, this iteration adds functionality to save and reuse the encryption key across multiple sessions. It also introduces input validation to ensure only valid characters are processed.

## Key Features
- **Key Persistence:** The encryption key is saved to a file and reused if available.
- **Input Validation:** Ensures that only supported characters are processed for encryption and decryption.

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
