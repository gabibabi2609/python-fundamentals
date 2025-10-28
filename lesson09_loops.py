# LOOPS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.
print()
print("--- Loops in Python ---")

# The for-loop.
# A for-loop repeats for each element in a sequence (like a list or string).

import time

# bats = ["Microbat", "Fruit bat", "Marshmallow bat", "Little brown bat", "Flying fox"]
# print("\nOur bats: ", bats)
# print("\n--- For Loop: holding each bat ---")

# for bat in bats:
#     print("Now holding a", bat)
#     time.sleep(1.5)

#     if bat == "Flying fox":
#         print("Those don't even look like foxes")

# print("\nNow I have held all of the bats")

print()

# # range(start, stop, step)
# print()
# print("--- range() with start, stop, step ---")

# for num in range(2, 11, 2):
#     print("Even number:", num)
# print("Loop ended. Evens appreciated.")

print("--- Iterating over strings ---\n")

fav_word = "Bingo"
letter_list = []

for letter in fav_word:
    print(letter, end="")
    letter_list.append(letter)
    print(letter_list)

print()


# ---------------------------------------------------------
# WHILE LOOPS
# ---------------------------------------------------------
# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 
import time
count = 0

while count < 5:
    print(f"Looping. We are on loop number {count}.")
    count += 1
    time.sleep(0.5)

print("We have escaped the loop!")

user_input = ""

print()
while user_input != "exit":
    user_input = input("Type 'exit' to escape: ")

count = 60
increment = 1

while count > 0:
    
    count -= increment
    increment += 1
    
    if count < 0:
        break

    

    print(count)


#Challenges

#Challenge 1: 

num_fruits = int(input("How many fruits to pick? "))
fruits = ['apple', 'peach', 'mango', 'strawberry', 'watermelon', 'raspberry', 'banana']

import random
import time

# for fruit in fruits:
#     print("You picked: ", random.choice(fruits))
#     time.sleep(1.5)

for fruit in range(num_fruits):
    print("You picked: ", random.choice(fruits))
    time.sleep(0.5)

