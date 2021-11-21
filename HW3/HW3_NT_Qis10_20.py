import numpy as np


X0_train = np.ones([1000,1])
X0_test =np.ones([3000,1])

train = np.genfromtxt('train.txt', delimiter='\t')
X_train = np.hsplit(train,[10])[0]  ## saparate the array into two part on the base of the nth column
Y_train = np.hsplit(train,[10])[1]
test = np.genfromtxt('test.txt', delimiter='\t')
X_test = np.hsplit(test,[10])[0]  ## saparate the array into two part on the base of the nth column
Y_test = np.hsplit(test,[10])[1]

Q = 10
Z_train = X0_train 
Z_test = X0_test
for q in range(1,Q+1):
    Z_train2 = np.power(X_train , q)
    Z_test2 = np.power(X_test , q)
    Z_train = np.append(Z_train , Z_train2 ,axis = 1)
    Z_test = np.append(Z_test , Z_test2 ,axis = 1)
    
g = np.dot(np.linalg.pinv(Z_train) , Y_train)

def sign(s):
    if s >= 0:
        return 1
    else:
        return -1

E_train = np.dot(Z_train , g) * Y_train  # 
E_test = np.dot(Z_test , g) * Y_test
Ein = 0
Eout = 0
for i in range(1000):
    if sign(E_train[i]) == -1:
        Ein += 1/1000
for i in range(3000):
    if sign(E_test[i]) == -1:
        Eout += 1/3000

print(Ein)
print(Eout)

print(abs(Ein-Eout))