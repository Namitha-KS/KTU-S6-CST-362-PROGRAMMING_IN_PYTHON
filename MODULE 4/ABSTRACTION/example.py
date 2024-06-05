from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def getROI(self):
        pass
class SBI(Bank):
    def name(self):
        print("THIS IS SBI")
    def getROI(self):
        pass

class Branch(SBI):
    def branchname(self):
        print("THIS IS SBI DELHI BRANCH")
        
class HDFC(Bank):
    def name(self):
        print("THIS IS HDFC")
    def getROI(self):
        print("0.6%")
        
        
# b1 = Bank()
# b1.getROI()

b2 = SBI()
b2.name()
b2.getROI()

b3 = Branch()
b3.name()
b3.branchname()
b3.getROI()

b4 = HDFC()
b4.name()
b4.getROI()