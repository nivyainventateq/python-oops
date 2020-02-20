# single inheritance
# Single parent - single child
# The process of inheriting property from one parent to one calss.

# class Parent:
#     def m1(self):
#         print('parent method')
# class Child(Parent):
#     def m2(self):
#         print("child method")
# p=Parent()
# p.m1()
# c=Child()
# c.m1()
# c.m2()

class Animal:
    def speak(self):
        print("Animal Speaking")
#child class & object Dog inherits the base class&object Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()