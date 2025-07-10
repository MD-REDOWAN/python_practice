

# We can use for loop in dictionary

person1 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}
for x in person1:
    print(x)
# same thing: print(person1[x])

# Output:
# keys: 
# name
# age
# country"""



# We can also use the values()method to return of a dictionary

person2 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}

for x in person2.values():
    print(x)
# Output: vlaues:
# Redowan
# 23
# Bangladesh



# We can use the keys() method to show the keys of dictionary

person3 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}

for x in person3.keys():
    print(x)

# Output: show the keys name



# for loop using the items() method

person4 = {
    "name" : "Redowan",
    "age" : 23,
    "country" : "Bangladesh"
}

for x, y in person4.items():
    print(x, y)

# Output:

# name Redowan
# age 23
# country Bangladesh

