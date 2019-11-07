# +
''' file to read order book data'''

import pandas as pd

df = pd.read_csv(r'/home/learner/Order-Book-Plotting/AAPL_2012-06-21_34200000_37800000_message_50.csv',header=None)
print(type(df.values))
# -


