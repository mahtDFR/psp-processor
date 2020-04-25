# dump list of folder contents to .txt file

import os

path = r"C:\Users\Matt\PycharmProjects\psp-downloader\processed"
file = "processed_list.txt"
list = os.listdir(path)

with open(file, "w") as f:
    f.write("'" + path +"'\n")
    f.write(str(len(list)) + " files \n\n")
    for i in os.listdir(path):
        f.write(str(i) + "\n")
print("list of files in '" + path + "' dumped to '" + file + "'")