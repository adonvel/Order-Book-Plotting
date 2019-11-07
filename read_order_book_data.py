# +
''' file to read order book data'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# global variables
N_intervals = 10       # number of intervals between max and min price 

df_m = pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth10/AMZN_2012-06-21_34200000_57600000_message_10.csv',header=None)
df_o =  pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth10/AMZN_2012-06-21_34200000_57600000_orderbook_10.csv',header=None)


# +
t = df_m.values[: , 0]
t_steps = len(t)
prices = df_m.values[: , 4]
levels = len(df_o.values[i,0::4])
cumulative_vol_buy = np.zeros((levels,))
cumulative_vol_sell = np.zeros((levels,))

for i in range(20):
    buy_price = df_o.values[i,0::4]
    buy_amount = df_o.values[i,1::4]
    sell_price = df_o.values[i,2::4]
    sell_amount = df_o.values[i,3::4]
    
    for j in range(levels):
        cumulative_vol_buy[j] =  np.sum(buy_amount[0:j+1])
        cumulative_vol_sell[j] =  np.sum(sell_amount[0:j+1])
    
    plt.plot(buy_price,buy_amount)
    plt.plot(sell_price,sell_amount)
    plt.plot(buy_price,cumulative_vol_buy)
    plt.plot(sell_price,cumulative_vol_sell)
    plt.show()
    time.sleep(1)
    plt.clf()
    

sell_orders = np.zeros((N_intervals,t_steps))
buy_orders = np.zeros((N_intervals,len(t)))

# Set initial state
#for i in


# -
del time



