# creating class

class test:
    x = 1
print(test.x)

# In python, we must notice that each class is associated with a documentation
# string which can be accessed by using <class-name>.__doc__.

class student:
    '''This is my first class'''
print(student.__doc__)
help(student)       #Doc  string


# class MyClass:
# 	"This is my second class"
# 	a = 10
# 	def test(self):
# 	    print('Hello')
# print(MyClass.a)
# print(MyClass.test)
# print(MyClass.__doc__)
# m=MyClass()
# print(m.a)
#

# Creating  an object

class Fruit:
    name="Orange"
s=Fruit()  # creating an object of class fruit and assign it to the varibale Fruit
print(s.name) # access the class attribute name inside the class  Fruit
print(Fruit.name)

# class Fruit:
#     print("orange")
# d=Fruit()

# class MyClass:
# 	a = 90
# 	def func(self):
# 		print('Hello')
# ob = MyClass()
# ob.func()
# print(MyClass.func)
# print(ob.func)
# print(ob.a)
# print(MyClass.a)
#
# ob1=MyClass()
# print(MyClass.a)
# print(ob1.a)
#
# def sum(a,b):
#     print(a+b)
# sum(10,7)


class Employee:
    k = int(input("enter id :"))
    l = input("enter name:")
    def display (self,k,l):
	    print(self.k,"...." , self.l)
a=Employee()
a.display('k','l')

