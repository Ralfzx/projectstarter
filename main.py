import os
from configparser import ConfigParser

appdata = os.getenv('APPDATA')
pathtoappdata = os.path.join(appdata, "projectstart")
os.chdir(pathtoappdata)

config = ConfigParser()
config.read("config.ini")
data1 = config["data1"]
projectdir = format(data1["project folder"])
data1 = config["data1"]
openvscode = format(data1["open vscode"])

f = open("projname.txt", "r+")
folder_name = f.read()
f.truncate(0)
f.close()


print(projectdir)
print(folder_name)
finalres = os.path.join(projectdir, folder_name.strip())
print(finalres)
os.mkdir(finalres)

if openvscode == True or "true":
    os.system(f"cd {finalres}")
    os.system("code .")
