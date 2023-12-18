"""
CS50 - Coke Machine
Author: Roger Nem
About:  Prompts to insert a coin, one at a time, each time informing the user of the amount due.
        Once the user has inputted at least 50 cents, output how many cents in change the user is owed
"""

print("Amount Due: 50")

def main():

    due = 50

    while due > 0:
        coin = int(input("Insert Coin: "))

        if coin in [5,10,25]:
            due -= coin

            if due > 0:
                print(str(f'Amount Due: {due}'))
            elif due < 0:
                print(str(f'Change Owed: {abs(due)}'))
                break
            else:
                print(str(f'Change Owed: 0'))
                break

        else:
            due = 50
            print(str(f'Amount Due: {due}'))

main()