# class Robot(object):
#    def __init__(self):
#       self.a = 123
#       self._b = 1234
#       self.__c = 1235
#
# r= Robot()
# print(r.a)
# print(r._b)
# print(r.__c) #AttributeError: 'Robot' object has no attribute '__c'

# So what’s with the underscores and error?
# A single underscore: Private variable, it should not be accessed directly.
# But nothing stops you from doing that (except convention).
# A double underscore: Private variable, harder to access but still possible.

# Both are still accessible: Python has private variables by convention.
# Private variables are intended to be changed using getter and setter methods.
# These provide indirect access to them:

class Robot(object):
   def __init__(self):
      self.__version = 22

   def getVersion(self):
      print(self.__version)

   def setVersion(self, version):
      self.__version = version

obj = Robot()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()

class Car:

   def __init__(self):
      self.__updateSoftware()

   def drive(self):
      print('driving')

   def __updateSoftware(self):
      print('updating software')


redcar = Car()
redcar.drive()
redcar.__updateSoftware() #AttributeError: 'Car' object has no attribute '__updateSoftware'

