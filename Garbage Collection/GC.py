# import gc
# print(gc.isenabled())
# gc.disable()
# print(gc.isenabled())
# gc.enable()
# print(gc.isenabled())

# Ex: 2
# import time
# class Test:
#     def __init__(self):
#         print("Constructor Execution...")
#     def __del__(self):
#         print("Destructor Execution...")
# t1=Test()
# t2=t1
# t3=t2
# del t1
# time.sleep(5)
# print("object not yet destroyed after deleting t1")
# del t2
# time.sleep(5)
# print("object not yet destroyed even after deleting t2")
# print("I am trying to delete last reference variable...")
# del t3

# Ex:3 How to find the number of references of an object:
import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t2
t4=t1
print(sys.getrefcount(t1))
