import re
import urllib.request
import os

source = "https://raw.githubusercontent.com/libretro/libretro-database/master/metadat/no-intro/Sony%20-%20PlayStation%20Portable%20(PSN).dat"
database = urllib.request.urlopen(source)

for line in database:
    decoded_line = line.decode("latin-1") # text is in byte format and needs to be decoded
    print(decoded_line)









# os.chdir(r"C:\Users\Matt\PycharmProjects\psp-downloader\processed")

# psn_serial = []
#
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)
#     psn_serial.append(f_name)
#     print(f_name)