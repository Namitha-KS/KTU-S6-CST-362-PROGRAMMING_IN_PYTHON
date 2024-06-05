'''Write a Python program to define a class Rectangle with
parameters height, width and member functions to find area,
and perimeter of it.'''

class Rectange:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def area(self):
        return (self.height*self.width)
    
    def perimeter(self):
        return (2*self.height*self.width)
    
r = Rectange(2,3)
print(r.area()) 
print(r.perimeter())