# from psone_classics import

import wget
import time
from pywinauto.application import Application
from pywinauto.timings import Timings
import os, shutil, glob
from psone_classics import psone_classics

download_path = r"C:\Users\Matt\PycharmProjects\psp-downloader\psone-classics\temp\\"

# for v in psone_classics.items():
#    print(v)


# # automate external extractor software using pywinauto
# def extract():
#     psp_extractor = r"C:\Users\Matt\PycharmProjects\psp-downloader\extractor\PSNPKGDecryptor&Extractor.exe"
#
#     app = Application(backend="win32").start(psp_extractor)
#     dlg = app.window(title_re="PSN PKG Decryptor & Extractor v1.85")
#     dlg.type_keys(str(download_path + filename))
#     app.window(title_re="PSN PKG Decryptor & Extractor v1.85").window(title="Extract").click()
#     app.window(title_re="Complete").window(title="OK").click()
#     app.window(title_re="PSN PKG Decryptor & Extractor v1.85").close()
#
# def cleaner():
#     # workaround for rigid extractor process. find any iso files inside download paths recursively
#     completed_isos = glob.glob(str(download_path) + '/**/*.iso', recursive=True)
#     dest = r"C:\Users\Matt\PycharmProjects\psp-downloader\processed"
#     # make destination path if it doesn't exist already
#     if not os.path.exists(dest):
#         os.makedirs(dest)
#
#     # move any iso files into destination path
#     print('moving ' + str(filename) + ' to "processed"\n')
#     for f in completed_isos:
#         try:
#             shutil.move(f, dest)
#         except OSError:
#             pass
#
#     # delete working directory
#     time.sleep(2)
#     print("destroying temp directory\n")
#     shutil.rmtree(download_path) # be careful with this!
#
#     time.sleep(0.5)
#     print("\nNEXT!\n")
#
# # main
# print("\n" + str(len(urls)) + " urls found in list\n\n") # print number of items in list
# for i in urls:
#
#     # make temp directory
#     if not os.path.exists(download_path):
#         os.makedirs(download_path)
#
#     filename = i[42:51] + str(".pkg")
#     # print(*urls, sep = "\n\n") # for debugging. print list with line separation
#
#     print('downloading "' + (i) + '"\ninto "' + (download_path)[:-1] + str(filename) + '"\n\n')
#
#     time.sleep(0.5)
#
#     #start downloading urls in list
#     try:
#         # i = urls[1] # for debugging. this is quick to download
#         wget.download(i, download_path + filename)
#         print("\n\n" + str(filename) + " downloaded. opening PSN PKG Decryptor & Extractor for conversion...")
#         extract()
#         cleaner()
#     except OSError:
#         print("link request failed! moving to next link\n")
#         pass
