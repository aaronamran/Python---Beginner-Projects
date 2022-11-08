# Author: Aaron Amran
# Creation Date: 01st November 2022
# Project: Simple program for determining if year input from users is a leap year

print("\nWelcome, this program is for you to determine if a year of your choice is a leap year or not.")

# important code section for validating user input
while True:
    user_year = input("Please input a year of your choice: ")
    try:
        user_year = int(user_year)
    except:
        print('\nPlease only use numerical digits.')
        continue
    if user_year < 1:
        print('\nPlease enter a positive number.')
        continue
    break

# first case must have both conditions fulfilled
# divisible by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (user_year % 400 == 0) and (user_year % 100 == 0):
    print("\n", user_year, " is a leap year")

# second case must also have both conditions fulfilled
# not divisible by 100 means not a century year
# user_year divided by 4 is a leap year
elif (user_year % 4 ==0) and (user_year % 100 != 0):
    print("\n", user_year, " is a leap year")

# if not divided by both 400 (century year) and 4 (not century year)
# anything else that does not fulfill both cases above is not a leap year
else:
    print("\n", user_year, " is not a leap year")