class SampleClass:

    def __init__(self, a):
        # private varibale or property in Python
        self.__a = a

    ## getter method to get the properties using an object
    def get_a(self):
        return self.__a

## setter method to change the value 'a' using an object
    def set_a(self, a):
        self.__a = a

## creating an object
obj = SampleClass(10)

## getting the value of 'a' using get_a() method
print(obj.get_a())

## setting a new value to the 'a' using set_a() method
obj.set_a(45)

print(obj.get_a())


# This is how you implement private attributes, getters, and setters in Python.
# The same process was followed in Java. Let's write the same implementation in a Pythonic way.

class PythonicWay:

    def __init__(self, a):
        self.a = a
# You don't need any getters, setters methods to access or change the attributes.
# You can access it directly using the name of the attributes.


# Creating an object for the 'PythonicWay' class
obj = PythonicWay(100)

print(obj.a)


# What's the difference between the above two classes.
# SampleClass hides the private attributes and methods. It implements the encapsulation feature of OOPS.
# PythonicWay doesn't hide the data. It doesn't implement any encapsulation feature.

class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks

n=int(input('Enter number of students:'))
for i in range(n):
    s=Student()
    name=input('Enter Name:')
    s.setName(name)
    marks=int(input('Enter Marks:'))
    s.setMarks(marks)
    print('Hi',s.getName())
    print('Your Marks are:',s.getMarks())
