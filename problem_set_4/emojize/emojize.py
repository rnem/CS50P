"""
CS50 - Emojize
Author: Roger Nem
About: Prompts for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji
"""

import emoji as e

def main():
    usr_input = input('Input: ')
    convert_to_emoji(usr_input)

def convert_to_emoji(emoji):
    # Convert user's input to emoji
    emoji = e.emojize(emoji,language='en')

    # Print the “emojized” version of the user's input
    print("Output: " + emoji)

main()