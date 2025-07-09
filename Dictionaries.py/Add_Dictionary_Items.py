

# Adding Items in dictinary

person = {
    "country" : "Bnagladesh",
    "name" : "Redowan",
    "age" : 23,
}

x = person.keys() # view all keys
print(x)

person["gender"] = "Male" # add new key

print(x) # print all keys with new key; dict_keys(['country', 'name', 'age', 'gender'])

print(person)  # Output: {'country': 'Bnagladesh', 'name': 'Redowan', 'age': 23, 'gender': 'Male'}



# using update() method add items

person2 = {
    "name" : "Akib",
    "age" : 24,
    "country" : "Bangladesh"
}

person2.update({"country" : "England"})

print(person2)

# output : {'name': 'Akib', 'age': 24, 'country': 'England'}