## INHERITANCE

Inheritance in Python allows classes to inherit attributes and methods from other classes. Here, we'll cover the different types of inheritance and related concepts like method overloading and overriding.

### Basic Inheritance
Basic inheritance involves a child class inheriting from a single parent class.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof!
```

### Method Overloading (Not directly supported in Python)
Python does not support method overloading like some other languages (e.g., Java). Instead, you can use default parameters or variable-length arguments to achieve similar functionality.

```python
class Math:
    def add(self, a, b, c=0):
        return a + b + c

math = Math()
print(math.add(1, 2))    # Output: 3
print(math.add(1, 2, 3)) # Output: 6
```

### Method Overriding
Method overriding allows a child class to provide a specific implementation of a method already defined in its parent class.

```python
class Animal:
    def speak(self):
        return "I am an animal"

class Dog(Animal):
    def speak(self):
        return "Woof!"

animal = Animal()
dog = Dog()
print(animal.speak()) # Output: I am an animal
print(dog.speak())    # Output: Woof!
```

### Single Inheritance
Single inheritance involves one class inheriting from another single class.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")

child = Child()
child.show()    # Output: Parent class
child.display() # Output: Child class
```

### Multiple Inheritance
Multiple inheritance involves a class inheriting from more than one parent class.

```python
class Father:
    def show_father(self):
        print("Father class")

class Mother:
    def show_mother(self):
        print("Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("Child class")

child = Child()
child.show_father() # Output: Father class
child.show_mother() # Output: Mother class
child.show_child()  # Output: Child class
```

### Multilevel Inheritance
Multilevel inheritance involves a chain of inheritance where a class is derived from another class, which in turn is derived from another class.

```python
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent class")

class Child(Parent):
    def show_child(self):
        print("Child class")

child = Child()
child.show_grandparent() # Output: Grandparent class
child.show_parent()      # Output: Parent class
child.show_child()       # Output: Child class
```

### Hierarchical Inheritance
Hierarchical inheritance involves multiple classes inheriting from a single parent class.

```python
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def show_child1(self):
        print("Child1 class")

class Child2(Parent):
    def show_child2(self):
        print("Child2 class")

child1 = Child1()
child2 = Child2()
child1.show()       # Output: Parent class
child1.show_child1()# Output: Child1 class
child2.show()       # Output: Parent class
child2.show_child2()# Output: Child2 class
```

### Hybrid Inheritance
Hybrid inheritance is a combination of two or more types of inheritance. This can create complex inheritance structures.

```python
class Grandparent:
    def show_grandparent(self):
        print("Grandparent class")

class Parent1(Grandparent):
    def show_parent1(self):
        print("Parent1 class")

class Parent2(Grandparent):
    def show_parent2(self):
        print("Parent2 class")

class Child(Parent1, Parent2):
    def show_child(self):
        print("Child class")

child = Child()
child.show_grandparent() # Output: Grandparent class
child.show_parent1()     # Output: Parent1 class
child.show_parent2()     # Output: Parent2 class
child.show_child()       # Output: Child class
```

These examples illustrate the various types of inheritance and the concepts of method overloading and overriding in Python.

co-authored by GPT4o
