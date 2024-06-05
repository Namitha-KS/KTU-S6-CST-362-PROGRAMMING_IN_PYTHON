from abc import ABC, abstractmethod
class Parent(ABC):
    def common(self):
        print("I am the common of parent")
    @abstractmethod
    def vary(self):
        pass
class Child1(Parent):
    def vary(self):
        print("I am vary of child1")
class Child2(Parent):
    def vary(self):
        print("I am vary method of child2")
obj1 = Child1()
obj1.common()
obj1.vary()
obj2 = Child2()
obj2.common()
obj2.vary()