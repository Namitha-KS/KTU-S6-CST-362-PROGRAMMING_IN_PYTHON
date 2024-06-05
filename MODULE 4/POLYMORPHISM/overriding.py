'''In Python, method overriding and constructor overriding are not directly achievable in the traditional sense like some other object-oriented languages (e.g., Java or C++). However, Python offers alternative mechanisms to achieve similar behavior:

**Method Overriding (Alternative):**

Python doesn't allow methods with the same name but different parameter lists within a class hierarchy. Instead, you can achieve a similar effect through polymorphism using inheritance and method names that indicate their purpose:

**Example:**'''

class P:
  def properties_status(self):
    print('Money,Land,Gold')
  def to_marry(self):
    print('OYSTER')
    
class C(P):
  def to_study(self):
    print('LOOKING FOR OPPORTUNITIES')
  def to_marry(self):
    print('CRAB')

obj = C()
obj.properties_status()
obj.to_marry()
obj.to_study()


'''
Constructor Overriding

If child class does not have a constructor, then the parent class constructor will be executed at the time of child class object creation.
From child class constructor parent class constructor can be invoked by using super() method.


If a child class has a constructor, then child class constructor will be executed at the time of child class object creation.
'''

class Person:
  def __init__(self, name, age):
    self.name = name 
    self.age = age
    
class Employee(Person):
  def __init__(self, name, age, eno, esal):
    super().__init__(name, age)
    self.eno = eno
    self.esal = esal
  def show(self):
    print('Employee Name:', self.name)
    print('Employee Age:', self.age)
    print('Employee Number:', self.eno)
    print('Employee Salary:', self.esal)
  
e1 = Employee('Namitha', 20, 1234, 5678)
e1.show()
e2 = Employee('Shivani', 21, 4321, 8765)
e2.show()