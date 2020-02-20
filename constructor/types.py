# Constructor with Default Arguments:

class Test:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0/1/2/3 number of arguments')
t1=Test()
t2=Test(10)
t3=Test(10,20)
t4=Test(10,20,30)
t4=Test(10,20,30,40) #TypeError: __init__() takes from 1 to 4 positional arguments but 5 were given


# Constructor with Variable Number of Arguments:

class Test:
    def __init__(self,*a):
        print('Constructor with variable number of arguments')
t1=Test()
t2=Test(10)
t3=Test(10,20)
t5=Test(10,20,30,40,50,60)