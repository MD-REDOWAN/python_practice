

# Remove an item in a set, using remove() or discard() method

set1 = {"apple", "banana", "mango"}
set1.remove("apple")

print(set1)


# Using discard() method

set2 = {"apple", "banana", "mango"}
set2.discard("apple")

print(set1)



# Random iteam remove using pop() method

set3 = {"apple", "banana", "mango"}
set3.pop()

print(set3)


# If we want to see the remove item and also available iteams

set4 = {"apple", "banana", "mango"}
x = set4.pop()

print(x) # see the remove item : mango
print(set4) # available items: {'apple', 'banana'}

# Output: 
# mango
# {'apple', 'banana'}



# For empty the set

set5 = {"apple", "banana", "mango"}
set5.clear()

print(set5)


# The del keyword delete the set completely

set6 = {"apple", "banana", "mango"}

del set6
print(set6)

# Output: error [completely delete]