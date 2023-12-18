"""
CS50 - Meal Time
Author: Roger Nem
About: Prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.
       If it’s not time for a meal, don’t output anything at all.
"""

def main():
    # Get the time from the usere
    usr_input = input("What time is it? ")

    # Call function
    time = convert(usr_input)

    # breakfast 7:00 - 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")

    # lunch 12:00 - 13:00
    if time >= 12 and time <= 13:
        print("lunch time")

    # dinner 18:00 - 19:00
    if time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    # split the hours and minutes
    hours, minutes = time.split(":")

    # convert to float
    new_min = float(minutes) / 60

    # return results to main
    return float(hours) + new_min

if __name__ == "__main__":
    main()