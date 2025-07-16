

# Default Parameter Value

def func1(country = "Bangladesh"):
    print(" I am from " + country)

func1("Rmaganj")
func1("Lakshmipur")
func1()  # This will use the default value "Bangladesh"



# passing a list as an argument

def func2(food):
    print(food)

fruits = ["Apple", "Banana", "Mango"]
func2(fruits)  # Passing the list as an argument)


# Using for loop same thing

def func3 (food):
    for x in food :
        print(x)

fruits = ["Apple", "Banana", "Mango"]
func3(fruits)


# Return Values


def func4(num):
    return num * 10

print(func4(2)) # Output: 20
print(func4(7)) # Output: 70
print(func4(10)) # Output: 100



# positonal- Only pass Arguments with(, /) without error  , only actual arguments can be passed


def func5(name, /):
    print(name)

func5("Redowan")




# Without the *, you are allowed to use positional arguments even if the function expects keyword arguments:

def func6(*, x):
  print(x)

func6(x = 3)




# Recursion

def x(k):
  if(k > 0):
    result = k + x(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
x(6)



