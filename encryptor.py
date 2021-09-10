from cryptography.fernet import Fernet as dpsisbad
import os as pp
import pygame as hotshit
#from playsound import playsound as sexy
#sexy('https://cdn.discordapp.com/attachments/831569914535739393/877087237743996938/y2mate.com_-_Jonas_Brothers_Hesitate_Lyrics.mp3', False)


hotshit.mixer.init()
hotshit.mixer.music.load('bis.wav')
hotshit.mixer.music.play(999)


pp.system("color 0E")
pp.system("cls")
print("Thank you for using AbhiQ Encrytor")
dpsreadschats = input("Do You Have A Key? (yes - y and no - n)\n")
if dpsreadschats == "y":
    key = input("Enter Your Key Here \n").encode()
    print("This is Your Key : "+ (key.decode()))
else:
    key = dpsisbad.generate_key() 
    print("Please Keep this Key Safely.\n")
    print("-------------------------------------------")
    print((key.decode()))
    print("-------------------------------------------\n")
dpsstalks = dpsisbad(key)

pp.system("color 0B")
while True:
    dpshacksyou = input("Do You Want to Encode Or Decode The Message? \n(Encode = e, Decode = d, quit = q) \n")
    if dpshacksyou == "e":
        gg = input("Enter the text you want to encode. \n")
        encoded_text = gg.encode()#https://stackoverflow.com/a/69043349/14836433
        token = dpsstalks.encrypt(encoded_text)
        print("This is Your Encrypted Message. \n"+(token.decode()))
        ghost = input("\n Press Enter To Continue")
        pp.system("cls")
    elif dpshacksyou == "d":
        text1 = input("Enter the encrypted text to decode. \n").encode()
        token = dpsstalks.decrypt(text1)
        print("This was your secret message \n"+(token.decode)())
        ghost = input("\n Press Enter To Continue")
        pp.system("cls")
    elif dpshacksyou in ("q", "exit", "quit"):
        pp.system("color 0F")
        pp.system("cls")
        ghost = input("Thanks For Using AbhiQ services. \n")
        break



