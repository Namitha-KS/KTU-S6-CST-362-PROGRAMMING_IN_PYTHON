'''Create a Student class and initialize it with name and roll
number.
Make methods to :
1. Display - Display all informations of the student.
2. setAge - Assign age to student
3. setTestMarks - Assign marks of a test to the student.'''


class Student:
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
    def display(self):
        print(f"NAME : {self.name}\nROOL NO. : {self.rollno}")
        if self.age is not None:
            print(f"AGE : {self.age}")
        if self.testmark is not None:
            print(f"TEST MARKS : {self.testmark}")
            
    def set_age(self, age):
        self.age = age
        
    def setTestMarks(self, testmark):
        self.testmark = testmark
        
s = Student("John", 101)
s.set_age(17)
s.setTestMarks(98)
s.display()
