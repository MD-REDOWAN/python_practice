

# Change Tuple Value

x = ("MD", "Redowan", "Hossain", "id", "1310")
y = list(x)  # Convert tuple to a list
y[1] = "Mirza"  # Change the second item
x = tuple(y)  # Convert list back to a tuple
print(x)  # Output: ('MD', 'Mirza', 'Hossain', 'id', '1310')


# Add Iteams (Convert the tuple into a list, add "orange", and convert it back into a tuple:)

x = ("MD", "Redowan", "Hossain", "id", "1310")
y = list(x)  # Convert tuple to a list
y.append("mirza")  # Add a new item
print(y)  # Output: ['MD', 'Redowan', 'Hossain', 'id', '1310', 'mirza']


# Remove Iteams (Convert the tuple into a list, remove "Hossain", and convert it back into a tuple:)

x = ("MD", "Redowan", "Hossain", "id", "1310")
y = list(x)  # Convert tuple to a list
y.remove("Hossain")  # Remove an item
print(y)  # Output: ['MD', 'Redowan', 'id', '1310']


# del (Delete the entire tuple)
x = ("MD", "Redowan", "Hossain", "id", "1310")
del x  # Delete the tuple
print(x)   # This will raise an error because x is deleted