# Remove list Items

list1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list1.remove("apple")
print(list1)


# Remove Item by Index
list2 = ["apple", "banana", "orange", "orange", "kiwi"]
list2.pop(2)
list2.pop(3) # Index 3 now kiwi, Because pop(2) remove 1st orange & 2nd orange is now at index 2
print(list2)


# Remove Last Item
list3 = ["apple", "banana", "cherry", "orange", "kiwi"]
list3.pop() # Remove the last item (kiwi)
print(list3)  # Output: ['apple', 'banana', 'cherry', 'orange']

# del keyword can also delete iteams by index

list4 = ["apple", "banana", "cherry", "orange", "kiwi"]
del list4[1]  # Delete the item at index 1 (banana)
print(list4)  # Output: ['apple', 'cherry', 'orange', 'kiwi']


# del keyword also delete the list completely

list5 = ["apple", "banana", "cherry", "orange", "kiwi"]
del list5  # Delete the entire list
# print(list5)  # This will raise an error because list5 no longer exists


# del keyword can also delete a range of items

list6 = ["apple", "banana", "cherry", "orange", "kiwi"]
del list6[1:3]  # Delete items from index 1 to 2 (banana and cherry)
print(list6)  # Output: ['apple', 'orange', 'kiwi']


# Clear() method to remove all itams from a list

list7 = ["apple", "banana", "cherry", "orange", "kiwi"]
list7.clear()  # Remove all items from the list
print(list7)  # Output: [] (an empty list)

