import os
from configparser import ConfigParser
import shutil

location = os.path.dirname(os.path.realpath(__file__))

projfold = input("project floder path:")
openvscode = input("open vscode after making project(True / False):")
appdata = os.getenv("APPDATA")

os.chdir(appdata)
adfold = os.path.join(appdata + "/projectstart") #makes path to make folder in appdata
os.mkdir(adfold)
os.chdir(adfold)

config = ConfigParser()
config["data1"] = {
    "project folder": projfold,
    "open vscode": openvscode,
    "appdata": appdata

}
with open('config.ini', 'w') as conf:
    config.write(conf)


#make file to write project name
f0 = open("projname.txt", "w+")
f0.close()
#make bat file for command line funcionality
f = open("create.bat", "w+")
f.write("@echo off \n")
f.write("set name=%1 \n")
f.write(f"cd {adfold} \n")
f.write("ECHO %name% >> projname.txt \n")
f.write("python main.py")
f.close()
#making 2 paths for moving
print("making")
frompath = os.path.join(adfold + "\create.bat")
topath = os.path.join(adfold, "batscripts")
os.mkdir(topath)
scriptfrom = os.path.join(location, "main.py")

os.environ["PATH"] += os.pathsep + topath

print("moving")
shutil.copy(frompath, topath)
shutil.copy(scriptfrom, adfold)
print("setup complete!")
os.system("PAUSE")