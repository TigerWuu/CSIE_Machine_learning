from libsvm.python.svmutil import*
import numpy as np

train_y , train_x = svm_read_problem("satimage_train.txt")
test_y , test_x = svm_read_problem("satimage_test.txt")

for i in range(len(train_y)):
    if train_y[i] != 6:
        train_y[i] = -1
    else:
        train_y[i] = 1
    if i < len(test_y):
        if test_y[i] != 6:
            test_y[i] = -1
        else:
            test_y[i] = 1

C = [0.01 , 0.1 , 1 , 10 , 100]
for c in C:
    model = svm_train(train_y , train_x , f"-c {c} -s 0 -t 2 -g 10 -q")
    p_labs, p_acc, p_vals = svm_predict(test_y, test_x, model)

    print(c , " E_out"," : " , 100-p_acc[0])


