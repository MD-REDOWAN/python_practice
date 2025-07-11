

# A dictionary  can contain multiple dictionaries

myteam = {

    "player1" : {
        "name" : "Redowan",
        "age" : 23,
        "position" : "Center Forward"
    },

    "player2" : {
        "name" : "Akib",
        "age" : 24,
        "positin" : "Center Mid Field"
    },

    "player3" : {
        "name" : "Abir",
        "age" : 22,
        "position" : "Right Back"
    }
}


for x, y in myteam.items():
 print(x, y)

# Output:
# player1 {'name': 'Redowan', 'age': 23, 'position': 'Center Forward'}
# player2 {'name': 'Akib', 'age': 24, 'positin': 'Center Mid Field'}
# player3 {'name': 'Abir', 'age': 22, 'position': 'Right Back'}



# create three dictionaries and one dictionary will contain the others three dictionaries

player1 = {
   "name" : "Redowan",
   "age" : 23,
   "position" : "Center Forward"
    },

player2 = {
    "name" : "Akib",
    "age" : 24,
    "positin" : "Center Mid Field"
    },

player3 = {
        "name" : "Abir",
        "age" : 22,
        "position" : "Right Back"
    }

myteam ={
 "player1" : player1,
 "player2" : player2,
 "player3" : player3
}

print(myteam.items())


# access items:
myteam = {

    "player1" : {
        "name" : "Redowan",
        "age" : 23,
        "position" : "Center Forward"
    },

    "player2" : {
        "name" : "Akib",
        "age" : 24,
        "positin" : "Center Mid Field"
    },

    "player3" : {
        "name" : "Abir",
        "age" : 22,
        "position" : "Right Back"
    }
}

print(myteam["player2"]["name"])



# You can loop through a dictionary by using the items() method like this:

myteam = {

    "player1" : {
        "name" : "Redowan",
        "age" : 23,
        "position" : "Center Forward"
    },

    "player2" : {
        "name" : "Akib",
        "age" : 24,
        "positin" : "Center Mid Field"
    },

    "player3" : {
        "name" : "Abir",
        "age" : 22,
        "position" : "Right Back"
    }
}

for x, obj in myteam.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])

# Output:
"""
player1
name: Redowan
age: 23
position: Center Forward
player2
name: Akib
age: 24
positin: Center Mid Field
player3
name: Abir
age: 22
position: Right Back
"""