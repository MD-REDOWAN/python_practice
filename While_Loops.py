

# Python has two prinnitve loop commands:
# 1. for loops
# 2. while loops

# while loop example

i = 5 
while i < 10:
    print(i)
    i += 1


# Use the break statement

i = 1
while i < 7:
    print(i)
    if i == 5:
        break
    i += 1




# The else statement

i = 6
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")



# The continue statement stop current iteration and continue with the next:

i = 1
while i < 7:
    i += 1
    if i ==5:
        continue
    print(i)

# Output: for the continue statement not printing value of = i and continue condition value
# that's why 1 not print and 5 not print