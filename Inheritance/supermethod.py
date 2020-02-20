# Super () can be used in the methods
# class P:
#     def property(self):
#         print('cash+land+gold')
#     def marriage(self):
#         print("Priya")
# class C(P):
#     def marriage(self):
#         # super().marriage()
#         print("Shilpa")
# c=C()
# c.property()
# c.marriage()

# class Animal(object):
#     def __init__(self, AnimalName):
#         print(AnimalName, 'is a warm-blooded animal.')
#
# class Dog(Animal):
#     def __init__(self):
#         print('Dog has four legs.')
#         super().__init__('lion')
# d1 = Dog()


class college:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(college):
    def __init__(self,name,age,rollno,marks):
        # super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
s=Student('xyz',20,10,70)
print(s.name)
print(s.age)
print(s.rollno)
print(s.marks)


