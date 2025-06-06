# Assign String to a Variable

a = "Hi I am Redowan"
print(a)

# Multiline String

a = """Hi,
What's up?,
It's me Redowan,
What about you."""
print(a)

# Loop style string

for x in "Redowan":
  print(x) 

# Output:
"""
R
e
d
w
a
n """

# Check String Length

a = "Hello, World!"
print(len(a))


# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])
# Output: e


# True or False::

txt = "The best things in life are free!"
print("expensive" not in txt)
# Output: True

#if right print:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  # Output:Yes, free is present.

# Slicing String

# Get the characters from position 2 to position 4 (not included):

b = "Redowan"
print(b[2:4])
#output: d, o


#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

# Negative indexing
#From: "d" from right side 4(position -5)To, but not included: "d" in "World!" (position -2):

b = "msredowan"
print(b[-5:-2])
# output: dow


# upper() and lower()

a = "Redowan Hossain"
print(a.upper())
      #Output: REDOWAN HOSSAIN

b = "Redowan Hossain"
print(b.lower())
# Output: redowan hossain


# remove whitespace

x = " Redowan Hossain "
print(x.strip())
# Output: "Redowan Hossain"

#Replace string

y = "redowan Hossain"
print(y.replace("redowan","Redowan"))
# Output: Redowan Hossain


# Split string
z = "Redowan Hossain"
print(z.split(" "))  # returns ['Redowan', 'Hossain']


# Concatenation of strings
a = "Redowan"
b = "Hossain"
c = a + b
print(c)  # Output: RedowanHossain


# Concatenation with space

a = "Redowan"
b = "Hossain"
c = a + " " + b
print(c)  # Output: Redowan Hossain


# F strings (combine data types)
# f specifying the string format

age = 23
txt = f"My name is Redowan, I am{ age }years old."
print(txt)  # Output: My name is Redowan, I am 23 years old.

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)  # Output: The price is 59.00 dollars

#
txt = f"The price is {20 * 59} dollars"
print(txt)


#Escape Character

txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # Output: We are the so-called "Vikings" from the north.

## Python - String all Methods from (w3)##