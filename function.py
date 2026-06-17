# def Greet():
#     print("Hello Everyone")
# Greet()

# def greet():
#     print("Hello Customer")
# greet()

# def sum():
#     print("invalid")
# sum()

# def sum(x):
#     return x
# print (sum(3+2))

# name = "maryam"
# print(f"my name is {name}")


# def add(a,b):
#     """
#     This function adds two numbers.
#     """
#     return a+b
# print(add.__doc__)

# file =open("data.txt","r")
# print(file.read)
# file.close()

class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student Name:", self.name)

s1 = Student("Maryam")
s1.display()
