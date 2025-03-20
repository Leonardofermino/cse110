"""
Author: Leonardo Fermino

Purpose: Create a grade calculator

"""


score = float(input("What score did you receive for the class? "))

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"

sign_score = score % 10
if sign_score >= 7:
    sign = "+"
elif sign_score < 3:
    sign = "-"
else:
    sign = ""

grade = letter + sign

if letter == "A":
    if sign == "+" or score == 100:
        print(f"Grade: {letter}")
    else:
        print(f"Grade: {grade}")

elif letter == "F" and sign != "":
    print(f"Grade: {letter}")

else:
    print(f"Grade: {grade}")

if score >= 70:
    print("You passed this course. Congratulations!")
else:
    print("You failed this course. Work harder next time. That's all the encouragement you are going to get.")