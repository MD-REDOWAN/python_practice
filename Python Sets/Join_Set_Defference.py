
# difference() method will represent the uncommon vales or items in sets

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

x = set1.difference(set2) # diffrence item of set1 
y = set2.difference(set1) # diffrence item of set2

print(x) # {'a', 'b'}
print(y) # {'d', 'e'}



# we can use (-) operator for find out the differnce items

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

x = set1 - set2 # diffrence item of set1 
y = set2 - set1 # diffrence item of set2

print(x) # {'a', 'b'}
print(y) # {'d', 'e'}



# Use the difference_update() method to keep the items that are not present in both sets:

set2 = {"apple", "banana", "cherry"}
set3 = {"google", "microsoft", "apple"}

set2.difference_update(set3)

print(set2)
# {'banana', 'cherry', 'microsoft', 'google'}



# symmetric_diffrence() method Keep the all items that are diffrence in both sets:

set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}

x = set4.symmetric_difference(set5)

print(x)
# Output: {'banana', 'cherry', 'microsoft', 'google'}


# symmetric_diffrence() method and ^ operator are same work

set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}

x = set4 ^ set5

print(x)
# Output: {'banana', 'cherry', 'microsoft', 'google'}

