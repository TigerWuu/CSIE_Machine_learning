import numpy as np
import matplotlib.pyplot as plt
import tensorflow 
from tensorflow import keras



def hotel_meal(hotel , meal , train):
    dates = 0
    datas_sum = 0
    datas_sum_all = np.zeros((1,640))   # 640 days
    arrival_year = train["arrival_date_year"][0]
    arrival_month = train["arrival_date_month"][0]
    arrival_day = train["arrival_date_day_of_month"][0]
    num_data = len(train)

    for case in range(num_data):
        if train["is_canceled"][case] == 1:
            continue
        if train["arrival_date_year"][case] == arrival_year and train["arrival_date_month"][case] == arrival_month and train["arrival_date_day_of_month"][case] == arrival_day:
            if train["hotel"][case].decode("utf-8") == hotel and train["meal"][case].decode("utf-8") == meal:
                datas_sum += 1
        else:
            arrival_year = train["arrival_date_year"][case]
            arrival_month = train["arrival_date_month"][case]
            arrival_day = train["arrival_date_day_of_month"][case]
            datas_sum_all[0][dates] = datas_sum

            dates += 1
            datas_sum = 0
            if train["hotel"][case].decode("utf-8") == hotel and train["meal"][case].decode("utf-8") == meal:
                datas_sum += 1

    return datas_sum_all

def info_sum(data, train):
    dates = 0
    datas_sum = 0
    datas_sum_all = np.zeros((1,640))   # 640 days
    arrival_year = train["arrival_date_year"][0]
    arrival_month = train["arrival_date_month"][0]
    arrival_day = train["arrival_date_day_of_month"][0]
    num_data = len(train)
    for case in range(num_data):
        if train["is_canceled"][case] == 1:
            continue
        if train["arrival_date_year"][case] == arrival_year and train["arrival_date_month"][case] == arrival_month and train["arrival_date_day_of_month"][case] == arrival_day:
            datas = train[data][case]
            datas_sum += datas
        else:
            arrival_year = train["arrival_date_year"][case]
            arrival_month = train["arrival_date_month"][case]
            arrival_day = train["arrival_date_day_of_month"][case]
            datas_sum_all[0][dates] = datas_sum
            
            dates += 1
            datas = train[data][case]
            datas_sum = datas

    return datas_sum_all

if __name__ == "__main__":
    ## load the training data
    name = ['ID','hotel','is_canceled','lead_time','arrival_date_year'
    ,'arrival_date_month','arrival_date_week_number'
    ,'arrival_date_day_of_month','stays_in_weekend_nights'
    ,'stays_in_week_nights','adults','children','babies','meal','country'
    ,'market_segment','distribution_channel','is_repeated_guest'
    ,'previous_cancellations','previous_bookings_not_canceled'
    ,'reserved_room_type','assigned_room_type','booking_changes'
    ,'deposit_type','agent','company','days_in_waiting_list','customer_type'
    ,'adr','required_car_parking_spaces','total_of_special_requests'
    ,'reservation_status','reservation_status_date']
    train = np.genfromtxt("train.csv", delimiter=",", skip_header=1, dtype = None, names = name)
    label_train = np.genfromtxt("train_label.csv", delimiter=",", skip_header=1, dtype = None, names = "dates,revenue")


    hotel = ["Resort Hotel", "City Hotel"]
    meal = ["SC", "BB", "HB", "FB"]
    
    h_m = np.zeros((8,640))
    count = 0
    for i in range(len(hotel)):
        for j in range(len(meal)):
            h_m[count] = hotel_meal(hotel[i], meal[j] , train)
            count += 1

    adults = info_sum("adults",train)
    children = info_sum("children",train)
    babies = info_sum("babies",train)
    weekend_night = info_sum("stays_in_weekend_nights",train)
    week_night = info_sum("stays_in_week_nights",train)

    x_train = np.concatenate((h_m,week_night,weekend_night,adults,children,babies),axis = 0)
    label_train = label_train["revenue"].reshape((640,1))
    x_train = x_train.reshape((640,13))
    # x_train = x_train.astype(np.float32)
    # label_train = label_train.astype(np.float32)

    ## setting model

    model = keras.models.Sequential([
    keras.Input(shape=13),
    keras.layers.Dense(10, activation='sigmoid'),
    keras.layers.Dense(10, activation='sigmoid'),
    keras.layers.Dense(1, activation='linear')
    ])

    mse = keras.losses.MeanSquaredError()
    sgd = keras.optimizers.SGD()
    model.compile(loss=mse , optimizer=sgd , metrics= ["accuracy"])

    his = model.fit(x_train , label_train , epochs= 800,batch_size = 64 )
    plt.plot(his.history['loss'])
    plt.show()

    model.save("Final_1")


# for i in range(8):
#     plt.figure(i)
#     plt.plot(h_m[i])

# plt.show()


# adr_multi_day = 0
# adr_multi_day_sum = np.zeros(640)

# arrival_year = train["arrival_date_year"][0]
# arrival_month = train["arrival_date_month"][0]
# arrival_day = train["arrival_date_day_of_month"][0]
# dates = 0

# ##　the decision method of revenue ranking
# for case in range(len(train)):
#     if train["is_canceled"][case] == 1:
#         continue
#     if train["arrival_date_year"][case] == arrival_year and train["arrival_date_month"][case] == arrival_month and train["arrival_date_day_of_month"][case] == arrival_day:
#         adr = train["adr"][case]
#         total_days = train["stays_in_weekend_nights"][case] + train["stays_in_week_nights"][case] + 1
#         adr_multi_day += adr * total_days
#     else:
#         arrival_year = train["arrival_date_year"][case]
#         arrival_month = train["arrival_date_month"][case]
#         arrival_day = train["arrival_date_day_of_month"][case]
#         adr_multi_day_sum[dates] = adr_multi_day

#         dates += 1
#         adr = train["adr"][case]
#         total_days = train["stays_in_weekend_nights"][case] + train["stays_in_week_nights"][case] + 1
#         adr_multi_day = 0
#         adr_multi_day += adr * total_days