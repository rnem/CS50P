"""
CS50 - Playback Speed
Author: Roger Nem
About: prompts the user for input and then outputs that same input, replacing each space with ...
"""

# Prompts the user for input
usr_input = input("What do you want to say? ")

# docs.python.org/3/library/functions.html#input
# docs.python.org/3/library/stdtypes.html#string-methods
print(usr_input.replace(" ","..."))