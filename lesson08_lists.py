# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.
print()
print("--- Lists in Python ---")

animals = ["whale", "fox", "Cat"]

numbers = [2, 4, 6, 8, 10]
mixed = ["kitty", 43, 3.14, False]

empty_list = []
empty_list.append("Microbat")
print("Empty list:", empty_list)

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

animal_replace = animals.index("fox")
print(animal_replace)
animals[animal_replace] = "Microbat"
print("Animals:", animals)


print()
print("--- Useful List Functions ---")
print()

nums = [4, 10, 5, 8, 3, 9, 2, 6, 1, 7]
print("Original numbers:", nums)

print("Length of the list:", len(nums))
print("Minimum:", min(nums))
print("Maximum:", max(nums))
print("Sum:", sum(nums))

nums.sort()
print("Sorted:", nums)
animals.sort()
print("Animals sorted:", animals)

nums.reverse()
print("Numbers reversed:", nums)

if "cat" in animals:
    print("I like cat")
else:
    print("Where is cat")

new_list = [4, 5, 6]
copied_list = new_list.copy()
copied_list.append(7)
print(new_list)
print(copied_list)

print()
print("--- Nested Lists/The Matrix ---")

matrix = [ 
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
    ]

print(matrix[0][2])
print(matrix[2][2])

### **Challenge 1: Integer Swap**

# Store this list in a variable: [ 1, 2, 3, 4, 5, 6 ] 
# Ask the user to enter a new integer.
# Replace the **third integer** in the original list with the user’s input, and then print the updated list.
# *Hint: use indexing and assignment.*

integers = [ 1, 2, 3, 4, 5, 6 ]
new_num = int(input("Gimme a number "))
integers[2] = new_num
print("New list: ", integers)


### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position and remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append("Flour, baking powder, cocoa powder")
shopping.insert(1, "milk")
print(shopping)


