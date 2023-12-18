"""
CS50 - File Extensions
Author: Roger Nem
About: Prompts for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default
"""

# Use lower function to treat the name of a file case-insensitive
name_of_file = input("File name: ").lower()

if ".gif" in name_of_file:
    print("image/gif")
elif ".jpg" in name_of_file:
    print("image/jpeg")
elif ".jpeg" in name_of_file:
    print("image/jpeg")
elif ".png" in name_of_file:
    print("image/png")
elif ".pdf" in name_of_file:
    print("application/pdf")
elif ".txt" in name_of_file:
    print("text/plain")
elif ".zip" in name_of_file:
    print("application/zip")
else:
    print("application/octet-stream")