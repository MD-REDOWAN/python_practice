

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.
 

# Create  a class

class Redowan:
    x = "Hi I'm Md. Redowan"
print(Redowan.x)


# Create an object

class Person:
    name = "Redowan"
    age = 23

print(Person.name)  # Output: Redowan
print(Person.age)   # Output: 23


# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:


# The string representation of an object 

class student1:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

x = student1("Redowan", 23)
print(x)

# Output: <__main__.student1 object at 0x...>



# The string Representation of an obect without the __str__() function

class student2:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"
    
x = student2("Redowan", 23)
print(x)

# Output: Redowan(23)



# Object Methods

class student3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def y(self):
        print("Hi my name is  " + self.name)

x = student3("Redowan", 23)
x.y()

# Output: Hi my name is  Redowan


# The self parameter forwards to oop 2nd part



