import random, string
import webbrowser
import time
import requests
import os
import base64


os.system("cls")
os.system(
    "TITLE Fortnite Codes Generator / By Lzyen")


print(base64.b64decode('Q29kZSBCeSBKdW5haS4=').decode())

num = input('How Many Codes to Generate: ')

f=open("Fortnite Codes.txt","w", encoding='utf-8')

print("Wait, Generating!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(21))
   f.write("https://www.epicgames.com/fortnite/ajax/redemption/validate-redemption-code?redeem-code=")
   f.write(y)
   f.write("\n")

f.close()

#=============Checker=========================


with open("Fortnite Codes.txt") as f:
    for line in f:
        fortnite = line.strip("\n")
        url = fortnite
        r = requests.get(url)

        if r.status_code == 304:
            print(" Valid | {} ".format(line.strip("\n")))
            break
        else:
        	print(" Invalid | {} ".format(line.strip("\n")))
a = input("The end! Press Enter")

if a == "":
    exit()