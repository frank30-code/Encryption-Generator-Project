from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os


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


# Step 4: Ensure the Label is Unique
def ensure_unique_label(label):
    while any(f.startswith(f"encrypted_message_{label}_") for f in os.listdir()):
        print(f"The label '{label}' already exists. Please choose a different label.")
        label = input("Enter a new unique label for your message: ").strip()
    return label


# Step 5: Save Encrypted Message to a Unique File with Verified Unique Label
def save_encrypted_message(cipher_text):
    user_label = input("Enter a unique label for your message (e.g., your name): ").strip()
    if not user_label:
        print("Invalid label. Using 'anonymous' as default.")
        user_label = "anonymous"

    # Ensure the label is unique
    user_label = ensure_unique_label(user_label)

    # Generate a unique filename
    counter = len([f for f in os.listdir() if f.startswith(f"encrypted_message_{user_label}_")]) + 1
    filename = f"encrypted_message_{user_label}_{counter}.txt"
    with open(filename, "wb") as file:
        file.write(cipher_text)
    print(f"Encrypted message saved to '{filename}'.")


# Step 6: Load the Most Recent Encrypted Message for a Given Label
def load_encrypted_message_by_label(label):
    # Find all files matching the given label
    matching_files = sorted(
        [f for f in os.listdir() if f.startswith(f"encrypted_message_{label}_")],
        reverse=True
    )
    if not matching_files:
        print(f"No messages found for the label '{label}'. Please ensure the label is correct.")
        return None

    # Load the most recent file for the given label
    latest_file = matching_files[0]
    with open(latest_file, "rb") as file:
        print(f"Loaded the most recent message: {latest_file}")
        return file.read()


# Main Program
if __name__ == "__main__":
    # Load or generate keys
    private_key, public_key = load_keys()

    # Program Menu
    while True:
        print("\nChoose an action:")
        print("1. Encrypt a new message")
        print("2. Decrypt a saved message by label")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            # Encrypt a new message
            plain_text = input("Enter a message to encrypt: ")
            cipher_text = encrypt_message(plain_text, public_key)
            save_encrypted_message(cipher_text)

        elif choice == "2":
            # Decrypt a message by label
            user_label = input("Enter the unique label associated with your message: ").strip()
            cipher_text = load_encrypted_message_by_label(user_label)
            if cipher_text:
                try:
                    decrypted_message = decrypt_message(cipher_text, private_key)
                    print(f"Decrypted message: {decrypted_message}")
                except Exception as e:
                    print(f"Decryption failed: {e}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")
