import numpy as np


X0_train = np.ones([1000,1])
X0_test =np.ones([3000,1])
train = np.genfromtxt('train.txt', delimiter='\t')
test = np.genfromtxt('test.txt', delimiter='\t')
train = np.append(X0_train , train ,axis=1)
test = np.append(X0_test , test ,axis=1)

X_train = np.hsplit(train,[11])[0]  ## saparate the array into two part on the base of the nth column
Y_train = np.hsplit(train,[11])[1]
X_test = np.hsplit(test,[11])[0]  ## saparate the array into two part on the base of the nth column
Y_test = np.hsplit(test,[11])[1]
Wlin = np.dot(np.linalg.pinv(X_train) , Y_train)

def sign(s):
    if s >= 0:
        return 1
    else:
        return -1

E_train = np.dot(X_train , Wlin) * Y_train  # 
E_test = np.dot(X_test , Wlin) * Y_test
Ein = 0
Eout = 0
for i in range(1000):
    if sign(E_train[i]) == -1:
        Ein += 1/1000
    if sign(E_test[i]) == -1:
        Eout += 1/1000

print(Ein)
print(Eout)
print(abs(Ein-Eout))
    

        
