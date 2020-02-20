# Hierarchcl inheritance
# one parent but multiple childs @ same level
# A-> Parent
# B-> Childrens

class Parent:
    def m1(self):
        print('parent method')

class Child1(Parent):
    def m2(self):
        print("child1 method")

class Child2(Parent):
    def m3(self):
        print("Child2 method")

c=Child1()
c.m1()
c.m2()
c1=Child2()
c1.m1()
c1.m3()


