# Basic string creation and indexes:
greeting = "Hello"
name = "Ada"
print(greeting, name)

# 0 1 2 3 4
# H E L L O

# 0 1 2
# A D A

print(greeting[1])

second_letter = greeting[1]
print(second_letter)

message = greeting + " " + name + "!!!!"
print("Concatenated message: ", message)

print()

word = "Supercalifragilisticexpialidocious"
print("First letter: ", word[0])
print("Last letter: ", word[-1])
print("Range of letters (non-inclusive):", word[4:-23])
print("First five letters: ", word[:5])
print("Last seven letters: ", word[-7:])
print("Step through every second character: ", word[::2])
print("Reversed: ", word[::-1])
print("Reversed, stepping every third letter", word[::-3])


#Built in functions

country = "Brazil"
length_of_word = len(country)
print(length_of_word)

phrase = "pEnguIN"
print("\nUppercase:", phrase.upper())
print("\nLowercase:", phrase.lower())
print("\nCapitalize:", phrase.capitalize())
print("\nTitle Format:", phrase.title())

print()

#Find and Replace text
sentence = "Penguins like to trade pebbles"
new_sentence = sentence.replace("like", "love")
print("First sentence: ", sentence)
print("New sentence:", new_sentence)

#Formatted strings

print("\n--- Formatted Strings ---\n")


name = "Billy"
age = 6
city = "Boston"

print(f"Hello, my name is {name}. I am {age} and live in {city}")

#f strings can do math and function calls inside {}

print(f"Next year, I'll be {age + 1}. My name in upper case is {name.upper()}")

#CHALLENGE TIMEEEEE