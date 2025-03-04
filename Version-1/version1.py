import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

# ENCRYPTION
plain_text = input("Enter a message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPTION
cipher_text = input("Enter a message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Encripted message: {cipher_text}")
print(f"original message: {plain_text}")
