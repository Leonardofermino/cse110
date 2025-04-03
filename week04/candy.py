"""
Author: Leonardo Fermino

Purpose: test while syntax

"""

candy = ''

while candy != 'yes':
    candy = input("May I have a piece of candy? ").strip().lower()

print("Thank you")