class Fruit:
    def __init__(self,name):
        self.name = name
    def setFruitName(self, name):
        self.name = name
    def getFruitName(self):
        return self.name
f1 = Fruit("Apple")
print("First fruit name: ", f1.getFruitName())
f1.setFruitName("Grape")
print("Second fruit name: ", f1.getFruitName())