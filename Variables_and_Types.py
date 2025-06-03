a =5
b =10.5
c = "Redowan"

# Mixing operatoes between numbers and strings not supported :print( a + b + c)

print(a + b)

print(type(a)) #print the type of variable a (int)

print(type(c)) # print the type of variable c(string)

print(type(b)) # print the type of variable b(float)


hello = "hello"
world = "world"
#helloworld = hello + " " + world #(concatenation)
print(hello,world)


# Multiple variable simultanuously
X ,Y ,Z = 3, 4, 5
# print the values of X, Y, Z
print(X,Y,Z)


# one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# change this code
mystring = "hello"
myfloat = 10.0
myint = 20


# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
