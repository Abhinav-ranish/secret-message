import tkinter as tk
from cryptography.fernet import Fernet as fnet

def generate_key():
    key = fnet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())
    key_label.config(text="Please Keep this Key Safely.")

def encrypt_message():
    key = key_entry.get().encode()
    encryptedkey = fnet(key)
    message = message_entry.get()
    encoded_text = message.encode()
    token = encryptedkey.encrypt(encoded_text)
    encrypt_label.config(text=token.decode())

def decrypt_message():
    key = key_entry.get().encode()
    encryptedkey = fnet(key)
    message = message_entry.get().encode()
    token = encryptedkey.decrypt(message)
    decrypt_label.config(text=token.decode())

root = tk.Tk()
root.title("AbhiQ Encrytor")

key_label = tk.Label(root, text="Do You Have A Key? (yes - y and no - n)")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

generate_key_button = tk.Button(root, text="Generate Key", command=generate_key)
generate_key_button.pack()

message_label = tk.Label(root, text="Enter the text you want to encrypt or decrypt")
message_label.pack()

message_entry = tk.Entry(root)
message_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.pack()

encrypt_label = tk.Label(root)
encrypt_label.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.pack()

decrypt_label = tk.Label(root)
decrypt_label.pack()

