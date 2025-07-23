

"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks."""

# The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")

# Output: 
# Try_Except.py
#  An exception occurred



# Many Exceptions

try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("an exception occured")

# Output:
# variable x is not defined




# Else can use the else keywod to difine a block of code to be executed if no errors were raised:

try:
    print(x)
except:
    print("Find a problem")
else:
    print("Nothing happed") 

# Output: Find a problem



# Finally : The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The tr execpt is finished")

# Output:
# Something went wrong
# The tr execpt is finished



# Rrise an exception

x = -1
if x < 0:
    raise Exception("Sorry , No number below zero")

# Exception: Sorry, no numbers below zero



# Example

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# Output:
# TypeError: Only integers are allowed

