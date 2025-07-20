

# Python Inheritance

# parent class is the class being inherited also called base class
# Child class is the class that inherits from another class , also caleed derived class


# create a Parent class

class student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

x = student1("Redowan", 23)
x.display()

# Output: Redowan 23



# Create a Child class


class person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printname(self):
        print(self.first_name, self.last_name)

class student2(person):
    pass

x = student2("MD", "Redowan")
x.printname()

# Output: MD Redowan



# using the  __init__() fuciton

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student3(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student3("Osama", "Akib")
x.printname()

# Output: Osama Akib



# Using the super() function


class person1:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def display(self):
      print(self.name, self.age)

class student4(person1):
    def __init__(self, name, age):
     super().__init__(name, age) # calling the parent class constructor

x = student4("Redowan", 23)
x.display()

# Output: Redowan 23



# Add properties
 

class person2:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def display(self):
      print(self.name, self.age)

class student5(person2):
    def __init__(self, name, age):
     super().__init__(name, age) # calling the parent class constructor
     self.grade = "A+"
     
x = student5("Redowan", 23)
print(x.grade)

# Output: A+



# Add Method

class Person3:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student6(Person3):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student6("Redowan", "Hossain", 2025)
x.welcome()

# Output: Welcome Redowan Hossain to the class of 2025



