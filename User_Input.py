

# That means we are able to ask the user for input.

name = "Redowan"

print("Enter your name:")
print(f"Hey, I am {name}")



# input() using prompt

name = input("Enter your name:")
print(f"Hi My name is {name}")

# Enter your name:Redowan
# Hi My name is Redowan


# Multiple Inputs

name = input("Enter your name: ")
print(f"Name : {name}")
id = input("Enter your id: ")
print(f"ID : {id}")
sec = input("Enter your section: ")
print(f"section : {sec}")

# Output :
""""
Enter your name: Redowan
Name : Redowan
Enter your id: 1310
ID : 1310
Enter your section: D
section : D
"""


# You can convert the input into a number with the float() function:

import math

x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# Output: 
# Enter a number: 25
# The square root of 25 is 5

