



# python useing for loop

for x in "Redowan" :
 print(x)




# Another example
 
person1 = ["Md", "Redowan", "Hossain"]

for x in person1:
    print(x)


# The break statement

person2 = [1, 2, 3, 4, 5]
for x in person2:
   print(x)
   if x == 3:
      break
   


# if we want continue after break

person3 = [1, 2, 3, 4, 5, 6]

for x in person3:
   print(x)
   if x == 2:
      continue
   print(x)



# The range() function

for x in range(5):
   print(x)

# Output:
"""
0
1
2
3
4
5"""


# The range use as a parameter

for x in range (3,5):
   print(x)

# Output: 3, 4


# Another example

for x in range (10):
   
   if x ==5:
      break
   print (x)
else:
   print("code has some error")


## for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error

for x in [1,2,3]:
    pass



