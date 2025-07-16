

#  We can pass data know as parameters, into a function
# A function can return data as a result


# Calling a Fuction

def redowan():
    print("Hi I am Redowan")

redowan()



# Information can be passed into functions as parameter/ arguments

def student(name):
    print("Student name " + name)

student("Redowan")
student("Akib")



# A function can have multiple parameters

def student_info(name, age):
    print("student name " + name, "and age is " + age)
student_info("Redowan", "23")
student_info("Akib", "24")



# Another example fuction 2 arguments, and gets 2 arguments

def student_info2(id, name):
    print(id, " " + name)

student_info2("1310", "Redowan")



# If we want to specific index print, we have to use * arbitrary arguments

def student3(*student):
    print("The Topper student is " +student[1])

student3("Redowan", "Shihab", "Akib")
# Output: The Topper student is Shihab



# Keyword Arguments

def child(child1, child2):
    print("The littiest child is " + child2)

child(child1 = "Akib", child2 = "Abir")



# specifying index kyword arguments using arbitrary argments: **kwargs

def kid(**boy):
    print("The kid name is " +boy["good"])

kid(bad = "Eram", good = "Redowan")

