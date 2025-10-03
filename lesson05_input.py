# USER INPUT IN PYTHON

print("\n--- User Input Demonstration ---\n")

name = input("Enter your name: ")
print("Hello", name)
print("\n")

age = input("Enter your age: ")
# print(type(age))
print("\n")

age_number = int(age)
print("Next year you'll be ", age_number + 1 )
# print(type(age))
print("\n")
#example with float input

height = float(input("Enter your height in feet "))
print("You are", height, "feet tall")
print("\n")
#Challenge 1: favorite color
# Ask the user for their favorite color and print out a message using it

fav_color = input("What is your favorite color? ")
print(fav_color, "is a nice color")
print("\n")
# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

number1 = int(input("Pick one number "))
print("\n")
number2 = int(input("Now pick another one "))
sum = number1 + number2
print("if you add them, they equal ", sum)
print("\n")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.

import math
radius = int(input("Gimme a radius of a circle please "))
area1 = math.pi * radius ** 2
real_area = math.floor(area1)
print("The area is ", real_area)
print("\n")

# Challenge: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random

sides = int(input("How many sides should this die have? "))
die_roll = random.randint (1, sides)
print("The dice says", die_roll)

