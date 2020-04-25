import re

# open raw data as file object
f = open(r"zeuslinks.txt", "r")
f1 = f.readlines()

# create empty dictionary to use as game database
psone_classics = {}
# x = 0

# process raw data to weed out psone classic titles and tidy up data
for i in f1: # loop through raw data line by line
    i = i.strip()[:-1] # strip any trailing characters off the end of each line
    if "US - " in i: # only look for lines with "US - " in the string
        if "PSOne Classics" in i: # then only look for lines with "PSOne Classics" in the string
            if not "pspiso.com" in i: # and then ignore lines with "pspiso.com" (because it is now defunct and links are dead)
                string = i.replace("(", "") # and then remove any left brackets from the string
                string = string.replace(")", "") # and then remove any right brackets from the string
                string = string[5:] # and then slice off the first 4 characters to remove "US - " from the string
                title, url = string.split(" PSOne Classics ") # and then split the string where it says " PSOne Classics " into separate "title" and "url" variables
                title = str(title) # create variable to pass data to string so i don't have to keep typing str(title)
                url = str(url) # create variable to pass data to string so i don't have to keep typing str(url)
                if not "Canadian Store " in url: # exclude canadian store entries
                    serial = re.search(r"\w\w\w\w\d\d\d\d\d", url)  # apply regex pattern to url string to pluck out serial number contained in url
                    serial = str(serial.group(0))[:4] + "-" + str(serial.group(0))[4:] # inject a hyphen into the serial number for properness

                    # raw data is now refined and can be added to dictionary with serial number as key, and title and download link as values
                    # psone_classics.update({"number": x})
                    psone_classics.update({"title": title}) # add each title value found to "title"
                    psone_classics.update({"serial": serial}) # add each serial value found to "serial"
                    psone_classics.update({"url": url}) # add each url value found to "url"

                    # clean dictionary of any duplicates
                    input_dict = psone_classics
                    def remove_duplicates(input_dict):
                        output_dict = {}
                        for key, value in input_dict.items():
                            if value not in output_dict.values():
                                output_dict[key] = value
                        return output_dict

                    # x += 1

                    # # print results on separate lines with linebreak
                    # print(psone_classics['number'])
                    # print(psone_classics['title'])
                    # print(psone_classics['serial'])
                    # print(psone_classics['url'])
                    # print()
