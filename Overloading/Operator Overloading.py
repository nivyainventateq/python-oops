# class Book:
#     def __init__(self,x):
#         self.pages=x
# b1=Book(100)
# print(b1.__dict__)  #{'pages': 100}

# class Book:
#     def __init__(self,x):
#         self.pages=x
# b1=Book(100)
# b2=Book(200)
# print(b1+b2) #TypeError: unsupported operand type(s) for +: 'Book' and 'Book'

class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return self.pages+other.pages
    def __mul__(self, other):
        return self.pages*other.pages
b1=Book(100)
b2=Book(200)
print('The Total Number of Pages:',b1+b2)
print('The Total Number of Pages:',b1*b2)

# for single book object:

# class Book:
#     def __init__(self,x):
#         self.pages=x
#
#     def __str__(self):
#         return "The No of pages :" + str(self.pages)
#
#     def __add__(self, other):
#         total=self.pages+other.pages
#         b=Book(total)
#         return b
#
# b1=Book(100)
# b2=Book(200)
# b3=Book(300)
# b4=Book(400)
# print(b1+b2+b3+b4)

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __gt__(self,other):
#         return self.marks>other.marks
#     def __le__(self,other):
#         return self.marks<=other.marks
# # print("10>20 =",10>20)
# s1=Student("Durga",100)
# s2=Student("Ravi",200)
# print(s1>s2)
# print(s1<s2)
# print(s1<=s2)
# print(s1>=s2)


