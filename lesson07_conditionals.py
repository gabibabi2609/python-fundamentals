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


#using 'or' and 'not'
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


