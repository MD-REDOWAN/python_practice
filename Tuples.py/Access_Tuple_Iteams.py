


# Accessing 2nd iteams in a tuple

tuple1 = ("MD", "Redowan", "Hossain", "id", "1310") # first index 0
print(tuple1[1])  # Output: Redowan


# Negative Indexing (-1 last from the end)
tuple2 = ("apple", "banana", "cherry", "kiwi", "mango")
print(tuple2[-1])  # Output: mango (last item)


# Range of Indexes (Always last range of Index is not included)

tuple3 = ("apple", "banana", "cherry", "kiwi", "mango")
print(tuple3[1:4])  # Output: ('banana', 'kiwi') (items from index 2 to 3)


# Single Range of Indexes ( First Index)

tuple4 = ("MD", "Redowan", "Hossain", "id", "1310")
print(tuple4[1:]) # Output: ('Redowan', 'Hossain', 'id', '1310') (items from index 1 to the end)

# Another single range of Indexes( Last Index )

tuple5 = ("MD", "Redowan", "Hossain", "id", "1310")
print(tuple5[:4]) # Output: ('MD', 'Redowan', 'Hossain', 'id') (items from index 0 to 3)



# Range of Negatives Indexe ()
tuple6 = ("apple", "banana", "cherry", "kiwi", "mango")
print(tuple6[-4:-1])  # Output: ('banana', 'cherry', 'kiwi') (items from index -4 to -2)


# Check if Item Exists in Tuple

tuple7 = ("MD", "Redowan", "Hossain", "id", "1310")
if "Redowan" in tuple7:
    print("Yes", "Redowan is in the tuple") # Output: Yes, Redowan is in the tuple




