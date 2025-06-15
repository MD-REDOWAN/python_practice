# Access Item in List
# The first item has index 0;
a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(a[1])  # Output: banana 
print(a[3])  # Output: orange
print(a[-1])  # Output: mango (last item)
print(a[-3])  # Output: orange (third last item)


# Access Range of Items

b = ["apple", "bannana", "cherry", "orange", "kiwi", "mango"]
# The search will start at index 2 (included) and end at index 5 (not included).

print(b[2:5])  # Output: ['cherry', 'orange', 'kiwi'] (items from index 2 to 4)
print(b[:4])  # Output: ['apple', 'bannana', 'cherry', 'orange'. 'mango'] (items from start to index 3)


# Range of Negative indexes
print(b[-3:-1])  # Output: ['orange', 'kiwi'] (items from third last to second last)


# Check if Item Exists in List

C = ["apple", "bannana", "cherry", "orange"]
if "bannana" in C:
    print("Yes, bannana is in the fruits list")
