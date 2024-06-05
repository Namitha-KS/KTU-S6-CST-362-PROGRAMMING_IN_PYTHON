'''
Write a Python
program to express the instances as return values to define
a class RECTANGLE with parameters height, width,
corner_x, and corner_y and member functions to find center,
area, and perimeter of an instance
'''


class Rectangle:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x
        self.corner_y = corner_y
        
    def find_center(self):
        center_x = self.corner_x + self.width/2
        center_y = self.corner_y + self.height/2
        return center_x, center_y
    
    def are(self):
        return (self.height*self.width)
    
    def perimeter(self):
        return (2*self.height*self.width)
    
r = Rectangle(10, 5, 0, 0)
print(r.find_center(), r.are(), r.perimeter())