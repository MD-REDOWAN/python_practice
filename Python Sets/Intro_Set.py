
""" IMPORTANT NOTE:
Set Items:
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered:
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable:
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items."""
#  Note: Set items are unchangeable, 
#  but you can remove items and add new items.

"""Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed."""


# The vales of set are change un-ordered / random order / 

set1 = {"MD","Redowan","Hossain"}
print(set1)
# Output: {'Hossain', 'MD', 'Redowan'}


# Do not allow duplicate values.

set2 = {"MD", "MD","Redowan","Hossain"}
print(set2)

# Use set() constructor

a = set(("apple", "Mango", "banana"))
print(a)

# True and 1 is considered the same value:

set3 = {1,2,True,"MD","Redowan","Hossain"}
print(set3)

# Output: {1, 2, 'MD', 'Redowan', 'Hossain'}


# False and 0 is considered the same value:

set4 = {0, 2, True, False,"MD","Redowan","Hossain"}
print(set4)

# Output: 0, True, 2, 'Hossain', 'MD', 'Redowan'}


# len() function uses for determine how many iteams a set

set5 = {"apple","banana","cherry"}
print(len(set5))

# Output: 3


# find type fo set

set6 = {"apple","banana","cherry"}
print(type(set6))

# Output: <class 'set'>