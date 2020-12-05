# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:44:28 2019

@author: Lenovo
"""
import datetime as dt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2001,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA','yahoo', start, end)
print(df.tail())