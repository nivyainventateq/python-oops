# # The problem in this approach is if obj does not contain talk() method
# # then we will get AttributeError
#
# class Duck:
#     def talk(self):
#         print('Quack.. Quack..')
# class Dog:
#     def talk(self):
#         print('Bow Bow..')
# class Cat:
#     def talk(self):
#         print('Moew Moew ..')
# class Goat:
#     def talk(self):
#         print('Myaah Myaah ..')
# def f1(obj):
#     obj.talk()
# l=[Duck(),Cat(),Dog(),Goat()]
# for obj in l:
#     f1(obj)

# Ex:2
# class Duck:
#     def talk(self):
#         print('Quack.. Quack..')
# class Dog:
#     def bark(self):
#         print('Bow Bow..')
# def f1(obj):
#     obj.talk()
# d=Duck()
# f1(d)
# d=Dog() #AttributeError: 'Dog' object has no attribute 'talk'
# f1(d)

# Program with hasattr() function:

class Duck:
    def talk(self):
        print('Quack.. Quack..')
class Human:
    def talk(self):
        print('Hello Hi...')
class Dog:
    def bark(self):
        print('Bow Bow..')
def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
d=Duck()
f1(d)
h=Human()
f1(h)
d=Dog()
f1(d)
