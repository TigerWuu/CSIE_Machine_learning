import numpy as np

a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
print(a.shape)
a = a.reshape((1,3))
print(a.shape)
print(b.shape)
c = np.dot(a,b)
d = np.dot(b,a)
print(c) 
print(d)

