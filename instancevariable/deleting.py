
# How to delete instance variable from the object:
# 1. Within a class we can delete instance variable as follows
# 	del self.variableName
# 2. From outside of class we can delete instance variables as follows
# 	del object reference.variableName

# Ex:1
class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
        self.d=40
    def delete(self):
        del self.a
        del self.b
s=Student()
s.delete()
print(s.__dict__)

# Ex:2
class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
s=Student()
del s.a
print(s.__dict__)