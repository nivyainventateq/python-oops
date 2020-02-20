# # Multiple inheritance
# Multiple parents but single child
# class P1:
#     def m1(self):
#         print('Parent1 Method')
# class P2:
#     def m2(self):
#         print('Parent2 method')
# class C(P1,P2):pass
# c=C()
# c.m1()
# c.m2()


class Cal1:
    def Sum(self,a,b):
        return a+b
class Cal2:
    def Mul(self,a,b):
        return a*b
class Derived(Cal1,Cal2):
    def Divi(self,a,b):
        return a/b
d = Derived()
print(d.Sum(10,20))
print(d.Mul(10,20))
print(d.Divi(100,20))






