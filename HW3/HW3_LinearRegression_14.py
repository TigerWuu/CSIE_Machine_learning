import numpy as np

X0 = np.ones([1000,1])
train = np.genfromtxt('train.txt', delimiter='\t')
train = np.append(X0 , train ,axis=1)
X = np.hsplit(train,[11])[0]  ## saparate the array into two part on the base of the nth column
Y = np.hsplit(train,[11])[1]
Wlin = np.dot(np.linalg.pinv(X) , Y)

E = np.dot(X , Wlin) - Y
print(E)
Ein = 0
for i in range(len(E)):
    Ein += (E[i][0]) ** 2/len(E)

print(Ein)

        
