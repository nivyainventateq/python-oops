# A->B->c->D
# features of the base class and the derived class&object is inherited into the new derived class&object
# Combination either A->B or B->C or C-> D

class Parent:
    def m1(self):
        print('parent method')

class Child(Parent):
    def m2(self):
        print("child method")

class Subchild(Child):
    def m3(self):
        print("Subchild method")

sc=Subchild()
sc.m1()
sc.m2()
sc.m3()

class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")
d = DogChild()
d.bark()
d.speak()
d.eat()     