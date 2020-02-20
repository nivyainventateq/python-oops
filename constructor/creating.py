class test:
    def __init__(self):
        print("Software Developer")
t=test()
t1=test()


# # Points to Remember:
# 1. The name of the constructor is always: __init__()
# 2. The main objective is to declare and initialize instance variables
# 3. for every object construcor will be executed.    def __init__(self):
#
# # ex:1

# 1 object = once constructor will be executed
# 4. every constructor should take atleast one argument that is self.
# 5. python will provide default constructor
# 6. constuctor is executed during creatng of an object

# Program to demonistrate constructor will execute only once per object:
class Test:
    def __init__(self):
        print("Constructor Execution")

    def m1(self):
        print("Method Execution")
t=Test()
t.m1()


class Student:
    def __init__(self,name,rollno):
        print("Constructor Execution")
        self.name=name
        self.rollno=rollno

    def display(self):
        print("Method Execution")
        print('Hello Myself:',self.name)
        print('My age is:',self.rollno)

s=Student('Pavan',1)
s1=Student('Akash',2)
s.display()
s.display()
s1.display()

