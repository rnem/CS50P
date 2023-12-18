"""
CS50 - Tip Calculator
Author: CS50 / Roger Nem
About: Calculates the tip based on the desired percentage and total amount
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Replace the dollar sign with nothing
    clean_d = d.replace("$","")
    return float(clean_d)


def percent_to_float(p):
    # Replace the percent sign
    clean_p = p.replace("%","")
    convert_p = float(clean_p) / 100
    return convert_p


main()