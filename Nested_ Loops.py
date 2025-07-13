

# A nested looop is inside a loop 


items1 = ["apple", "banana","mango"]
items2 = ["cherry", "pinepple"]

for x in items1:
    for y in items2:
        print(x, y)

"""Output:
apple cherry
apple pinepple
banana cherry
banana pinepple
mango cherry
mango pinepple
"""


