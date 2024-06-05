'''Define a class Student in Python with attributes to store
the roll number, name and marks of three subjects for each
student. Define the following methods:
readData()- to assign values to the attributes
computeTotal() – to find the total marks
print_details() - to display the attribute values and the total marks
Create an object of the class and invoke the methods.'''

class Student:
    def __init__(self, rollno, name, mark1, mark2, mark3):
        self.name = name
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def readData(self):
        print("ENTER DETAILS - ROLL NO, NAME, MARK1, MARK2, MARK3")
        self.rollno = int(input())
        self.name = input()
        self.mark1 = int(input())
        self.mark2 = int(input())
        self.mark3 = int(input())
        
    def computeTotal(self):
        self.total = self.mark1 + self.mark2 + self.mark3
        return self.total
    
    def print_details(self):
        print(f"ROLL NO : {self.rollno}\nNAME : {self.name}\nMARKS : {self.mark1}, {self.mark2}, {self.mark3}\nTOTAL : {self.total}")
        
s = Student(None, None, None, None, None)
s.readData()
s.computeTotal()
s.print_details()
        
        