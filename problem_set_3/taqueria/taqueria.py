"""
CS50 - Felipe’s Taqueria
Author: Roger Nem
About: Enables a user to place an order, prompting them for items, one per line, until the user inputs control-d
"""

# Menu provided
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        # Prompt user for menu item
        item = input("Item: ").lower()

        # Loop throught the menu
        for i in menu:

            # if type item is in the menu add it to total
            if item == i.lower():
                total += menu[i]
                print(f"Total: ${total:.2f}")

            # if not, keep prompting the user for valid entry
            else:
                pass

    except EOFError:
        print()
        break