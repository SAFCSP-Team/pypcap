# Class, Object, Properties, Methods
# 1. what is encapsulation

# 2. access modifiers (public, protected, private)
class Employee:

    def __init__(self, name, project, salary):
        self.name = name # public: access from anywhere
        self._project = project # protected: access within the class and its subclasses
        self.__salary = salary # private: access within the class only


class Department(Employee):

    def __init__(self, name, project, salary, dept):
        super().__init__(name, project, salary)
        self.dept = dept

    def getSal(self):
        print (self.__salary) # accessing private attribute of the parent class

    def getProject(self):
        print (self._project) # accessing protected attribute of the parent class
    def getName(self):
        print(self.name) # accessing public attribute of the parent class


emp1 = Department("Ahmed", "AI", 1000, "IT")
emp1.getName()
emp1.getProject()
# emp1.getSal() # Error: AttributeError: 'Department' object has no attribute '_Department__salary'