# Sort List Alphanumerically

#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

list1 = [ "banana", "cherry", "apple", "pineapple", "kiwi"]
list1.sort()
print(list1)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'pineapple']


# Another Example of sorting a list of numbers
list2 = [500, 100, 50, 25, 10, 5, 1]
list2.sort()
print(list2)  # Output: [1, 5, 10, 25, 50, 100, 500]


# Sort List in Descending Order
list3 = [ "banana", "cherry", "apple", "pineapple", "kiwi"]
list3.sort(reverse = True)
print(" descending order:", list3)  # Output: ['pineapple', 'kiwi', 'cherry', 'banana', 'apple']


# Sort List Numerically
list4 = [500, 100, 50, 25, 10, 5, 1]
list4.sort(reverse = True)
print(list4)  # Output: [500, 100, 50, 25, 10, 5, 1]


# Customize Sort Function
def myfunc(n):
    return abs(n-50)
list5 = [100,500,200,600,800]
list5.sort(key = myfunc)
print(list5)  # Output: [100, 200, 500, 600, 800]


# Case Insensitive sort

list6 = ["banana", "cherry", "Apple", "pineapple", "kiwi"]
list6.sort( key = str.lower)
print(list6)  # Output: ['Apple', 'banana', 'cherry', 'kiwi', 'pineapple']


# reverse the oder of the list iteams

list7 = ["banana", "cherry", "apple", "pineapple", "kiwi"]
list7.reverse()
print(list7)  # Output: ['kiwi', 'pineapple', 'apple', 'cherry', 'banana']



