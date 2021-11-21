from libsvm.python.svmutil import*
import numpy as np

choice = range(1,6)
for number in choice:
    train_y , train_x = svm_read_problem("satimage_train.txt")

    W = np.zeros(36)
    W_square = 0
    W_norm = 0

    for i in range(len(train_y)):
        if train_y[i] != number:
            train_y[i] = -1
        else:
            train_y[i] = 1

    model = svm_train(train_y , train_x ,"-c 10 -s 0 -t 1 -d 2 -q")
    p_labs, p_acc, p_vals = svm_predict(train_y, train_x, model)

    print(number," versus not ", number , " : " , 100-p_acc[0])


