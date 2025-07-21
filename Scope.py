

# The local variable can be accessed from a function within the function:
# Just x use as a funciton



def func():
    a = 500
    def x():
        print(a)
    x()  # Call the inner function

func()

# Output: 500




# Global Scope
# A variable created outside of a function is global and can be used by anyone:


b = 100
def func1():
   print(b)

func1()

print(b)

# Output: 100



# Global keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Output: 300



# Nonlocal keyword


def func2():
   x = "what's your name"
   def myfunc():
      nonlocal x
      x = "My name is"
   myfunc()
   return x
print(func2())

# Output: My name is


