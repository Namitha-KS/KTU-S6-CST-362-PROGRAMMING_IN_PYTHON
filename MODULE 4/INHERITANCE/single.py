class Person:
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True
    
p = Person("Anu")
print(p.getName(), p.isEmployee())

e = Employee("Ammu")
print(e.getName(), e.isEmployee())