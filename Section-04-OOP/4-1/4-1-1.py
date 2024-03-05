# 1. what is class and object

# 2. property and method

# 3. define a class
class Person:

    # 4. how to initialize constructor with instance variables
    def __init__(self, name, age):
        # properties
        self.name = name
        self.age = age

    # method
    def greet(self):
        print("Hello, " + self.name)

# create an object of the class
person1 = Person("Ahmed", 20)
person1.greet()

