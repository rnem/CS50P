"""
CS50 - Home Federal Savings Bank
Author: Roger Nem
About: Prompts the user for a greeting.
       If the greeting starts with “hello”, output $0.
       If the greeting starts with an “h” (but not “hello”), output $20.
       Otherwise, output $100.
       Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""

# Use lower function to treat the user’s greeting case-insensitively
# strip() to Ignore any leading whitespace
gretting = input("Greeting: ").lower().strip()

if gretting.startswith("hello"):
    print("$0")
elif gretting.startswith("h") and gretting != "hello":
    print("$20")
else:
    print("$100")
