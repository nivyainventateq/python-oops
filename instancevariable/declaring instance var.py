# Where we can declare Instance variables:
# 1. Inside Constructor by using self variable
# 2. Inside Instance Method by using self variable
# 3. Outside of the class by using object reference variable

# 1. Inside Constructor by using self variable

class Student:
    def __init__(self):
        self.name='Arun'
        self.id=108
s=Student()
print(s.__dict__)

# 2. Inside Instance Method by using self variable

class Student:
    def __init__(self,x,y):
        self.name=x
        self.id=y
    def test(self,z):
        self.age=z
s=Student('Misa',12)
s.test(25)
print(s.__dict__)

# 3. Outside of the class by using object reference variable
class Student:
    def __init__(self,x,y):
        self.name=x
        self.id=y
    def test(self,z):
        self.age=z
s=Student('Misa',12)
s.test(25)
s.subject='Computer Science'
print(s.__dict__)

# Using Constructor, Using Instance Method and Using Object Reference together
class Student:
    def __init__(self,x,y):
        self.name=x
        self.id=y
    def info(self):
        self.marks=60
s=Student("xyz", 11)     # using  constructor
s.info()                 # using instance method
s.std= 'seventh'                  # using object reference
print(s.__dict__)        # {'name': 'xyz', 'id': 11, 'marks': 60}
print(s)                 # <__main__.Student object at 0x7f8eecc27f28>



#Ex: 1
class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        self.d=40
    def m2(self):
        self.e=50
t=Test()
t.m1()
t.m2()
t.f=60
print(t.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'd': 40}
#
# t1=Test()
# t1.m2()
# print(t1.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'e': 50}
#
# t2=Test()
# t2.m2()
# t2.f=200
# print(t2.__dict__)  #{'a': 10, 'b': 20, 'c': 30, 'e': 50, 'f': 200}


l=[1,2,3,4]
k=l.index(3)
print(k)
l.insert(0,l.pop(k))
print(l)