import numpy as np
from random import randint


X0 = np.ones([1000,1])
train = np.genfromtxt('train.txt', delimiter='\t')
train = np.append(X0 , train ,axis=1)
X = np.hsplit(train,[11])[0]  ## saparate the array into two part on the base of the nth column
Y = np.hsplit(train,[11])[1]
Wlin = np.dot(np.linalg.pinv(X) , Y)

E = np.dot(X , Wlin) - Y 
Einlin = 0
for i in range(len(E)):
    Einlin += (E[i][0]) ** 2/len(E)

n = 0.001
count = 0
times_avg = 0
while count < 1000:
    print(count)
    times = 0
    ratio = 100
    Wt = np.zeros([11,1])
    while ratio > 1.01: 
        rand = randint(0,999)
        E = np.dot(X , Wt) - Y 
        Einwt = 0
        for i in range(len(E)):
            Einwt += (E[i][0]) ** 2/len(E)
        x = X[rand].reshape((1,11))    # what the hell is it????

        Ein_grad = 2*(np.dot(x,Wt) - Y[rand][0]) * np.transpose(x)
        Wt = Wt- n*Ein_grad
        ratio = Einwt / Einlin
        times += 1

    times_avg += times/1000
    count += 1

print(times_avg)
    




