#Local variables:
# Sometimes to meet temporary requirements of programmer,we can declare variables inside a
# method directly,such type of variables are called local variable or temporary variables.
# Local variables will be created at the time of method execution and destroyed once method
# completes.
# Local variables of a method cannot be accessed from outside of method.

# Ex1:
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()

# Ex:2
class Test:
    def m1(self):
        a=1000
        print(a)
    def m2(self):
        b=2000
        print(a) #NameError: name 'a' is not defined
        print(b)
t=Test()
t.m1()
t.m2()

