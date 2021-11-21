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
data_set = 20
tau = 0.1

while times <= 10000:
    X = []
    Ein_min = [100 , 100]
    Ein = [0 , 0]
    theta_best = [0 , 0]
    s_best = [0 , 0]
    s_theta_plus = [0 , 0]
    X = uniform(-1,1,data_set)
    X.sort()

    for ii in range(len(X)):

        if ii >= len(X)-1:
            theta = -1
        else:
            theta = (X[ii]+X[ii+1])/2

        for s in S:
            err = [0 , 0]
            Ein = [0 , 0] 
            for j in X:
                f = sign(j)
                h = s*sign(j - theta)
                if abs(j) <= tau:
                    if f != -h:
                        err[1] += 1
                    else:
                        err[0] += 1
                elif f != h:
                    err[0] += 1
                    err[1] += 1

            for i in range(2):
                Ein[i] = err[i] / len(X)
                if Ein[i] < Ein_min[i]:
                    Ein_min[i] = Ein[i]
                    theta_best[i] = theta
                    s_best[i] = s
                    s_theta_plus[i] = s_best[i] + theta_best[i]

                elif Ein[i] == Ein_min[i] and (s + theta) <= s_theta_plus[i]:
                    theta_best[i] = theta
                    s_best[i] = s
                    s_theta_plus[i] = s_best[i] + theta_best[i]

    if s_best[0] == 1:
        Eout = abs(theta_best[0])/2
    else:
        Eout = (2-abs(theta_best[0]))/2

    Eout_tau = Eout*(1-2*tau) + tau
    E_mean = E_mean + (Eout_tau - Ein_min[1])/10000
    times += 1
print(E_mean)