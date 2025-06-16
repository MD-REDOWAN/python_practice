
# Change Item in List

list1 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
list1[1] = 'watermelon'  # Change the second item banana to watermelon
print(list1)  # Output: ['apple', 'watermelon', 'cherry', 'orange', 'kiwi', 'mango']


# Change Range of Items

list2 = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']
list2[2:3] = ['pinapple', 'jackfruit']  # Change the third item cherry to pinapple and jackfruit
print(list2)  # Output: ['apple', 'banana', 'pinapple', 'jackfruit', 'orange', 'kiwi', 'mango']


# Change Range of Items with Different Length

list3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list3[2:5] = ["pinapple", "jackfruit"]  # Change the third item cherry to pinapple and jackfruit
print(list3)


# Insert Itams

list4 = ["apple", "banana", "orange", "Kiwi"]
list4.insert(2, "watermelon")# Insert watermelon at index 2
print(list4)  # Output: ['apple', 'banana', 'watermelon', 'orange', 'Kiwi']

