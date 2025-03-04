import random
import string

chars = string.punctuation + string.ascii_letters + string.digits + " "
chars = list(chars)

try:
    with open("encryption_key.txt", "r") as key_file:
        key = list(key_file.read())
except FileNotFoundError:
    key = chars.copy()
    random.shuffle(key)
    with open("encryption_key.txt", "w") as key_file:
        key_file.write("".join(key))

def validate_input(message, valid_chars):
    for chars in message:
        if chars not in valid_chars:
            return False
    return True

while True:
    plain_text = input("Enter a message to encrypt: ")
    if validate_input(plain_text, chars):
        break
    else:
        print("Invalid characters found. Please enter a valid message.")

cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

while True:
    cipher_text = input("Enter a message to decrypt: ")
    if validate_input(cipher_text, key):
        break
    else:
        print("Invalid characters found. Please enter a valid message.")

plain_text = ""
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Encripted message: {cipher_text}")
print(f"original message: {plain_text}")
