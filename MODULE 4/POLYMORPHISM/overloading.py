'''
## Overloading in Python

While Python doesn't support overloading in the same way as some other languages (like C++ or Java), it achieves similar functionality through other mechanisms:

**1. Operator Overloading (Limited):**

Python offers limited operator overloading capabilities. You can redefine the behavior of certain operators for custom classes using special methods named after the operators (e.g., `__add__` for +, `__sub__` for -, etc.).

**Example:**
'''
class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Overloading the + operator for vector addition
  def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses the overloaded + operator

print(v3.x, v3.y)  # Output: 4 6

'''

**2. Method Overloading (Alternative):**

If 2 methods have same name but different type of arguments, then those methods are saod to be overloaded methods.
'''
class Demo:
    def show(self):
        print("No Argument")
    def show(self, a, b):
        print("Two Arguments")
    def show(self, a):
      print("One Arguments")

obj = Demo()
# obj.show()
obj.show(10)
# obj.show(10,20)


'''**3. Constructor Overloading:**

Python allows you to define multiple constructors (methods named `__init__`) with different parameter lists for object initialization.

**Example:**'''

# class Point:
#   def __init__(self, x=0, y=0):  # Default values for x and y
#     self.x = x
#     self.y = y

# p1 = Point()  # Uses default values (0, 0)
# p2 = Point(5)  # Uses constructor with one parameter
# p3 = Point(3, 4)  # Uses constructor with two parameters

class Demo:
    def __init__(self):
        print("No Argument")
    def __init__(self, a, b):
        print("Two Arguments")
    def __init__(self, a):
      print("One Arguments")

obj = Demo(10)

'''**Key Points:**

- Python relies on special method names (like `__add__`) for operator overloading.
- Use descriptive method names for method overloading alternatives.
- Multiple constructors provide flexibility in object initialization.

**Remember:**

- Overloading in Python is not as extensive as in some other languages.
- Use these techniques judiciously to maintain code clarity.
'''