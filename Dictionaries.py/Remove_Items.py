

# Remove specific key or item name using pop() method

person1 = {
    "name" : "Redowan",
    "age" : "23",
    "country" : "bangladesh"
}

person1.pop("age")

print(person1)
# Output: {'name': 'Redowan', 'country': 'bangladesh'}



# The popitem() method remove the last iteam

person2 = {
    "name" : "Redowan",
    "age" : "23",
    "country" : "bangladesh"
}

person2.popitem()

print(person2)

# Output: {'name': 'Redowan', 'age': '23'}




# The del keyword removes the specific key name

person3 = {
    "name" : "Redowan",
    "age" : "23",
    "country" : "bangladesh"
}
del person3["age"]
print(person3)

# Output: {'name': 'Redowan', 'country': 'bangladesh'}




# The clear() method work for empty the dictionary

person4 = {
    "name" : "Redowan",
    "age" : "23",
    "country" : "bangladesh"
}
person4.clear()
print(person4)

# Output: {}



