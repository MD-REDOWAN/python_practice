

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.


fruits1= ["Apple", "Banana", "Mango"]
print(fruits1[0])  # Output: Apple



# The Length of an array

fruits2 = ["Apple", "Banana", "Mango"]

len(fruits2)  # Output: 3



# Looping Array Elements

fruits3 = ["Apple", "Banana", "Mango"]

for x in fruits3:
    print(x)

# Output:
# Apple
# Banana
# Mango



# Adding array Elements using append() method

fruits4 = ["Apple", "Banana", "Mango"]

fruits4.append("Cherry")

print(fruits4)  # Output: ['Apple', 'Banana', 'Mango', 'Cherry']



# Removing Array Elements using remove() method

fruits5 = ["Apple", "Banana", "Mango"]
fruits5.remove("Banana")

print(fruits5)  # Output: ['Apple', 'Mango']



# Sorting Arrays using sort() method

fruits6 = ["Banana", "Apple", "Mango"]
fruits6.sort()

print(fruits6)  # Output: ['Apple', 'Banana', 'Mango']


# insert() method which is add element at specific index

fruits7 = ["Apple", "Banana", "Mango"]
fruits7.insert(1, "Cherry")

print(fruits7)  # Output: ['Apple', 'Cherry', 'Banana', 'Mango']



