# How to delete static variables of a class:
#
# We can delete static variables from anywhere by using the following syntax
# del classname.variablename
# But inside classmethod we can also use cls variable
# del cls.variablename
#
# class Test:
#     a=10
#     def __init__(self):
#         Test.b=20
#         del Test.a
#
#     def m1(self):
#         Test.c=30
#         del Test.b
#
#     @classmethod
#     def m2(cls):
#         cls.d=40
#         del Test.c
#
#     @staticmethod
#     def m3():
#         Test.e=50
#         del Test.d
# print(Test.__dict__)
# t=Test()

class Test:
    a=10
t1=Test()
del t1.a #AttributeError: a