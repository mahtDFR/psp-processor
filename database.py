import re
# f = open(r"Sony - PlayStation Portable (PSN).dat.txt", "r")
f = open(r"zeuslinks.txt", "r")
f1 = f.readlines()

# find psone classic titles in data and clean up data to generate tidy list
for i in f1: # loop through data line by line
    i = i.strip()[:-1] # strip any trailing characters off the end of each line
    if "US - " in i: # only look for lines with "US - " in the string
        if "PSOne Classics" in i: # then only look for lines with "PSOne Classics" in the string
                if not "pspiso.com" in i: # ignore lines with "pspiso.com" (because it is now defunct)
                    string = i.replace("(", "") # remove any left brackets from the string
                    string = string.replace(")", "") # remove any right brackets from the string
                    string = string[5:] # slice off the first 4 characters to remove "US - " from the string
                    string = string.split(" PSOne Classics ") # split the string where it says " PSOne Classics " to separate the title fron the link
                    string = str(string) # create variable to pass to string so i don't have to keep typing str(var)
                    serial = re.search(r"\w\w\w\w\d\d\d\d\d", string)  # apply regex pattern to string to find psx serial number
                    serial = str(serial.group(0))[:4] + "-" + str(serial.group(0))[4:] # add a hyphen into the serial number for properness

                    print(serial + " " + string)




                    # database = dict(string.split(" PSOne Classics ") for x in string.split(','))
                    # print(psone_classics_database)



# print(len(database))



# # find name amd put in a list
# names = []
# for name_line in f1:
#     if "name" in name_line:
#         if not "rom" in name_line:
#             # print(name_line[7:-2])
#             names.append(name_line[7:-2])
#
# # find serials and put in a list
# serials = []
# for serial_line in f1:
#     if "serial" in serial_line:
#         if not "rom" in serial_line:
#             # print(serial_line[9:19])
#             serials.append(serial_line[9:19])
#
# names.pop(0)
# #
# # for i in names:
# #     print(i)
# #
# # for i in serials:
# #     print(i)
# #
# res = dict(zip(serials, names))
#
# for s,n in res.items():
#     print(s , n)

