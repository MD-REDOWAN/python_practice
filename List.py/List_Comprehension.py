# Looping Using list Comprehension

list1 = ["apple", "banana", "cherry"]
list2 = [x for x in list1]  # Create a new list with the same items
print(list2)  # Output: ['apple', 'banana', 'cherry']


# List Comprehension 

list3 = ["apple", "banana", "cherry"]
newlist = []

for x in list3:
    if "a" in x:
        newlist.append(x) # This will add items that contain "a" to newlist
print(newlist)


# list comprehension same solution in one line
list3 = ["apple", "banana", "cherry"]
newlist = [x for x in list3 if "a" in x]


# The Syntax of list comprehesnsion is:
# newlist = [expression for item in iterable if condition]
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.



# Example of list comprehension with a condition

list4 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in list4 if x != "apple"]

print(newlist)


# With no If Statement

list5 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in list5]

print(newlist)



# Iterable with range()

list6 = [x for x in range(10)]
print(list6)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Iterable with range() and condition

list7 = [x for x in range(10) if x < 5]
print(list7)  # Output: [0, 1, 2, 3, 4]


# Expression

list8 = ["apple", "banana", "cherry, kiwi", "mango"]
NEWLIST = [x.upper()for x in list8]
print(NEWLIST)  # Output: ['APPLE', 'BANANA', 'CHERRY, KIWI', 'MANGO']


list9 = ["apple", "banana", "cherry, kiwi", "mango"]
newlist = [ 'Hello' for x in list9]
print(newlist)  # Output: ['Hello', 'Hello', 'Hello', 'Hello']


# Expression with condition

list10 = ["apple", "banana", "cherry, kiwi", "mango"]
newlist = [x if x != "apple" else "orange" for x in list10]
print(newlist)  # Output: ['orange', 'banana', 'cherry, kiwi', 'mango']


# Nested List Comprehension
list11 = [[x for x in range(3)], [x for x in range(3, 6)]]  
print(list11)  # Output: [[0, 1, 2], [3, 4, 5]]

