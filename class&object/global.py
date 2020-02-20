# Global variables using function
z = 20
def function():
    global z
    z=11
    global z
    print(z)

# function()

# The global variable z can be used all throughout the program, inside functions or outside.
# A global variable can modified inside a function and change for the entire program.

# global function within class
# a = 0
# class b():
#     global a
#     a = 10
# print(a)

# Local variables
# Local variables can only be reached in their scope.
# The variables x and y can only be used inside the function sum, they don’t exist outside of the function.
def sum(x,y):
    sum = x + y
    return sum
print(sum(8,6))

# both global and local variables
z = 10
try:
    def func1():
        global z
        z = 3
        print(z)
    def func2(x,y):
        global z
        return x+y+z
    func1()
    total = func2(4,5)
    print(total)
except RecursionError:
    print("hello")
