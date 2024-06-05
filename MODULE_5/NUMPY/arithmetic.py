import numpy as np
from numpy.linalg import inv,det

x = np.array([[1,2],[2,3]])
y = np.array([[4,3],[1,3]])

print(x+y)
print(x-y)
print(x*y) #element wise multiplication
print(x@y) #matrix multiplication
print(x.dot(y)) #matrix multiplication
print(x/y) #element wise division
print(x//y) #floor division
print(x%y) #modulus
print(x**y) #exponentiation
print(x.transpose()) #transpose
print(x)
print(y.transpose())
print(y)
print(inv(x))
print(det(y))


print(np.sin(0))