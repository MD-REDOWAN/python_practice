

# The self Parameter
# It does not have to be named self, you can call it whatever you like,

class student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(abc):
        print("Hi my name is " + abc.name)

x = student1("Redowan", 23)
x.display()

# Output: Hi my name is Redowan



# Modify Object Properties

class student2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(a):
        print("Hey This is " + a.name)

x = student2("Redowan", 23)
x.display()
x.age = 25
print(x.age)

# Output:
# Hey This is Redowan 
# 25 years old



# Delete the object properties using del keyword

class student3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(a):
        print("Hey This is " + a.name)

x = student3("Redowan", 23)
del x.name   # delete object properties
x.display()



# The pass statement

class student:
    def __init__(self):
        pass

#  having an empty class definition like this, would raise an error without the pass statement


