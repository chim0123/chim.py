#Variable = A container for a value (string, integer, float, boolean)
#           A variable behaves as if it was the value it contains

# Strings
first_name = "Bro"
food = "pizza"
print(f"Hello {first_name}")
print(f"You like {food}")

# Integers
age = 25
print(f"You are {age} years old")

# Float
price = 10.99
print(f"The price is ${price}")

# Boolean
is_student = False
print("Are you a student?: {is_student}")
for_sale = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not for available")