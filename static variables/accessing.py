# How to access static variables:
# 1. inside constructor: by using either self or classname
# 2. inside instance method: by using either self or classname
# 3. inside class method: by using either cls variable or classname
# 4. inside static method: by using classname
# 5. From outside of class: by using either object reference or classname

class Test:
    a="Hello Welcome to Python Section"

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m1(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m3():
        print(Test.a)

t = Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()

# 1. inside constructor: by using either self or classname

class Test:
    a = "Hello Welcome to Python Section"
    def __init__(self):
        print(self.a)
        print(Test.a)
t=Test()

# 2. inside instance method: by using either self or classname

class Test:
    a = "Hello Welcome to Python Section"
    def m1(self):
        print(self.a)
        print(Test.a)
t=Test()
t.m1()

# 3. inside class method: by using either cls variable or classname

class Test:
    a = "Hello Welcome to Python Section"
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
t=Test()
t.m2()

# 4. inside static method: by using classname

class Test:
    a = "Hello Welcome to Python Section"
    @staticmethod
    def m3():
        print(Test.a)
t=Test()
t.m3()

# 5. From outside of class: by using either object reference or classname
class Test:
    a = "Hello Welcome to Python Section"
t=Test()
print(Test.a)
print(t.a)

