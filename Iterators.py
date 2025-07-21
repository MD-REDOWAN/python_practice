

# An iterator is an object that contains a countable number of values.
# which consist of the methods __iter__() and __next__().



# Iterator vs Iterable

# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
#All these objects have a iter() method which is used to get an iterator:


fruits = ("apple", "banana", "cherry")
x = iter(fruits)

print(next(x))  # Output: apple
print(next(x))  # Output: banana
print(next(x))  # Output: cherry


# Another Example of an iterable object containing a sequence of characters:

fruit = "Apple"
x = iter(fruit)

print(next(x))  # Output: A
print(next(x)) # Output: p
print(next(x))  # Output: p
print(next(x))  # Output: l



# Iterate value of a tuple using a for loop:

fruits1 = ("apple", "banana", "cherry")

for x in fruits1:
    print(x)

# Output:
# apple
# banana
# cherry    



# itrate the characters of a string using a for loop:

fruit1 = "Apple"

for x in fruit1:
    print(x)

# Output:
# A
# p
# p
# l


# Create an Iterator

# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# we can use the StopIteration statement.

class Numbers:
    def __iter__ (self):
        self.a = 1
        return self
    
    def __next__ (self):
        if self.a <= 10:
            x = self.a 
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = Numbers()
y = iter(myclass)

for x in y:
    print(x)
    


# Output:
# 1
# 2 
# 3
# 4
# 5
# 6
# 7
# 8
# 9 
# 10


