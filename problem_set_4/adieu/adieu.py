"""
CS50 - Adieu, Adieu
Author: Roger Nem
About: Prompts for names, one per line, until the user inputs control-d
       Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with commas and one and,
"""

import inflect
p = inflect.engine()

list_of_names = []

while True:
    try:
        usr_input = input("Name: ")
        list_of_names.append(usr_input)

    except EOFError:
        print()
        break

output_of_names = p.join(list_of_names)
print("Adieu, adieu, to " + output_of_names)