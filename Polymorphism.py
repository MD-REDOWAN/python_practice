

# The word "polymorphism" means "many forms", and it occurs when we have multiple classes with methods of the same name.


# for strings len() returns the number of characrers

x = "Hi I amm Redowan"
print(len(x)) # Output: 15


# Tuples len() return the number of items in the tuple

fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Output: 3


# Dictionay len() return the number of key/ value pairs in the dictionary

person = {
    "name": "Redowan",
    "age": 23,
    "city": "Dhaka"
}

print(len(person))

# Output: 3



# Class Polymorphism car, boat and plane
# Polymorphism with functions : move() 


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Driveing on the road")

class Boat:
    def __init__(self, brand, model):
        self.type = "Sailboat"
        self.model = "Marcidies"

    def move(self):
        print("Sailing on the water")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Flying in the sky")

About_Car = Car("BMW", "x7")
About_Boat = Boat("Yamaha", "242X")
About_Plane = Plane("Boeing", "747")

for x in (About_Car, About_Boat, About_Plane):
    x.move()


# Output:
# Driveing on the road
# Sailing on the water
# Flying in the sky



# Inheritance Class Polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

  