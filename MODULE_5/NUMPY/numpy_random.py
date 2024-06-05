import numpy as np

x = np.random.randint(100)
print(x)

y = np.random.randint(100, size=3)
print(y)

z = np.random.randint(100, size=(4,4))
print(z)

w = np.random.choice([3,5,6,7,9,2],size=(3,5))
print(w)