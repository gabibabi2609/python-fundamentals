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
#         print("Those don't look like foxes")

print("\nNow I have held all of the bats")

for i in range(2, 11 , 2):
    print("Even number:", i)
