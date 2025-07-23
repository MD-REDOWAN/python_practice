

# f-String formate

age = 30
display = f"Ronaldo is {age}Years old "

print(display)


txt = f"The price is {95:.2f} dollars"
print(txt)

# Output;
# The price is 95:00 dollars



# Perform operations in F-Strngs

txt2 = f"The price is {10*5} taka"
print(txt2)

# Output: The price is 50 taka



# Use the string method upper()to convert a value into upper case letters:


fruit = "apple"

txt3 = f"I love {fruit.upper()}"
print(txt3)

# Output: I love APPLE 



# Multiple Valurs

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."

print(myorder.format(quantity, itemno, price))

# Output: I want 3 pieces of item number 567 for 49.00 dollars.


# Index Number

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Output: His name is John. John is 36 years old.


# Name Index

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

 # Output: I have a Ford, it is a Mustang.



# Formatting Type:
"""
Formatting Types
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format"""


