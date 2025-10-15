# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
print()
print("--- Lists in Python ---")

animals = ["whale", "fox", "cat"]

numbers = [2, 4, 6, 8, 10]
mixed = ["kitty", 43, 3.14, False]

print("Animals:", animals)
print("Numbers:", numbers)
print("Mixed:", mixed)

print()
print()
print()
print("--- Indexing: how to access the elements of a list ---")
print("First element: ", animals[0])
print("Second element: ", animals[1])
print("Last element: ", animals[-1])

print()
print("--- Modifying Lists ---")
animals[0] = "Sea horse"
print("Animals:", animals)


animals.append("Tree frog")

print("Animals: ", animals)

# insert an element at a specifc index

animals.insert(3, "Megachiroptera")
print("Animals:", animals)

animals.remove("Sea horse")
print("Animals:", animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

animals.replace("fox", "tree frog")
print(animals)