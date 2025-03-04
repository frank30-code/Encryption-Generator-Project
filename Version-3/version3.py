from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# Step 1: Generate or Load RSA Keys
def generate_keys():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate public key
    public_key = private_key.public_key()

    # Save the keys to files
    with open("private_key.pem", "wb") as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open("public_key.pem", "wb") as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    return private_key, public_key


def load_keys():
    try:
        # Load private key
        with open("private_key.pem", "rb") as private_file:
            private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None,
            )

        # Load public key
        with open("public_key.pem", "rb") as public_file:
            public_key = serialization.load_pem_public_key(public_file.read())

        return private_key, public_key

    except FileNotFoundError:
        print("Key files not found. Generating new keys...")
        return generate_keys()


# Step 2: Encrypt Message with Public Key
def encrypt_message(message, public_key):
    cipher_text = public_key.encrypt(
        message.encode(),  # Convert the message to bytes
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return cipher_text


# Step 3: Decrypt Message with Private Key
def decrypt_message(cipher_text, private_key):
    plain_text = private_key.decrypt(
        cipher_text,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return plain_text.decode()  # Convert bytes back to a string


# Step 4: Input Validation
def validate_input(message):
    # Allow all characters by default (no restrictions)
    return True  # Since RSA handles Unicode, there's no need to limit input


# Main Program
if __name__ == "__main__":
    # Load or generate keys
    private_key, public_key = load_keys()

    # Encrypt a message
    while True:
        plain_text = input("Enter a message to encrypt: ")
        if validate_input(plain_text):
            cipher_text = encrypt_message(plain_text, public_key)
            print(f"Encrypted message: {cipher_text}")
            break
        else:
            print("Invalid input. Please try again.")

    # Ask the user if they want to decrypt the message
    while True:
        decrypt_option = input("Do you want to decrypt the message? (y/n): ").lower()
        if decrypt_option == "y":
            decrypted_message = decrypt_message(cipher_text, private_key)
            print(f"Decrypted message: {decrypted_message}")
            break
        elif decrypt_option == "n":
            print("Decryption skipped.")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
