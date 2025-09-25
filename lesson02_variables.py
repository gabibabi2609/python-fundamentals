#CONCEPTS VARIABLES
#Variable: holds a value in physical storage

shrimps = "radioactive"
password = "unkn0wn_ent1ty"
email = "il0vec4ts4321"

print("Password:", password)
print("Email:", email)
print("Walmart shrimps are", shrimps)

temperature = 72.5
print(type(temperature))
price = 3.99

enabled = False
is_complete = False
print(is_complete)

#variables are overwrite-able

enabled = True
print(enabled) 
#after changing enabled to true, it overrode the original code saying it was false

#variable names must be meaningful

#for math problems:

x = 3.141592653589793238462643383279502
y = 7
print(x + y)

#variables are flexible, you can create or update another variable like so:
count = 10
print(count)
count_down = count - 1
print(count_down)
count = count_down
print(count)
count_down = count - 1
print(count_down)
count = count_down
print(count)

#CHALLENGES:
#first challenge

name = "Radia Perlman"
age = 34
occupation = "Networking Engineer"

#second challenge

count = 10
count_up = count + 5
count = count_up
print(count)

#third challenge
x = 4
y = "hello"

temp = y
y = x
x = temp
print("y = ", y)
print("x = ", x)

#fourth challenge
is_raining = False
is_raining = True
print("is it raining?", is_raining)