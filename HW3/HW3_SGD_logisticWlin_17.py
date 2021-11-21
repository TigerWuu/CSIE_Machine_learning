import numpy as np
from random import randint


X0 = np.ones([1000,1])
train = np.genfromtxt('train.txt', delimiter='\t')
train = np.append(X0 , train ,axis=1)
X = np.hsplit(train,[11])[0]  ## saparate the array into two part on the base of the nth column
Y = np.hsplit(train,[11])[1]
Wlin = np.dot(np.linalg.pinv(X) , Y)

def sigmoid(h):
    ans = 1/(1+np.exp(-h))
    return ans

n = 0.001
count = 0
Ein_avg = 0
while count < 1000:
    print(count)
    times = 0
    Wt = Wlin
    while times < 500: 
        rand = randint(0,999)
        x = X[rand].reshape((1,11))    # what the hell is it????
        Ein_grad = sigmoid(-Y[rand][0] * np.dot(x,Wt)) * Y[rand][0] * np.transpose(x)
        Wt = Wt + n*Ein_grad
        times += 1

    Einwt = 0
    for i in range(1000):
        x = X[i].reshape((1,11))
        CE_error = np.log(1+np.exp(-Y[i][0] * np.dot(x,Wt)[0][0]))
        Einwt += CE_error/1000
        
    Ein_avg += Einwt/1000
    count += 1

print(Ein_avg)