pip install --upgrade mplfinance

import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from pandas_datareader import data as pdr
import datetime as dt
style.use('ggplot')

df = pd.read_csv("C:/NVDA.csv", skiprows = [i for i in range (1,2768)]) 

#I have skipped the intial rows as I wanted to include the data from 2011. Then I created a new CSV file from the dataframe.

df.to_csv(r'C:/Users/vgupt/Desktop/NVDA.csv', index=False, header=True)

df = pd.read_csv('C:/Users/vgupt/Desktop/NVDA.csv', parse_dates = True, index_col=0)

#By default, date columns are represented as object when loading data from a CSV file. To read the date column correctly, we can use the argument parse_dates to specify a list of date columns

Manipulating Data¶

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum() #sum will give true values for volume and not the average volume

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #converting our dates into matplotlib date format
print(df_ohlc.head())

Output:
    Date       open       high        low      close
0  14977.0  14.536760  21.455963  14.490812  21.455963
1  14987.0  21.492723  21.676493  20.417622  20.417622
2  14997.0  22.724022  22.724022  21.832708  22.485113
3  15007.0  23.505075  23.587778  20.968952  21.566229
4  15017.0  21.235437  23.596966  20.720856  23.551016

#Creating a graph with matplotlib having multiple axis and visuals

x_axis = plt.subplot2grid((6,1),(0,0),rowspan=5, colspan=1)
y_axis = plt.subplot2grid((6,1),(5,0),rowspan=1, colspan=1, sharex=x_axis)

x_axis.xaxis_date()

candlestick_ohlc(x_axis, df_ohlc.values, width = 2, colorup='g')
y_axis.fill_between(df_volume.index.map(mdates.date2num), df_volume.values,0)

plt.show()

URL FOR GRAPH - https://user-images.githubusercontent.com/83883988/125545234-666f58c1-5bc3-4331-a36f-57e16e22b8c5.png
  
