import hashlib
import os
import json
import subprocess
import urllib3
import requests

os.system("clear")
print("""
İnstagram : codewithluka
web : https://lukacoder.com/
 /$$      /$$       /$$ /$$$$$$$        /$$      /$$                                 /$$                        
| $$$    /$$$      | $$| $$____/       | $$$    /$$$                                | $$                        
| $$$$  /$$$$  /$$$$$$$| $$            | $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$| $$$$$$$       | $$ $$/$$ $$ /$$__  $$| $$__  $$ /$$_____/|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$| $$| $$  | $$|_____  $$      | $$  $$$| $$| $$  \ $$| $$  \ $$|  $$$$$$   | $$    | $$$$$$$$| $$  \__/
| $$\  $ | $$| $$  | $$ /$$  \ $$      | $$\  $ | $$| $$  | $$| $$  | $$ \____  $$  | $$ /$$| $$_____/| $$      
| $$ \/  | $$|  $$$$$$$|  $$$$$$/      | $$ \/  | $$|  $$$$$$/| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$      
|__/     |__/ \_______/ \______/       |__/     |__/ \______/ |__/  |__/|_______/    \___/   \_______/|__/      

1- MD5 OLUŞTUR
2- MD5 BRUTE FORCE 
3- MD5 CRACK
""")
veri = input("Islem Numarasini Girin : ")
if veri == "1":
    user = input("YAZIYI GİR :  ")
    h = hashlib.md5(user.encode())
    h2 = h.hexdigest()
    print(h2)

if veri == "2":

    wlist = input("wordlist: ")
    hash2crack = input("hash: ")
    wlistlines = open(wlist, "r").readlines()

    for i in range(0, len(wlistlines)):

        hash2comp = hashlib.md5(wlistlines[i].replace(
            "\n", "").encode()).hexdigest()

        if hash2crack == hash2comp:
            print("Cracklendi: " + wlistlines[i].replace("\n", ""))
            exit()
            print("Cracklenemedi....")
if veri == "3":
    dat2 = input("Kırılacak MD5 Hash ==> ")
    print("")
    print("_______________________________")
    print("")
    response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
    print("crack sonucu => ", response)
    print("")
    print("cracklenen hash => ", dat2)
    print("")
    print("_______________________________")