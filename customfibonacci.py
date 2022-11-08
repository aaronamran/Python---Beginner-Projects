# Author: Aaron Amran
# Creation Date: 01st November 2022
# Project: Custom Fibonacci sequence generator based on user-defined size

print("\nWelcome to the customisable Fibonacci sequence generator.")
print("The rules are: Number range has to be a positive number, while 1st and 2nd numbers can be positive or negative.")

# important code section for validating user input
while True:
    user_range = input("Please input a range of your choice: ")
    try:
        user_range = int(user_range)
    except:
        print('\nPlease only use numerical digits.')
        continue
    if user_range < 1:
        print('\nPlease enter a positive number.')
        continue
    break

# function to calculate and output sequence based on user-defined first and second number
def fibonacci():

    while True:
        first_number = input("\nPlease input the first number of your choice: ")
        try:
            first_number = int(first_number)
        except:
            print('\nPlease only use numerical digits.')
            continue
        break

    while True:
        second_number = input("\nPlease input the second number of your choice: ")
        try:
            second_number = int(second_number)
        except:
            print('\nPlease only use numerical digits.')
            continue
        break

    print(first_number)

    for i in range(user_range - 1):
        print(second_number)
        first_number, second_number = second_number, first_number + second_number

fibonacci()