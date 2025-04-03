"""
Author: Leonardo Fermino

Purpose: test loop examples

"""

number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry this is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print(f"The number is: {number}")