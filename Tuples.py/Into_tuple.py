#  Tuple are used to store multiple iteams in single variable

"""Ordered:
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable:
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

"""

# Example of creating tuples in python

tuple1 = ("MD", "Redowan", "Hossain")

tuple2 = ('MD', 'Redowan', 'Hossain')

tuple3 = (1, 2, 3 , 4, 5)

print(tuple1)

print(tuple2)

print(tuple3)



# Allow Duplicates:

tuple4 = ("apple", "apple", "banana")
print(tuple4)

# Tuple Length:

tuple5 = ("apple","cherry", "banana", "pineapple")
print(len(tuple5))  # Output: 4



# Create a tuple with one item
tuple6 = (type("apple"),)  # Note the comma
tuple7 = (type("apple"))  # This is not a tuple, it's just a string
print(tuple6)  # Output: ('apple',)
print(tuple7)  # Output: apple (not a tuple)


# Tuple Iteams - Data Types
tuple8 = ("apple", "banana", "cherry")
tuple9 = (1, 2, 3, 4, 5)
tuple10 = (True, False, True)
tuple11 = (2, "apple", True) # Mixed data types in a tuple
print(tuple8)  # Output: ('apple', 'banana', 'cherry')
print(tuple9)  # Output: (1, 2, 3, 4, 5)    
print(tuple10)  # Output: (True, False, True)
print(tuple11)  # Output: (2, 'apple', True)



# Tuple  Constructor

tuple12 = tuple(("apple", "banana", "cherry"))  # Using the tuple() constructor
print(tuple12)  # Output: ('apple', 'banana', 'cherry')









