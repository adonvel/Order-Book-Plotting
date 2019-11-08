# +
''' t_steps to read order book data'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import pylab as pl
from IPython import display

# global variables
N_intervals = 10       # number of intervals between max and min price 

df_m = pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth10/AMZN_2012-06-21_34200000_57600000_message_10.csv',header=None)
df_o =  pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth10/AMZN_2012-06-21_34200000_57600000_orderbook_10.csv',header=None)


# +
t = df_m.values[: , 0]
#t_steps = len(t)
prices = df_m.values[: , 4]
order_type = df_m.values[: , 1]


market_price = prices[np.where(order_type == 4) or np.where(order_type == 5)]/10000
time_price = t[np.where(order_type == 4) or np.where(order_type == 5)]/10000
plt.plot(time_price,market_price)


plt.plot(time_price,market_price)


# +
levels = len(df_o.values[0,0::4])
cumulative_vol_buy = np.zeros((levels,))
cumulative_vol_sell = np.zeros((levels,))


plt.Figure()
#axes.set_ylim([ymin,ymax])

for i in range(10000):
    buy_price = df_o.values[i,0::4]/10000
    buy_amount = df_o.values[i,1::4]
    sell_price = df_o.values[i,2::4]/10000
    sell_amount = df_o.values[i,3::4]
    
    for j in range(levels):
        cumulative_vol_buy[j] =  np.sum(buy_amount[0:j+1])
        cumulative_vol_sell[j] =  np.sum(sell_amount[0:j+1])
    
    
    #pl.plot(buy_price,buy_amount)
    #pl.plot(sell_price,sell_amount)
    axes = plt.gca()
    axes.set_xlim([np.amin(market_price),np.amax(market_price)])
    pl.plot(buy_price,cumulative_vol_buy)
    pl.plot(sell_price,cumulative_vol_sell)

    time.sleep(0.01)
    display.display(pl.gcf())
    display.clear_output(wait=True)  
    plt.clf()
    #plt.plot(buy_price,buy_amount)
    #plt.plot(sell_price,sell_amount)
#    plt.plot(buy_price,cumulative_vol_buy)
 #   plt.plot(sell_price,cumulative_vol_sell)   
  #  plt.clf()
   # plt.pause(0.2)
    #plt.show()



# -
del t_steps


