

# consider a module to be the same  as a code library
# A file containing a set of functions you want to include in your application


# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# Modules import

import Scope

Scope.myfunc()

# Output: 500



# Renaming Modules

import Scope as a

x = a.func()
print(x)
# Output: none


# Using dir() function to list all the function name or modules name

import Function_part1

y = dir(Function_part1)

print(y)



# From in Module

from Function_part1 import student_info

print(student_info["Akib"])


