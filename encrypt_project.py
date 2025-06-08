from cryptography.fernet import Fernet
import os

# Generate and save key
def generate_key(key_file='secret.key'):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as f:
        f.write(key)
    print(f"[+] Key saved to {key_file}")

# Load existing key
def load_key(key_file='secret.key'):
    if not os.path.exists(key_file):
        print("[-] Key file not found. Generate a key first.")
        return None
    with open(key_file, 'rb') as f:
        return f.read()

# Encrypt file
def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path + ".enc", 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    print(f"[+] File encrypted as: {file_path}.enc")

# Decrypt file
def decrypt_file(encrypted_path, key):
    fernet = Fernet(key)
    with open(encrypted_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    decrypted_path = encrypted_path.replace(".enc", ".dec")
    with open(decrypted_path, 'wb') as dec_file:
        dec_file.write(decrypted)
    print(f"[+] File decrypted as: {decrypted_path}")

# Main Menu
def main():
    print("=== File Encryption/Decryption Tool ===")
    while True:
        print("\n1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            key = load_key()
            if key:
                file_path = input("Enter file path to encrypt: ")
                if os.path.exists(file_path):
                    encrypt_file(file_path, key)
                else:
                    print("[-] File not found.")
        elif choice == '3':
            key = load_key()
            if key:
                encrypted_path = input("Enter encrypted file path: ")
                if os.path.exists(encrypted_path):
                    decrypt_file(encrypted_path, key)
                else:
                    print("[-] File not found.")
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
