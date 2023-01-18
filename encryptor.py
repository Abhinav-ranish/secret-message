from cryptography.fernet import Fernet as fnet
import os as os
import pygame as game

game.mixer.init()
game.mixer.music.load('bis.wav')
game.mixer.music.play(999)


os.system("color 0E")
os.system("cls")
print("Thank you for using AbhiQ Encryptor")
x = input("Do You Have A Key? (yes - y and no - n)\n")
if x == "y":
    key = input("Enter Your Key Here \n").encode()
    print("This is Your Key : "+ (key.decode()))
else:
    key = fnet.generate_key() 
    print("Please Keep this Key Safely.\n")
    print("-------------------------------------------")
    print((key.decode()))
    print("-------------------------------------------\n")
encryptedkey = fnet(key)

os.system("color 0B")
while True:
    cryptography = input("Do You Want to Encode Or Decode The Message? \n(Encode = e, Decode = d, quit = q) \n")
    if cryptography == "e":
        gg = input("Enter the text you want to encode. \n")
        encoded_text = gg.encode()#https://stackoverflow.com/a/69043349/14836433
        token = encryptedkey.encrypt(encoded_text)
        print("This is Your Encrypted Message. \n"+(token.decode()))
        ghost = input("\n Press Enter To Continue")
        os.system("cls")
    elif cryptography == "d":
        text1 = input("Enter the encrypted text to decode. \n").encode()
        token = encryptedkey.decrypt(text1)
        print("This was your secret message \n"+(token.decode)())
        ghost = input("\n Press Enter To Continue")
        os.system("cls")
    elif cryptography in ("q", "exit", "quit"):
        os.system("color 0F")
        os.system("cls")
        input("Task Terminated. \n")
        break



