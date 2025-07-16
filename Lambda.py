

# Syntax of lambda

# lmbda arguments : expression


# Example:

x = lambda a : a + 5
print(x(5))  # Output: 10   

 

# Multiple arguments

x = lambda a, b, c : a + b + c

print(x(10, 5, 5)) # Output : 20



# Multiple arguments

x = lambda a, b : a * b
print(x(10, 5))  # Output: 50



# Actually lambda is an anonymous function, for helpul multiple functiond


def func(x):
    return lambda a : a * x



# using functions

def num(n):
    return lambda a : a * n

first_result = num(5)
second_result = num(10)

print(first_result(2)) # Output: 10
print(second_result(3)) # Output: 30


