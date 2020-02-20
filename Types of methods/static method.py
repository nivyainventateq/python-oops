# class Numeric:
#     @staticmethod
#     def add(x,y):
#         print('The Sum:', x + y)
#
#     @staticmethod
#     def product(x, y):
#         print('The Product:', x * y)
#
#     @staticmethod
#     def average(x, y):
#         print('The average:', (x + y) / 2)
# Numeric.add(10, 20)
# Numeric.product(10, 20)
# Numeric.average(10, 20)

# Passing members of one class to another class:
# We can access members of one class inside another class.
class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('Employee Number:',self.eno)
        print('Employee Name:',self.ename)
        print('Employee Salary:',self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
e=Employee(101,'MISA',10000)
Test.modify(e)


