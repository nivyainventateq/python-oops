# How to access Instance variables:
# 1. with in the class by using self variable and
# 2. outside of the class by using object reference.

class Student:
    def __init__(self,x,y):
        self.name=x
        self.id=y
    def display(self):
      print(self.name)
      print(self.id)
s=Student('xyz',17)
s.display()
print(s.name,s.id)
s.marks=25
print(s.marks)
print(s.__dict__)