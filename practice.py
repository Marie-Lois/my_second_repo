"""
This program checks whether someone is eligible to
join the army.
"""

age = int(input("Enter age: "))
height = float(input("Enter Height: "))
weight = float(input("Enter weight: "))

if age >= 18 and height >= 150 and weight >= 50:
    print("Welcome to the Army")
elif age >= 18 or height >= 150 or weight >= 50:
    print("Try again next time")
else:
    print("Your are not qualified")

