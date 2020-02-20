# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900
#
#     def sell(self):
#         print(self.__maxprice)
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
# c = Computer()
# c.sell()             #  900
#
# # change the price
# c.__maxprice = 1000
# c.sell()             #  900 price doesn't change
#
# # using setter function
# c.setMaxPrice(2000)
# c.sell()             # 2000

class Car:
   __maxspeed = 0
   __name = ""

   def __init__(self):
      self.__maxspeed = 200
      self.__name = "Supercar"

   def drive(self):
      print( self.__maxspeed)
      print( self.__name)

   def setmaxspeed(self,speed,name):
      self.__maxspeed=speed
      self.__name=name

c = Car()
c.drive()

c.__maxspeed = 10  # will not change variable because its private
c.drive()

c.setmaxspeed(100,'duster')
c.drive()

c.setmaxspeed(10,'BMW')
c.drive()
