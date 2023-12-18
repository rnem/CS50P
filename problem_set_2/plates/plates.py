"""
CS50 - Vanity Plates
Author: CS50 / Roger Nem
About: Prompts for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):

        # middle of the plate minus one due to array
        m = int(len(s) / 2) - 1

        # Numbers cannot be used in the middle of a plate; they must come at the end
        if s[m].isalpha() == False:
            return False

        # in case of numbers
        if s[i].isalpha() == False:

            # The first number used cannot be a ‘0’.
            if s[i] == '0':
                return False
            else:
                break

        i += 1

    # No periods, spaces, or punctuation marks are allowed
    for c in s:
        if c in ['.',' ','!','?']:
            return False

    # If all tests above are ok then return true
    return True


main()