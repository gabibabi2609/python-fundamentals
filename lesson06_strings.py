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