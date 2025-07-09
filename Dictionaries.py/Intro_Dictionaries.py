

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.



# Example of Dictionary:

dic1 = {
    "name": "Redowan",
    "age" : 23,
    "gender": "male"
}

print(dic1)

# Output: {'name': 'Redowan', 'age': 23, 'gender': 'male'}



# If we want to print name value of the dictionary

dic2 = {
    "name": "Redowan",
    "age" : 23,
    "gender": "male"
}

print(dic2["name"])

# Output: Redowan



# Duplicate values not allowed

dic3 = {"name" : "Redowan",
        "age" : 23,
        "gender": "male",
        "gender": "male"
        }

print(dic3) # don't show the duble values



# Length fo Dictonary

dic4 = {
    "name": 'Redowan',
    "age" : 23,
    "gender": "male",
    "country" : "Bangladesh"
}

print(len(dic4)) # Output: 3



# Data Type : Dictionary Items

# string , int , boolean, and list data type:

dic5 = {
    "name" : 'Redowan',
    "age"  : 23,
    "Male" : True,
    "Hobby": ["fishing", "playing", "walking"]
    }

print(dic5)



# Type() 'dist'

dic6 = {
    "name" : 'Redowan',
    "age"  : 23,
    "Male" : True,
    "Hobby": ["fishing", "playing", "walking"]
    }

print(type(dic6))
# Ouput: <class 'dict'>



# The dict() Construction

dic7 = dict(name = "Redowan", age = 23, Country = "Bangladesh" )

print(dic7)

# Output: {'name': 'Redowan', 'age': 23, 'Country': 'Bangladesh'}



