import numpy as np

x = np.random.randint(100)
print(x)

y = np.random.randint(100, size=3)
print(y)

z = np.random.randint(100, size=(4,4))
print(z)

w = np.random.choice([3,5,6,7,9,2],size=(3,5))
print(w)

'''Write a python program to create two numpy arrays of random integers between 
0 and 20 of shape (3, 3) and perform matrix addition, multiplication and transpose 
of the product matrix.'''

a = np.random.randint(0,20, size=(3,3))
b = np.random.randint(0,20, size=(3,3))

add = a+b
print(add)

mul = a@b
print(mul)

print(a.transpose())
print(b.transpose())