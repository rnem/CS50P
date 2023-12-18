"""
CS50 - Nutrition Facts
Author: Roger Nem
About: Prompts to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits
"""

usr_input = input("Fruit: ").lower()

# Dictionary of fruits and their calories
fruits = {
    "apple":"130",
    "avocado":"50",
    "banana":"110",
    "cantaloupe":"50",
    "grapefruit":"60",
    "grapes":"90",
    "honeydewmelon":"50",
    "kiwifruit":"90",
    "lemon":"15",
    "lime":"20",
    "nectarine":"60",
    "orange":"80",
    "peach":"60",
    "pear":"100",
    "pineapple":"50",
    "plums":"70",
    "strawberries":"50",
    "sweet cherries":"100",
    "tangerine":"50",
    "watermelon":"80"
}

if usr_input in fruits:
    print(f"Calories: {fruits[usr_input]}")