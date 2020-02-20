# Ex:1 Program to track the number of objects created for a class:
class Test:
    count=0
    def __init__(self):
        Test.count =Test.count+1
    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for test class:',cls.count)
t1=Test()
t2=Test()
Test.noOfObjects()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjects()

# Ex:2
class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print('{} walks with {} legs...'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')