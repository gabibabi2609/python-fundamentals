#python libraries are repositories of code that you can use in your own files

# MATH LIBRARY

import math
print("\n--- Math Library ---\n")

print("Square root: ", math.sqrt(25))
print("Round up to an integer: ", math.ceil(4.2))
print("Round down to an integer: ", math.floor(4.8))
print("Power: ", math.pow(2, 5))
print("Pi: ", math.pi)

# RANDOM LIBRARY

#Pseudorandom Number Generator (PRNG) - random enough (Pseudo: Fake)
#True Random Generator - truly random and there is no way to guess what it will generate

print("\n--- Random Library ---\n")

seed = 36822
result_1 = seed + 34263
print(result_1)
result_2 = result_1 -  seed
print(result_2)
result_3 = result_2 ** 2
print(result_3)
result_4 = result_3 / result_1
print(result_4)
result_5 = result_4 - 4169
print(result_5)
print(math.floor(result_5))

print("\n--- ANSWER ---\n")

import math 

# seed = 80583
# step1 = seed / 6.7
# step2 = step1 - 800
# step3 = step2 + 180843
# print(step3)
# result = math.floor(step3)
# print(result)
# limitednumber = step3 - result
# answer = math.floor(limitednumber * 10)

# print(answer)

seed = 12.4444
step1 = seed / 6.7
step2 = step1 - 800
step3 = step2 + 180843
step4 = step3 % 10
result = math.floor(step4)
print(result)
#stuff from class ^^^^^

print("\n--- Random Stuff ---\n" )

import random

#methods:
print("Random integer: ", random.randint(1, 7))
print("Random float between 0 and 1: ", random.random())
my_favs = ["cat", "fox", "whale", "queen victoria"]
print(random.choice(my_favs))  
print(random.choice(my_favs))

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

radius = 3.14 * 7 ** 2

