

# Join Sets
"""There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""


# Using Union() method for join sets

set1 = {1, 2, 3}
set2 = {"apple", "banana", "mango"}

x = set1.union(set2)
print(x)


# Output: {1, 2, 3, 'mango', 'banana', 'apple'}


# join set and tuple using union()

a = {1, 2, 3}
b = ("apple", "banana","mango")

x = a.union(b)
print(x)


# Using the | operator for join multiple sets

set3 = {1, 2, 3}
set4 = {"MD", "Redowan","Hossain"}
set5 = {"apple", "banana", "mango"}

join = set3|set4|set5

print(join)

#Output: {1, 2, 3, 'mango', 'MD', 'Hossain', 'Redowan', 'apple', 'banana'}


# Update() method changes the original set, and does not retuen a new set

set6 = {1, 2, 3}
set7 = {"a", "b", "c"}

set6.update(set7)
print(set6)

# Output: {'b', 1, 2, 3, 'a', 'c'}


# The intersection() method using for find common item multiple sets

set8 = {"MD", "Redowan","Hossain"}
set9 = {"MD", "apple", "banana"}

x = set8.intersection(set9)
print(x)
# Output: 'MD'

# intersection_update() use for keep duplicate vales

set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "mango"}

set1.intersection_update(set2)
print(set1)



# we can also use & operator for find out the common iteam in the multiple set

set10 = {"MD", "Redowan","Hossain"}
set11 = {"MD", "banana", "cherry"}

x = set10 & set11
print(x)
# Output: 'MD'


# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
# The values True and 1 are considered the same value. The same goes for False and 0.

set13 = {"apple", 1,  "banana", 0, "cherry"}
set14 = {False, "mango", 1, "apple", 2, True}

x = set13.intersection(set14)

print(x)
# Output: {False, True, 'apple'}




