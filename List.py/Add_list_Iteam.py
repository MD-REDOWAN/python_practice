#To add an item to the end of the list, use the append() method:
# append Iteam

list1= [1, 2, 3, 4, 5]
list1.append(6)  # Append 6 to the end of the list
print(list1)  # Output: [1, 2, 3, 4, 5, 6]


# Append Ieam for strings

list2 = ["apple", "banana", "cherry"]
list2.append("jackfruit")  # Append jackfruit to the end of the list
print(list2)  # Output: ['apple', 'banana', 'cherry', 'jackfruit']


# Append Iteam for mixed data types
list3 = [1, "apple", 3.14, True] 
list3.append("banana")  # Append "banana" to the end of the list
print(list3)  # Output: [1, 'apple', 3.14, True, 'banana']


# Insert Iteams

list4 = ["apple", "pinapple", "cherry"]
list4.insert(1, "banana") # Insert banana at 2 second position (index 1)
print(list4) # Output: ['apple', 'banana', 'pinapple', 'cherry']



# Add Multiple Iteams

list5 = [1, 2, 3, 4]
fruits = ["apple", "banana", "cherry", "orange"]
list5.extend(fruits)  # Add multiple items from fruits list to list5
print(list5)  # Output: [1, 2, 3, 4, 'apple', 'banana', 'cherry' 'orange]

