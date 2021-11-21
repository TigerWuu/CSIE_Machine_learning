from numpy.random import uniform 

def sign(a):
    if a > 0:
        return 1
    else:
        return -1

times = 0
S = [-1 , 1]
s_best = 0
E_mean = 0
s_theta_plus = 0
data_set = 2

while times <= 10000:
    Ein_min = 100
    theta_best = 0
    X = uniform(-1,1,data_set)
    X.sort()
    for i in range(len(X)):
        if i >= len(X)-1:
            theta = -1
        else:
            theta = (X[i]+X[i+1])/2
        for s in S:
            err = 0 
            for j in X:
                f = sign(j) 
                h = s*sign(j - theta)
                if f != h:
                    err += 1
            Ein = err / len(X)
            if Ein < Ein_min:
                Ein_min = Ein
                theta_best = theta
                s_best = s
                s_theta_plus = s_best + theta_best
            elif Ein == Ein_min and (s + theta) <= s_theta_plus:
                theta_best = theta
                s_best = s
                s_theta_plus = s_best + theta_best
    if s_best == 1:
        Eout = abs(theta_best)/2
    else:
        Eout = (2-abs(theta_best))/2
    E_mean = E_mean + (Eout - Ein_min)/10000
    times += 1
print(E_mean)