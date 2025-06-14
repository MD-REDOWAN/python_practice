
"""""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

# List: is a collection which is ordered and changeable. Allows duplicate members.
# Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
# Set: is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary: is a collection which is ordered** and changeable. No duplicate members.
"""

# List : Lists are used for multiple iteam in a single variable.

X = ["bannana, apple, orange, mango, pineapple"]
print(X)

# List is a collection which is ordered and changeable. Allows duplicate members.
Y = ["bannana", "apple", "orange", "mango", "pineapple"]
print(Y)


# Allow duplicate values:

a = ["apple", "banana", "cherry", "banana", "apple"]
print(a)


# List Length:

a = ["apple", "banana", "cherry", "banana", "apple"]
print(len(a))  # Output: 5


# List Items - Data Types:
# List items can be of any data type, including strings, integers, booleans, and even other lists.

list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 7, 9, 3]
list3 = [True, False, False]
list4 = ["apple", 1, True, 3.14, [1, 2, 3]]
print(list1)
print(list2)
print(list3)
print(list4)


# List type():

print(type(list1))  # Output: <class 'list'>
print(type(list2))  # Output: <class 'list'>


# List Constructor:

Z = list(("banana", "apple", "cherry")) #note the dpuble round brackets
print(Z)  # Output: ['banana', 'apple', 'cherry']