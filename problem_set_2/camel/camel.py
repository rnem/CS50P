"""
CS50 - camelCase
Author: Roger Nem
About: Prompts for the name of a variable in camel case and outputs the corresponding name in snake case.
"""

usr_input = input("camelCase: ")

print("snake_case: ", end="")

for letter in usr_input:

    # check to see if letter is upper case
    if letter.isupper():
        print("_" + letter.lower(), end="")

    # if letter is not upper case
    else:
        print(letter, end="")

# print space at the end
print()