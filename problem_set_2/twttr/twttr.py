"""
CS50 - Just setting up my twttr
Author: Roger Nem
About:  Prompts for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase
"""

def main():
    usr_input = input("Input: ")
    print("Output:", removeVowels(usr_input))

def removeVowels(word):

    vowels = 'AEIOUaeiou'

    for ele in vowels:
        word = word.replace(ele,"")
    return word


main()