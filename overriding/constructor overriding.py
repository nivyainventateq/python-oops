# class P:
#     def __init__(self):
#         print('Parent Constructor')
# class C(P):
#     def __init__(self):
#         print('Child Constructor')
# c=C()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def display(self):
        print('Employee Name:',self.name)
        print('Employee Age:',self.age)
        print('Employee Number:',self.eno)
        print('Employee Salary:',self.esal)
e1=Employee('Mickey',48,7245,26000)
e1.display()
e2=Employee('Sunny',39,82426,36000)
e2.display()
