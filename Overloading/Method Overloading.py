# Method Overloading
#
 # If 2 methods having same name but different type of arguments then those methods are said to
# be overloaded methods.
# Eg: m1(int a)
#     m1(double d)
# But in Python Method overloading is not possible.
# If we are trying to declare multiple methods with same name and different number of arguments
# then Python will always consider only last method.


# class Test:
# # define single argument method
#     def method(self, a):
#         print(a)
# obj = Test()        # create object of class
# obj.method(5)       # call method with integer argument
# obj.method('Hello') # call method with string argument
# obj.method(10.2)    # call method with double argument
# obj.method(10.2,99) # TypeError: method() takes 2 positional arguments but 3 were given


class Test:
    def m1(self):
        print('no-arg method')
    def m1(self,a):
        print('one-arg method')
    def m1(self,a,b):
        print('two-arg method')
t=Test()
# t.m1()
# t.m1(10)
t.m1(10,20)

class Test:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The Sum:',total)
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum()



