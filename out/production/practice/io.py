import math

"""name=input("enter  your name:")
print("your name:",name)
age=int(input("enter  your age:"))
print("your age:",age)

# this function will always give you a string
number=input("enter  your number:")
as_integer=int(number)
print(as_integer)
as_float=float(number)
print(as_float)"""


print("I hate: ", end="")
print("line breaks")

pi = 3.141
print(f" the value of pi is {pi}")


pi=math.pi
print(f" the value of pi is {pi}")

print(f"{pi:.0f}")
print(f"{pi:.2f}")
print(f"{pi:.3e}")

ratio=.25
print(f"{ratio:.2%}")

#Reading and Writing Files
# Basic open (don't forget to close!)

file = open('example.txt', 'r')
content = file.read()
file.close()
print(content)
# Better way: Using 'with' statement (auto-closes)

with open ('example.txt','r') as file:
    content=file.read()
    print(content)


# Creating a New File:
# Method 1: Using 'w' mode (creates if doesn't exist)

with open('newfile.txt','w')as file:
    file.write("I  created new file")

# Method 2: Using 'x' mode (fails if file exists)
try:
    with open('newfiles.txt','w') as file:
        file.write("This only creates if file doesn't exist")
except FileExistsError:
    print("file already exists")



with open('log.md','a') as file:
    file.write("This is readme file")
