

# Python supports the usual logical conditions from mathematics:
"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# If Statement 

a = 50
b = 10
if a > b :
    print("1: a is greater than b")


# Else condition present like (else) :

a = 10
b = 20
if a > b :
    print("a is greater than b")
else:
    print("2: b is greater than a")


# Else if python present like (elif)

a = 15
b = 30
if a>b:
    print("a is greater than b")
elif b>a:
    print("3: b is greater than a")
else:
    print("a and b are equal")


# short: if in one line

if a>b: print("a is greater than b")


# Short: if....else

a = 10
b = 40
print("a is less than b") if a < b else print("a is greter than b")


# (and) keyeord is a logical operator for if condition

a = 300
b = 250
c = 200
if a > b and b > c :
    print(" Printing Values are Right")
else :
    print("Not printing")



# Or keyword also logical operator

a = 300
b = 250
c = 200
if a > b or b > c :
    print(" Printing Values are Right")
else :
    print("Printing Values are Right")


# Not : not keyword is also logical operator

a = 100
b = 200
if not a > b:
    print("a is not greater than b")


# you can have if stat

a = 50
if a > 20:
    print("Above 20")
    if a > 40:
        print("and also above 40!")
    else:
        print("but not abobe 40")


# The pass steatement

a = 20
b = 40
if b > a :
    pass


