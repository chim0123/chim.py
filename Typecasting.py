#Typecasting = the process of converting a variable from one data type to another
#              str (), int(), float(), bool()

name = "Chim"
age = 18
gpa = 3.1
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = str(age)
age += "1"
print(age)