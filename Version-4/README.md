# Version 4: Advanced File Management & User Interface

## Overview
This version adds advanced features for managing encrypted messages and a menu-driven interface for better usability. Encrypted messages are saved to uniquely labeled files, allowing easy retrieval and decryption.

## Key Features
- **File-Based Message Labeling:** Saves encrypted messages to uniquely labeled files.
- **Interactive Menu:** A user-friendly menu system for encryption, decryption, and program exit options.
- **Label Verification:** Ensures that file labels are unique to prevent accidental overwrites.
- **Message Retrieval:** Allows retrieval and decryption of saved messages by label.

## How to Use
1. **Run the Script:**
   ```bash
   python version4.py

2. **Program Menu:**

Choose from the menu options:

a. Encrypt a new message.

b. Decrypt a saved message by label.

c. Exit the program.

3. **Encrypt a Message:**

Enter a message to encrypt and provide a unique label. The script will save the encrypted message to a file.

4. **Decrypt a Message:**

Enter the label associated with the message to retrieve and decrypt it.

## Example
**Encrypt:**  
Enter a message to encrypt: Hello, World!  
Enter a unique label for your message: Example  
Encrypted message saved to 'encrypted_message_Example_1.txt'.  

**Decrypt:**  
Enter the unique label associated with your message: Example  
Loaded the most recent message: encrypted_message_Example_1.txt  
Decrypted message: Hello, World!

## Learnings
This version taught me about file management, creating interactive user interfaces, and the importance of unique identifiers in data handling.
