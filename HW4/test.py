import numpy as np
from liblinearutil import *



# a = np.array([[1, 2,3] , [3,4,5]])
# a = list(a)
# #a = [[1, 2,3] , [3,4,5]]
# print(a)


# y = [1,-1]
# x = [[1,0,1],[ -1,0,-1]]
# print(len(y))
# print(type(y))
# print(len(x))
# print(type(x))


# prob  = problem(y, x)
# param = parameter('-s 0')
# m = train(prob, param)
x0 = np.array([4,1])
X = np.array([[1],[2],[3],[4]])
y = np.array([[4],[5],[6],[7]])
z = X*y
z.append(x0)
print(z)