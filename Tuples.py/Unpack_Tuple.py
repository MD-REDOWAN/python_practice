# Packing tuples :

tuple1 = ("MD", "Redowan", "Hossain", "id", "1310")
print(tuple1)  # Output: ('MD', 'Redowan', 'Hossain', 'id', '1310')


# Unpacking tuples:

tuple2 = ("MD", "Redowan", "Hossain")
(apple, banana, cheri) = tuple2  # Unpacking the tuple into variables
print(apple)  # Output: MD
print(banana)  # Output: Redowan
print(cheri)  # Output: Hossain

# Unpacking with asterisk (*):

tuple3 = ("MD", "Redowan", "Hossain", "id", "1310", "D2")
(apple, banana, cheri, *kiwi) = tuple3  # Unpacking with an asterisk
print(apple)  # Output: MD
print(banana)  # Output: Redowan
print(cheri)  # Output: Hossain
print(kiwi)  # Output: ['id', '1310', 'D2'] (remaining items packed into a list)


# Added to another variable name than the last

tuple4 = ("MD", "Redowan", "Hossain", "id", "1310", "D2")
(apple, banana, cheri, *kiwi, mango) = tuple4  # Unpacking with an asterisk and another variable
print(apple)  # Output: MD 
print(banana)  # Output: Redowan
print(cheri)  # Output: Hossain
print(kiwi)  # Output: ['id', '1310'] (remaining items packed into a list)
print(mango)  # Output: D2 (last item unpacked into a variable)

