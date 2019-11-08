# +
# Import necessary packages-----------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import pylab as pl
from IPython import display

# Save data in DATAFRAME--------------------------------------------------------------

df_m = pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth30/MSFT_2012-06-21_34200000_37800000_message_30.csv',header=None)
df_o =  pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth30/MSFT_2012-06-21_34200000_37800000_orderbook_30.csv',header=None)


# +
#Plot price evolution-----------------------------------------------------------------

t = df_m.values[: , 0]
t_steps = len(t)
prices = df_m.values[: , 4]
order_type = df_m.values[: , 1]
w=10


market_price = prices[np.where(order_type == 4) or np.where(order_type == 5)]/10000
time_price = t[np.where(order_type == 4) or np.where(order_type == 5)]

for k in range(1000):
    plt.clf()
    axes = plt.gca()
    plt.title('Evolution of Microsoft stock', size=16)
    plt.ylabel('Price (USD)')
    plt.xlabel('Time (minutes after 9:30)')
    pl.plot((time_price[0:1000+w*k]-34000)/60,market_price[0:1000+w*k])

    display.display(pl.gcf())
    display.clear_output(wait=True)  
    


# +
#Plot order book cumulative order depth----------------------------------------

levels = len(df_o.values[0,0::4])
t_steps = len(t)
cumulative_vol_buy = np.zeros((levels,))
cumulative_vol_sell = np.zeros((levels,))
v = 500


plt.Figure()

for i in range(1000):
    
    #Load data in arrays
    
    plt.clf()
    buy_price = df_o.values[v*i,0::4]/10000
    buy_amount = df_o.values[v*i,1::4]
    sell_price = df_o.values[v*i,2::4]/10000
    sell_amount = df_o.values[v*i,3::4]
    
    #Integrate to obtain the cumulative order depth
    
    for j in range(levels):
        cumulative_vol_buy[j] =  np.sum(buy_amount[0:j+1])
        cumulative_vol_sell[j] =  np.sum(sell_amount[0:j+1])
    
    #Plot
    axes = plt.gca()
    axes.set_xlim([0.995*np.amin(market_price),1.005*np.amax(market_price)])
    axes.set_ylim([0,350000])
    plt.title('Order book evolution',size=16)
    plt.ylabel('Cumulative order depth (shares $\cdot $ USD) ')
    plt.xlabel('Price (USD)')
    pl.plot(buy_price,cumulative_vol_buy,label = 'Buy orders')
    pl.plot(sell_price,cumulative_vol_sell, label = 'Sell orders')
    plt.legend()
    # textstr = '\n'.join(('text'))
    # pl.text(0, 0, textstr)
    
    time.sleep(0.001)
    display.display(pl.gcf())
    display.clear_output(wait=True)  


# -



