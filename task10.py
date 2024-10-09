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
 
meta_percent = meta_price[-1] / meta_price[0] * 100
aapl_percent = aapl_price[-1] / aapl_price[0] * 100
amzn_percent = amzn_price[-1] / amzn_price[0] * 100
nflx_percent = nflx_price[-1] / nflx_price[0] * 100
nvda_percent = nvda_price[-1] / nvda_price[0] * 100
googl_percent = googl_price[-1] / googl_price[0] * 100

plt.title("FAANG Performance")
plt.plot(dates, meta_price, color='blue', label=f'META +{meta_percent:.2f}%')
plt.plot(dates, aapl_price, color='gray', label=f'AAPL +{aapl_percent:.2f}%')
plt.plot(dates, amzn_price, color='black', label=f'AMZN +{amzn_percent:.2f}%')
plt.plot(dates, nflx_price, color='red', label=f'NFLX +{nflx_percent:.2f}%')
plt.plot(dates, nvda_price, color='green', label=f'NVDA +{nvda_percent:.2f}%')
plt.plot(dates, googl_price, color='gold', label=f'GOOGL +{googl_percent:.2f}%')
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")

plt.legend(loc='upper left')
plt.show()