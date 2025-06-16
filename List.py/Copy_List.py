
# Make a copy of a list using the copy() method

list1 = ["apple", "banana", "cherry"]
mylist = [list1.copy()]
print(mylist)  # Output: [['apple', 'banana', 'cherry']]


# Make a copy of a list using the list() constructor

list2 = ["apple", "banana", "cherry"]
mylist = list(list2)
print(mylist)  # Output: ['apple', 'banana', 'cherry']


# Make a copy of a list using : operator

list3 = ["apple", "banana", "cherry"]
mylist = list3[:]
print(mylist)  # Output: ['apple', 'banana', 'cherry']
