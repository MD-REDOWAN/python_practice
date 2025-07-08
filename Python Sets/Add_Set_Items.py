

#Once a set is created, you cannot change its items, but you can add new items.

# Add one iteam to a set using add() method

set1 = {"MD", "Redowan", "Hossain"}
set1.add("Eram")
print(set1)


# Update a set iteam from another set, using update() mehtod

set2 = {"apple", "mango", "cherry"}
set3 = {"banana", "pineapple"}

set2.update(set3)
print(set2)
# Output: {'banana', 'cherry', 'apple', 'mango', 'pineapple'}


# The update() method can be useany iterable object (tuple, Lists,dictionaries etc)

set4 = ["apple", "mango", "banana"]
set5 = {"cherry", 1, 2}

set5.update(set4)
print(set5)
# Output : {1, 2, 'apple', 'mango', 'cherry', 'banana'}