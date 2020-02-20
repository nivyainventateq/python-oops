# First  method
class P:
    def property(self):
        print('cash+land+gold')
    def marriage(self):
        print("Priya")
class C(P):
    pass
c=C()
c.property()
c.marriage()

# Second Method- method overrriding

#     def property(self):
#         print('cash+land+gold')
#     def marriage(self):
#         print("Priya")
# class C(P):
#     def marriage(self):
#         print("Shilpa")
# c=C()
# c.property()
# c.marriage()

# from the child if you wanna to call parent call super ()
#
# class P:
#     def property(self):
#         print('cash+land+gold')
#     def marriage(self):
#         print("Priya")
# class C(P):
#     def marriage(self):
#         super().marriage()
#         print("Shilpa")
# c=C()
# c.property()
# c.marriage()

class Robot:
    def action(self):
        print('Robot action')
class HelloRobot(Robot):
    def action(self):
        print('Hello world')

r = HelloRobot()
r.action()
