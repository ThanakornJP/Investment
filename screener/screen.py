import urllib, json
import requests
import pylab
import plotly.offline as pyo 
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr 
import yfinance as yf
from yahoo_fin import stock_info as si 
import numpy as np

def getTickers():
    df1 = pd.DataFrame(si.tickers_sp500())
    df2 = pd.DataFrame(si.tickers_nasdaq())
    print('all S&P500')
    print(df1)
    print('all NASDAQ')
    print(df2)

    sym1 = set( symbol for symbol in df1[0].values.tolist())
    sym2 = set( symbol for symbol in df2[0].values.tolist())
    symbols = set.union(sym1,sym2)
    del_set = set()
    sav_set = set()
    my_list = ['W','R','P','Q']
    for symbol in symbols:
        if len(symbol) > 4 and symbol[-1] in my_list:
            del_set.add(symbol)
        else:
            sav_set.add(symbol)

    print(f'Removed {len(del_set)} unqualified stock')
    print('All qualified S&P and NASDAQ')
    print(sav_set)

def getAllEarnings(ticker):
    all_earnings = si.get_earnings_history(ticker)
    earnings = pd.DataFrame(all_earnings)
    print(earnings)

def getAllDividends(ticker):
    all_dividends = si.get_dividends(ticker)
    dividends = pd.DataFrame(all_dividends)
    print(dividends.index)
    dividends.to_csv('dividend_analysis.csv', encoding='utf-8')
    inds = dividends['dividend'].index[dividends['dividend'].apply(np.isnan)] 
    print(inds)


getAllDividends('AAPL')




# Sample plot 1
#plt.plot([1,2,3])
#plt.show()

# Sample plot 2
#df = pd.DataFrame({
#    'name':['john','mary','peter','jeff','bill','lisa','jose'],
#    'age':[23,78,22,19,45,33,20],
#    'gender':['M','F','M','M','M','F','M'],
#    'state':['california','dc','california','dc','california','texas','texas'],
#    'num_children':[2,0,0,3,2,1,4],
#    'num_pets':[5,1,0,5,2,2,3]
#})
#df.plot(kind='scatter',x="num_children", y='num_pets', color='red')
#plt.show()
#df.plot(kind='bar',x='name',y='age')
#plt.show()

#msft = yf.Ticker("MSFT")
#print(msft.info)
#data = msft.info
#print(msft.earnings)
#print(msft.get_financials())

end = dt.datetime.now()
start = end - dt.timedelta(days=5000)
print(start)
print(end)

#
#stocklist = ['AAPL','TSLA','MSFT']
#stocks = [i + '' for i in stocklist]
#stocks

#df = pdr.get_data_yahoo(stocks, start,end)
#print(df.head())
#print(df.index)
#print(df.columns)

#Close = df.Close
#print(Close.head())
#print(Close.describe(percentiles=[0.1,0.5,0.9]))
#print(Close[Close.index > end - dt.timedelta(days=100)].describe(percentiles=[0.1,0.5,0.9]))
#df.to_csv('close_analysis.csv', encoding='utf-8')
# plot



#Close.plot()

#pd.options.plotting.backend = 'plotly'
#plt.plot(Close)
#pyo.show()


#Close['MSFT'].pct_change().plot(kind='hist')





#url = "https://eodhistoricaldata.com/api/eod/AAPL.US?api_token=62ad732d92c4b1.07282612&order=d&fmt=json"

#url = "https://eodhistoricaldata.com/api/fundamentals/AAPL.US?api_token=62ad732d92c4b1.07282612&fmt=json"
#response = urllib.urlopen(url)
#data = json.loads(response.read())
#print(data)




# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
#url = 'https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey=demo'
#r = requests.get(url)
#data = r.json()

#print(data)