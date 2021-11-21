from liblinearutil import *
import numpy as np

def X_tranformation(X):
    X0 = np.ones([200,1])
    X_new = np.zeros([200,1])
    for k in range(len(X)):
        X_new[k] = np.append()
        for i in range(len(X)):
            for j in range(i,len(X)):
                print(X[k])
                print(X[k][i]*X[k][j])
                a = np.append(X[k],X[k][i]*X[k][j])
                X[k] = a 
                print(len(X[0]))
    X = np.append(X0 , X ,axis=1)
    return X



train3 = np.genfromtxt('hw4_train.txt', delimiter=' ')
X = np.hsplit(train3,[6])[0]  ## saparate the array into two part on the base of the nth column
Y = np.hsplit(train3,[6])[1]
Y = Y.reshape((1,200))
print(X)
X = X_tranformation(X)

# prob  = problem(Y[0], X)
# param = parameter('-s 0')
# m = train(prob, param)

