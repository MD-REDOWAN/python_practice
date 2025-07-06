

# Loop using in Tuple

tuple1 = ("Md", "Redowan","Hossain")
for x in tuple1:
    print(x) 
""" 
output: 
Md
Redowan
Hossain
"""

#loop through the index numbers range() len()

tuple2 = ("Md", "Redowan","Hossain")
for x in range(len(tuple2)):
    print(x)
"""
Output:
0
1
2
"""

# Using while loop

tuple3 = ("Md", "Redowan","Hossain")
i = 0
while i < len(tuple3):
    print(tuple3[i])
    i = i + 1
    
    """
    Output:
    Md
    Redowan
    Hossain
    """