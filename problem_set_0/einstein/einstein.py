"""
CS50 - Einstein
Author: Roger Nem
About: Prompts for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer
"""
def main():
    # Prompts the user for input
    usr_input = int(input("m: "))

    # Use the formula function
    end_result = einstein(usr_input)

    # Print the result(s)
    print(end_result)

def einstein(mass):

    c = 300000000
    E = mass * ( c ** 2 )

    # Print the Energy
    return E

main()