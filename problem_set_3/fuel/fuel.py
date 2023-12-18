"""
CS50 - Fuel Gauge
Author: Roger Nem
About: Prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.
       If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
       And if 99% or more remains, output F instead to indicate that the tank is essentially full
"""

def main():
    fuel = get_fuel_in_tank("Fraction: ")
    print(f"{fuel}")

def get_fuel_in_tank(prompt):
    while True:
        try:
            usr_input = input(prompt)

            # make sure we have a division
            if '/' in usr_input:

                numbers = usr_input.split('/')

                x = numbers[0]
                y = numbers[1]

                # If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again
                if type(x) == int or type(y) == int:
                    usr_input = input(prompt)
                elif ( int(x) > int(y) ) and (int(y) != 0):
                    usr_input = input(prompt)
                #elif int(y) == 0:
                #    print('c')
                #    usr_input = input(prompt)
                else:
                    fraction = int(x) / int(y)

                    # 1% or less remains, output E
                    if fraction <= 1/100:
                        return 'E'
                    # if 99% or more remains, output F
                    elif fraction >= 99/100:
                        return 'F'
                    else:
                        fuel = "{0:.0f}%".format(fraction * 100)
                        return fuel

        # Be sure to catch any exceptions like ValueError or ZeroDivisionError.
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()