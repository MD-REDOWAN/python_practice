

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# Python has a built-in package called re, which can be used to work with Regular Expressions.

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


# The findall() function
# The findall() function returns a list containing all matches.

import re


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 



# The split() Function
# The split() function returns a list where the string has been split at each match:


import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Output: ['The', 'rain', 'in', 'Spain']



# The sub() Function
# The sub() function replaces the matches with the text of your choice:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


# Match object
# .span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


# Output: (12, 17)


import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Output: The rain in Spain


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Output: Spain


