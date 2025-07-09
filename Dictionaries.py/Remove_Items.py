

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


