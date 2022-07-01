import yfinance as yf
import datetime 
import pandas as pd
# msft = yf.Ticker("MSFT")
# print(msft.info)
# print(msft.calendar)
# print(msft.earnings)
# hist = msft.history(period="max",interval="1wk")
# print(hist)


# data = yf.download("MSFT", period="max" start="2021-01-01", end="2021-12-31", interval="1wk")
data = yf.download("MSFT", period="max", interval="1wk")
data['Open'] = data['Open'].fillna(0)
data['High'] = data['High'].fillna(0)
data['Low'] = data['Low'].fillna(0)
data['Close'] = data['Close'].fillna(0)
# print(data)
# tble_data = {
#     '1':[],
#     '2':[],
#     '3':[],
#     '3':[],
# }
# tbl_close = pd.DataFrame(tble_data)
# print(tbl_close)


for row in data.itertuples():
    #print(datetime.datetime.strptime(row[0].split(' ')[0], "%Y-%m-%d").date().isocalendar()[1])
    print(row[0].isocalendar()[1], ' ', row[1], ' ', row[2], ' ')
    #tbl[row[0].isocalendar()[1]].append(row[1])

# for ind in data.index:
#     
    
#     # d = datetime.datetime.strptime(ind.split(' ')[0], "%Y-%m-%d").date()
#     y,wn,wd = ind.isocalendar()
#     print(y, '-', wn) 


#print(data.describe())

# for ind in data.index:
#     print(data['High'][ind], " ", data['Low'][ind])
    
#     d = float(data['High'][ind]) - float(data['Low'][ind])
#     print(d)
#     print(float(data['Low'][ind] + d))

#print(msft.info['industry'])
# print(msft.info['ebitdaMargins'])
# print(msft.info['profitMargins'])
# print(msft.info['grossMargins'])
#print(msft.info['revenueGrowth'])
#print(msft.info['earningsGrowth'])

# print('previousClose: ', msft.info['previousClose'])
# print('currentPrice: ', msft.info['currentPrice'])

# print('targetMeanPrice: ', msft.info['targetMeanPrice'])
# print('targetHighPrice: ', msft.info['targetHighPrice'])
# print('targetLowPrice: ', msft.info['targetLowPrice'])
# print('regularMarketDayLow: ', msft.info['regularMarketDayLow'])
# print('regularMarketDayHigh: ', msft.info['regularMarketDayHigh'])
# print('regularMarketPreviousClose: ', msft.info['regularMarketPreviousClose'])
# print('regularMarketPrice: ', msft.info['regularMarketPrice'])
# print('regularMarketOpen: ', msft.info['regularMarketOpen'])
# print('dayLow: ', msft.info['dayLow'])
# print('dayHigh: ', msft.info['dayHigh'])
# fiftyDayAverage

# print('fiftyTwoWeekHigh: ', msft.info['fiftyTwoWeekHigh'])
# print('fiftyTwoWeekLow: ', msft.info['fiftyTwoWeekLow'])



# print('bid: ', msft.info['bid'])
# print('ask: ', msft.info['ask'])
# print('askSize: ', msft.info['askSize'])
# print('bidSize: ', msft.info['bidSize'])


# print(': ', msft.info['']) 


#---

# lastDividendValue
# earningsQuarterlyGrowth
# priceToSalesTrailing12Months
# 
# twoHundredDayAverage
# trailingAnnualDividendYield
# payoutRatio
# averageDailyVolume10Day
# fiftyDayAverage
# averageVolume10days
# regularMarketVolume
# marketCap



# _price_zone = [] # (last - low_52) / (high_52 - low_52)
# _dpr = [] # 
# _highest_yield = [] # low_52_dividend / low_52
# _target_price = [] # _yield / _highest_yield
# _zone1 = [] # _yield / (_highest_yield * 90%)
# _zone2 = [] # _yield / (_highest_yield * 80%)
# _money_trail = [] # 'good' if last - zone1 < 0; 'ok' if (last - zone1 > 0) and (last - zone2 < 0); otherwise 'bad'
# _price_trail = [] # 'good' if _price_zone < 40%; 'ok' if (_price_zone > 40%) and (_price_zone < 60%); otherwise 'bad'
