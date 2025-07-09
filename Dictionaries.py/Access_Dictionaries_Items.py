

# We can access the items of a dictonary by it's key name, inside square brackets

dic1 = {
    "name": "Redowan",
    "Age": 23,
    "Country": "Bangladesh"
}
print(dic1["Age"])

# Output: 23



# We also access using get() method 

dic2 = {
    "name" : "Redowan",
    "Age" : 23,
    "Country" : "Bangladesh"
    }

print(dic2.get("Age"))


# The key() method will return a list of all the keys in thr dictionary

dic3 = {
    "Name" : "Redowan",
    "Age" : 23,
    "Country" : "Bangladesh" 
}

x = dic3.keys() # This method view the all keys
print(x)

# Output: dict_keys(['Name', 'Age', 'Country'])



# add a new keys in variable dictionary

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




# values() method using for show all values withput keys

dic4 = {
    "Name" : "Redowan",
    "Age" : 23,
    "Country" : "Bangladesh" 
}

print(dic4.values())

# Output: dict_values(['Redowan', 23, 'Bangladesh'])



#*** The items() method help us to see  keys with values


dic5 = {
    "name" : "Redowan",
    "age" : 23,
    "gender" : "Male"
}

print(dic5.items()) 

# Output: dict_items([('name', 'Redowan'), ('age', 23), ('gender', 'Male')])



# Check any key are exist in variable by using (in) keyword

dic6 = {
    "name" : "Redowan",
    "age" : 23,
    "gender" : "Male"
}

if "age" in dic6 :
    print("Yes , 'age' exist in dic6 variable or dictionary")



