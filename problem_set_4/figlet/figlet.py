"""
CS50 - Frank, Ian and Glen’s Letters
Author: Roger Nem
About: Prompts the user for a str of text. Outputs that text in the desired font - FIGlet
"""

import sys
from pyfiglet import Figlet

def main():

    # No font specified
    if len(sys.argv) == 1:
        convert_to_figlet("")

    # Font specified
    elif len(sys.argv) == 3 and ( sys.argv[1] == "-f" or sys.argv[1] == "-font" ):
        convert_to_figlet(sys.argv[2])

    # Wrong arguments passed
    else:
        sys.exit("Invalid usage")

def convert_to_figlet(f):

    usr_input = input('Input: ')

    figlet = Figlet()
    figlet.getFonts()

    if f != '':
        figlet.setFont(font = f) # // Set the figlet font

    # // Print the rendered text
    print(figlet.renderText(usr_input))


main()