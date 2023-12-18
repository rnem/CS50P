"""
CS50 - Making Faces
Author: Roger Nem
About:
- Function called convert that accepts a str as input and returns that same input with any :) / :( converted to 🙂 / 🙁
- Function called main that prompts the user for input, calls convert on that input, and prints the result
"""

def main():
    # Prompts the user for input
    usr_input = input("Please say something: ")

    # Use the convert function
    end_result = convert(usr_input)

    # Print the result(s)
    print(end_result)

def convert(input_msg):
    # 1 - Replace :) with happy emoji
    init_str = input_msg.replace(":)","🙂")

    # 2 - Replace :( with sad emoji
    final_str = init_str.replace(":(","🙁")

    # Print the str
    return final_str

main()