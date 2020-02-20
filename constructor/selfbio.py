# Self variable:
# self is the default variable which is always pointing to current object (like this keyword in Java)
# By using self we can access instance variables and instance methods of object.

# Note:
# 1. self should be first parameter inside constructor
# def __init__(self):
# 2. self should be first parameter inside instance methods
# def talk(self):
# 6. constuctor is executed during creatng of an object

# class test:
#     def __init__(self):
#         print("constructor")
# s=test()

 # ex:
class student:
    def __init__(self):
        print(id(self))
s=student()
print(id(s)) # returns address of self.id

# # both s and self are point to the same object so the address will be same

class Employee:
    def __init__(self,x,y,z):
        self.ename=x
        self.eage=y
        self.eaddress=z
    def info(self):
        print("ename:",self.ename)
        print("eage:",self.eage)
        print("eaddress:",self.eaddress)
e1=Employee("Akash",22,'Bangalore')
e2=Employee("Priya",23,'Mangalore')
e1.info()
e2.info()
