# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

print()
print()
print()
print()

# if
num1 = 10
if num1 == 10: 
    print("Your number is equal to 10")

print()

num2 = 202020
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")
else: 
    print("Your number is greater than 12")


print()
print()

#if elif else

temperature = 92
if temperature > 80:
    print("It's very hot")
elif temperature >= 60:
    print("It's warm")
else:
    print("It's cold")

print()
print()
print("--- Comparing Values with if/elif/else ---")

x = 20
y = 30


if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("error")


print()
print()
print()
# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 

age = 17
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("You can't drive yet")

print()
print()
print()


# Using 'or' and 'not'

day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
elif day == "Monday" or day == "Tuesday":
    print("It's early in the week")
else: 
    print("It's later in the week")

print()

if day is not "Monday":
    print("It's not Monday")

# Challenge 1: Even or Odd
# Ask the user for a number, and tell them if it’s even or odd.
# Example output:
# Enter a number: 7
# 7 is odd.
# Hint: use modulus operator

import math

number = int(input("Give me a number: "))

if number % 2 == 1:
    print(f"{number} is an odd number")
else:
    print(f"{number} is an even number")

# Create a variable with a stored password
# Ask the user to enter a password. 
# If it matches the stored password, print "Access granted." Otherwise, "Access denied."
# Example output:
# Enter password: dolphin
# Access granted. Access denied.
# Enter password: swordfish
# Access granted.

print()

password = "penguinsarecool"

entered_password = input("Enter your password: ")

if password == entered_password:
    print("Access granted")
else:
    print("Access denied")

# Challenge 3: Grading System
# Ask the user for a numeric grade (0-100) and print a letter grade.
# Example output:
# Enter your grade: 94
# You earned an A.

print()

grade = int(input("What grade did you get? "))
if grade >= 90:
    print("You got an A!")
elif grade >= 80: 
    print("You got a B!")
elif grade >= 70: 
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
else:
    print("You got an F... Be better.")