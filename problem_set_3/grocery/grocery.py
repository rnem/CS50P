"""
CS50 - Grocery List
Author: Roger Nem
About: Prompts for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
       Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item.
"""

grocery_list = {}

while True:
    try:
        # Prompts user
        item = input().lower()

        # If the item has already been typed, added it up
        if item in grocery_list:
            grocery_list[item] += 1
        # if not, add 1
        else:
            grocery_list[item] = 1

    except EOFError:
        # primpt the sorted results of the list
        print("\n")
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key.upper())
        break