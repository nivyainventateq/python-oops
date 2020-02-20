class Test:
    def __init__(self):
        print('No-Arg Constructor')
    def __init__(self,a):
        print('One-Arg constructor')
    def __init__(self,a,b):
        print('Two-Arg constructor')
# t1=Test()
# t1=Test(10)
t1=Test(10,20)


# def sum(a,b):
#     x=a+b
#     print(x)
# def sum(a,b,c):
#     y=a+b+c
#     print(y)
# sum(10,20) #TypeError: sum() missing 1 required positional argument: 'c'
# sum(10,20,30)
