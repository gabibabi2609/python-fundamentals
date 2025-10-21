#Challenge 1- palindrome checker
palindrome = input("Enter a word")
print(palindrome == palindrome[::-1])

#Challenge 2 - 
email = input("Enter your email: ")
#Yeah i have no idea :P

#Challenge 3
bats = ["Microbat", "Marshmallow bat", "Fruit bat"]
last = input("name a type of bat: ")
print(bats[-1] == last )

#Challenge 4
word = input("Enter a verb: ")
if len(word) >= 3 and word[-3 : 1] != "gni":
    print(f"New word: {word}ing")
elif word[-3:1] == "gni":
    print(f"New word: {word}ly")
else:
    print(word)
