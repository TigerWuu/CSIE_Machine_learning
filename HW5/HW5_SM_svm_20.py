from libsvm.python.svmutil import*
import numpy as np
from random import randint

Gamma_choice = [0,0,0,0,0]
times = 0
while times < 1000:
    print(times)
    train_y , train_x = svm_read_problem("satimage_train.txt")
    valid_x = []
    valid_y = []
    ran = []
    i = 0
    while i < 200:
        rand = randint(0,4435)
        # if rand >= i:
        #     rand = rand - i
        if rand not in ran:
            valid_x.append(train_x[rand-i])
            valid_y.append(train_y[rand-i])
            train_x.remove(train_x[rand-i])
            train_y.remove(train_y[rand-i])
            ran.append(rand)
            i += 1
            
    for i in range(len(train_y)):
        if train_y[i] != 6:
            train_y[i] = -1
        else:
            train_y[i] = 1
        if i < len(valid_y):
            if valid_y[i] != 6:
                valid_y[i] = -1
            else:
                valid_y[i] = 1

    Gamma = [0.1 , 1 , 10 , 100 , 1000]
    for ga in Gamma:
        min_Eval = 100
        best_gamma = None
        model = svm_train(train_y , train_x , f"-c 0.1 -s 0 -t 2 -g {ga} -q")
        p_labs, p_acc, p_vals = svm_predict(valid_y, valid_x, model ,"-q")
        if (100-p_acc[0]) < min_Eval:
            best_gamma = ga
            min_Eval = p_acc[0]

    if best_gamma == 0.1:
        Gamma_choice[0] += 1 
    elif best_gamma == 1:
        Gamma_choice[1] += 1
    elif best_gamma == 10:
        Gamma_choice[2] += 1
    elif best_gamma == 100:
        Gamma_choice[3] += 1
    elif best_gamma == 1000:
        Gamma_choice[4] += 1
    times += 1

print(Gamma_choice)




