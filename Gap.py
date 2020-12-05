# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:44:28 2019

@author: Lenovo
"""
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import style

pd.options.mode.chained_assignment = None

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300) # create the canvas
canvas1.pack()
  
entry1 = tk.Entry (root) # create the entry box
canvas1.create_window(150, 100, window=entry1)
  
def insert_number(): # add a function/command to be called by the button (i.e., button1 below)
    global x1 # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed 
    x1 = str(entry1.get()) # store the data input by the user as a variable x1 


 
button1 = tk.Button (root, text='Input stock Ticker (XXXX) ',command=insert_number, bg='blue', fg='white') # button to call the 'insertnumber' command above 
canvas1.create_window(150, 140, window=button1)

 
root.mainloop()

start = dt.datetime(2001,1,1)
end = dt.datetime.now()
df = web.DataReader(f'{x1}','yahoo', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)



# first add the name of the header (high and low) to your dataframe if it does not have one by:
df.columns = ["High", "Low", "Open", "Close", "Volume", "Adj Close"]
# This is an empty column which is called compare and is added to the last column of your data frame.We will fill
# this column with true (if the high < low) and false later in the for loop.
df['compare'] = '' 

for x in np.arange(len(df.index)-1):
    if df.High[x] < df.Low[x+1]:
        df.compare[x] = True
    else:
        df.compare[x] = False

# because the last cell will be empty I just assign zero to it. 
df.compare.iloc[[-1]] = 0

print (df)

style.use('ggplot')


df.to_csv('stock.csv')
df = pd.read_csv('stock.csv', parse_dates=True, index_col=0)

df[['High','Low']].plot()
plt.show()


df