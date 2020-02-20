class Student:
    def __init__(self): # method 1
        self.name="Akash"
        self.age=23
        self.marks=80

    def talk(self):  # method 2
        print('Hello Myself:',self.name)
        print('My age is:',self.age)
        print('My marks is:',self.marks)
s=Student() # creating object in python
s.talk()  # calling the method


# class is a template it acts like blue print it doesnt point
# to one student so we sud print for more than one

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def talk(self):
        print('Hello Myself:',self.name)
        print('My age is:',self.age)
        print('My marks is:',self.marks)
s1=Student('Pavan',20,100)
s1.talk()
print('\n')
s2=Student('Priya',10,89)
s2.talk()

# blueprint for car
class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelarate(self):
        print("accelarating...")
#     "accelarator functionality here"

    def change_gear(self, gear_type):
        print("gear changed")
#     " gear related functionality here"

maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
maruthi_suzuki.start()
maruthi_suzuki.accelarate()
maruthi_suzuki.stop()
audi = Car("A6", "red", "audi", 80)
audi.start()
audi.accelarate()
audi.change_gear("low gear")