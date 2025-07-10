

# We cannot copy a dictionary simply by typing dict2 = dict1; Because: dict2 will only be reference to dict1
#

# there a copy of a dictionary with the copy() method:

person1 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}
x = person1.copy()
print(x)

# Output: {'name': 'Redowan', 'age': 23, 'country': 'Bangladesh'}




# Anther way to make a copy to use dict() function:


person2 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}

mydict = dict(person2)
print(mydict)

# Output: {'name': 'Redowan', 'age': 23, 'country': 'Bangladesh'}


