
# Ex:1
class Example:
    def __init__(self):
        print("Object created")
    # destructor
    def __del__(self):
        print( "Object destroyed")

# creating an object
myObj = Example()
# to delete the object explicitly
del myObj

# Ex:2
import time
class Test:
    def __init__(self):
        print("Constructor Execution...")
    def __del__(self):
        print("Destructor Execution...")    
list=[Test(),Test(),Test()]
del list
time.sleep(5)
print("End of application")

# Ex:3
# import time
# class Test:
#     def __init__(self):
#          print("Object Initialization...")
#     def __del__(self):
#         print("Fulfilling Last Wish and performing clean up activities...")
# t1=Test()
# t1=None
# time.sleep(5)
# print("End of application")