# Check a object is an integer or not:

a = 100
print(isinstance(a, int))
# Output: True


# Print a message based on whether the condition is True or False:

a = 200
b = 100
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")


#Evaluate Values and Variables

# 1.
print(bool("Redowan"))
print(bool(20))

# 2.
x = "Redowan"
y = 50

print(bool(x))
print(bool(y))


# Some Values are False Like:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# Output: False


# Most Values are True Like:

bool("Redowan")
bool(240)
bool(["Md", "Redowan", "Hossain"])
# Output: True


#Functions can Return a Boolean:
# 1.
def myFunction():
    return True
print(myFunction())
# Output: True

# 2.
def myFunction2():
    return False
print(myFunction2())

# 3.
def myfunction():
    return  True

if myfunction():
    print("Yes")
else:
    print("No")
    # Output: Yes