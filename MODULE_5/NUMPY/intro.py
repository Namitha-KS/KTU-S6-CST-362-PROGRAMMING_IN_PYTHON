import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print("Value of a is\n",a,"\n") 

b = np.array([(1,2,3),(4,5,6)], dtype = float)
print("Value of b is\n",b,"\n")

c = np.array([(1,2,3),(4,5,6),(7,8,9),(1,1,4)], dtype='U32')
print("Value of c is\n",c,"\n")

# ATTRIBUTES
print(b.shape)
print(c.ndim)
print(a.size)
print(c.dtype)
print(c.itemsize)
print(a.itemsize)

# INDEXING
print(a[-2])
print(b[1,2])

# SLICING
print(a[0:2])
print(a[-6:-1])
print(a[1:6:2])
# print('enter values : ')
# m = int(input())
# n = int(input())
# print(a[m:n:-1])
print(a[::-1])

print(c[1, :])
print(c[: ,1])
print(c[1:3, 1:3])