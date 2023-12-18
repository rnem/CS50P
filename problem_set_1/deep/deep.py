"""
CS50 - Deep Thought
Author: Roger Nem
About: Prompts for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two
"""

# Use lower function to make it case-insensitive
question = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()

# strip() to remove any leading, and trailing whitespaces
cleanned_question = question.strip()

match cleanned_question:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")