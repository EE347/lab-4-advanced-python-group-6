import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

dates = []
meta_price = []
aapl_price = []
amzn_price = []
nflx_price = []
nvda_price = []
googl_price = []

with open('task9.csv') as f:
    f.readline()
    for line in f.readlines():
        date, META, AAPL, AMZN, NFLX, NVDA, GOOGL = line.split(',')
        dates.append(datetime.strptime(date, '%d/%m/%Y'))
        meta_price.append(float(META))
        aapl_price.append(float(AAPL))
        amzn_price.append(float(AMZN))
        nflx_price.append(float(NFLX))
        nvda_price.append(float(NVDA))
        googl_price.append(float(GOOGL))
 
plt.title("FAANG Performance")
plt.plot(dates, meta_price, color='blue', label='META')
plt.plot(dates, aapl_price, color='gray', label='AAPL')
plt.plot(dates, amzn_price, color='black', label='AMZN')
plt.plot(dates, nflx_price, color='red', label='NFLX')
plt.plot(dates, nvda_price, color='green', label='NVDA')
plt.plot(dates, googl_price, color='gold', label='GOOGL')
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")

plt.legend(loc='upper left')
plt.show()