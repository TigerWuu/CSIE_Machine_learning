from libsvm.python.svmutil import*
import numpy as np

train_y , train_x = svm_read_problem("satimage_train.txt")
W = np.zeros(36)
W_square = 0
W_norm = 0

for i in range(len(train_y)):
    if train_y[i] != 3:
        train_y[i] = -1
    else:
        train_y[i] = 1

model = svm_train(train_y , train_x ,"-c 10 -s 0 -t 0 -q")
nSV = model.get_nr_sv()
alpha = model.get_sv_coef()
SV = model.get_SV()

for i in range(nSV):
    X = np.zeros(36)
    for j in range(1,37):
        X[j-1] = SV[i].get(j,0)    
    W += alpha[i][0] * X       

for i in range(36):
    W_square += W[i] ** 2
W_norm = W_square ** 0.5
print(W_norm)


