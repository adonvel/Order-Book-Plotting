# +
''' file to read order book data'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

""" global variables"""
N_intervals = 100       # number of intervals between max and min price 

df_m = pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth1/GOOG_2012-06-21_34200000_57600000_message_1.csv',header=None)
print(type(df.values))

time = df_m.values[: , 0]
prices = df_m.values[: , 4]
print(np.amax(prices))
print(np.amin(prices))

df_o =  pd.read_csv(r'/home/learner/Order-Book-Plotting/order_book_depth1/GOOG_2012-06-21_34200000_57600000_orderbook_1.csv',header=None)
#print(df_o([:: , :1]))

# -


