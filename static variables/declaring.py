class Test:
    x=10
    def __init__(self):
        self.y=20
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x=202
t1.y=300
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# Various places to declare static variables:
# 1. In general we can declare within the class directly but from out side of any method
# 2. Inside constructor by using class name
# 3. Inside instance method by using class name
# 4. Inside classmethod by using either class name or cls variable
# 5. Inside static method by using class name

class Test:
    a=10                #within the class directly but from out side of any method
    def __init__(self):
        Test.b=20       #Inside constructor by using class name
    def m1(self):
        Test.c=30       #Inside instance method by using class name
    @classmethod
    def m2(cls):
        cls.d1=40       # classmethod by using cls variable
        Test.d2=400     # classmethod by using class name
    @staticmethod
    def m3():
        Test.e=50       #Inside static method by using class name
print(Test.__dict__)
t=Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f=60
print(t.__dict__)

# 1. within the class directly but from out side of any method
class Test:
    a=10
t=Test()
print(Test.__dict__)
Test.a1=60
print(Test.__dict__)

# 2. Inside constructor by using class name
class Test:
    def __init__(self):
        Test.b=20
t=Test()
print(Test.__dict__)

# 3.Inside instance method by using class name
class Test:
    def m1(self):
        Test.c=30
t=Test()
t.m1()
print(Test.__dict__)

#4.classmethod by using either class variable or class name
class Test:
    @classmethod
    def m2(cls):
        cls.d1=40
        Test.d2=400
t=Test()
t.m2()
print(Test.__dict__)

#5 Inside static method by using class name
class Test:
    @staticmethod
    def m3():
        Test.e=50
t=Test()
t.m3()
print(Test.__dict__)

