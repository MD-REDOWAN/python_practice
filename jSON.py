

# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.


# Python has a built-in package called json, which can be used to work with JSON data.

import json

x = '{ "name":"Redowan", "age":"23", "city": "Dhaka"}'

y = json.loads(x)

print(y["age"])

# Output: 23



# Convert from python to json
#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.


import json

x = {

    "name" : "Redowan",
    "age" : 23,
    "city" : "Dhaka"
}

y = json.dumps(x)

print(y)

# Output: {"name": "Redowan", "age": 23, "city": "Dhaka"}



# You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
#string
int
float
True
False
None

# Example
# Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# indent:
# Use the indent parameter to define the numbers of indents:


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

# Output: 
"""
{
    "name": "John",
    "age": 30,
    "married": true,
    "divorced": false,
    "children": [
        "Ann",
        "Billy"
    ],
    "pets": null,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ]
}
"""



# separator:
# Use the separator parameter to change the default separator


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))


# Output:
"""
{
    "name" = "John".
    "age" = 30.
    "married" = true.
    "divorced" = false.
    "children" = [
        "Ann".
        "Billy"
    ].
    "pets" = null.
    "cars" = [
        {
            "model" = "BMW 230".
            "mpg" = 27.5
        }.
        {
            "model" = "Ford Edge".
            "mpg" = 24.1
        }
    ]
}
"""

