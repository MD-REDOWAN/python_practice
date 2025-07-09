

# Change Values in dictinary

person = {
    "country" : "Bnagladesh",
    "name" : "Redowan",
    "age" : 23,
}

person["age"] = 24

print(person)



# We can also use update() mehod for change Dictionary

person2 = {
    "name" : "Akib",
    "age" : 24,
    "country" : "Bangladesh"
}

person2.update({"country" : "England"})

print(person2)

# output : {'name': 'Akib', 'age': 24, 'country': 'England'}


