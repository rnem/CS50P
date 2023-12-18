"""
CS50 - Outdated
Author: Roger Nem
About: Prompts for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

      Then output that same date in YYYY-MM-DD format.
      If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        # Get user input
        date = input('Date: ').strip()

        try:
            # Assuming mm/dd/yyyy is provided
            mnth,day,year = date.split('/')

            mnth = int(mnth)
            day = int(day)
            year = int(year)

            if (int (mnth) > 0 and int(mnth) < 13) and (int(day) > 0 and int(day) < 32):
                if year >= 1000 and year <= 9999:
                    print (year, f'{mnth:02}',f'{day:02}', sep='-')
                    break
        except:

            # if a diff format is provided
            try:
                # Confirm the date has a comma
                if "," in date:

                    # We split the spaces
                    mnth,day,year = date.split(' ')

                    # We replace the comma in the day
                    day = day.replace(',','')
                    day = int(day)
                    year = int(year)

                    if mnth in months and (int(day) > 0 and int(day) < 32):
                        if year >= 1000 and year <= 9999:
                            mnth= (months.index (mnth)+1)
                            print (year, f'{mnth:02}',f'{day:02}', sep = '-')
                            break

            except:
                pass

main()