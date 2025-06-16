# for loop use in list

list1 = ["apple", "banana", "cherry"]
for x in list1 :
    print(x) # Output: apple, banana, cherry (each on a new line)

# Also print like [print(x) for x in thislist]


# Using for loop with range to access list items by index

list2 = ["apple", "banana", "cherry"]
for i in range(len(list2)):
    print(list2[i])  # Output: apple, banana, cherry (each on a new line)


# Using for loop with enumerate to get both index and item
list3 = ["apple", "banana", "cherry"]
for index, x in enumerate(list3):
    print(f"Index {index}: {x}")  # Output: Index 0: apple, Index 1: banana, Index 2: cherry (each on a new line)


# Using While loop 

list4 = ["apple", "banana", "cherry"]
i=0
while i < len(list4): # Check if i is less than the length of the list
    print(list4[i]) 
    i = i + 1  # Output: apple, banana, cherry (each on a new line)





