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
result_5 = result_4

