

# Join Two Lists

list1 = ["apple", "banana", "cherry"]
list2 = ["kiwi", "mango", "orange"]

list3 = list1 + list2  # Using the + operator to join two lists
print(list3)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']



# Another way to join two lists using the append() method

list4 = ["apple", "banana", "cherry"]
list5 = ["kiwi", "mango", "orange"]

for x in list5:
    list4.append(x) # Appending each item from list5 to list4
print(list4)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']



# Using the extend() method to join two lists

list6 = ["apple", "banana", "cherry"]
list7 = ["kiwi", "mango", "orange"]
 
list6.extend(list7)  # Extending list6 with items from list7
print(list6)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']


# join two lists using function

def join_lists(list1, list2):
    return list1 + list2  # Using the + operator to join two lists



    