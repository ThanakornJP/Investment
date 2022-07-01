import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from re import sub
from decimal import Decimal
import json

def fetchInfo(ticker):
    
    headers = {
        'authority': 'api.nasdaq.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,th;q=0.8',
        'origin': 'https://www.nasdaq.com',
        'referer': 'https://www.nasdaq.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }

    params = {
        'assetclass': 'stocks',
    }

    try:
        response = requests.get('https://api.nasdaq.com/api/quote/' + ticker + '/info', params=params, headers=headers)        
        response_json = response.json()        
        info = response_json['data']
        

        #print(response_json_data.keys())
        #print(response_json_data['dividends'].keys())
        #print(response_json_data['dividends']['headers'])
        # print(response_json_data['dividends']['rows'])
        
        if info is not None and response_json['status']['rCode'] == 200:        
            return info
        else:
            return []
    except TypeError:
        return []

def fetchDetail(ticker):
    headers = {
        'authority': 'api.nasdaq.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,th;q=0.8',
        'origin': 'https://www.nasdaq.com',
        'referer': 'https://www.nasdaq.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    params = {
        'assetclass': 'stocks',
    }

    
    try:
        response = requests.get('https://api.nasdaq.com/api/quote/' + ticker + '/summary', params=params, headers=headers)
        
        response_json = response.json()        
        info = response_json['data']
        

        #print(response_json_data.keys())
        #print(response_json_data['dividends'].keys())
        #print(response_json_data['dividends']['headers'])
        # print(response_json_data['dividends']['rows'])
        
        if info is not None and response_json['status']['rCode'] == 200:        
            return info
        else:
            return []
    except TypeError:
        return []

def load(model):
    # return pd.read_csv('dividends.csv')    
    return pd.read_csv(model)        

def model(dividend_df): 
    name = []
    stock_type = []
    exchange = []
    industry = []
    sector = [] 
    share_volume = []
    trade_volume = []
    market_cap = []
    low_today = []
    high_today = []
    low_52 = []
    high_52 = []
    previous_close = []
    _pe = []
    _yield = []
    _eps = []
    _annualized_dividend = []
    

    _price_zone = [] # (last - low_52) / (high_52 - low_52)
    _dpr = [] # 
    _highest_yield = [] # low_52_dividend / low_52
    _target_price = [] # _yield / _highest_yield
    _zone1 = [] # _yield / (_highest_yield * 90%)
    _zone2 = [] # _yield / (_highest_yield * 80%)
    _money_trail = [] # 'good' if last - zone1 < 0; 'ok' if (last - zone1 > 0) and (last - zone2 < 0); otherwise 'bad'
    _price_trail = [] # 'good' if _price_zone < 40%; 'ok' if (_price_zone > 40%) and (_price_zone < 60%); otherwise 'bad'

    for index, row in dividend_df.iterrows():
        print(row['tick'])  

        data = fetchDetail(row['tick'])
        if len(data):
            exchange.append(data['summaryData']['Exchange']['value'])
            industry.append(data['summaryData']['Sector']['value'])
            sector.append(data['summaryData']['Industry']['value'])    

            #
            share_volume.append(int(data['summaryData']['ShareVolume']['value']))
            trade_volume.append(int(data['summaryData']['AverageVolume']['value']))
            market_cap.append(int(data['summaryData']['MarketCap']['value']))

            #
            #highlow_today.append(data['summaryData']['TodayHighLow']['value'])
            highlow_today = data['summaryData']['TodayHighLow']['value'].split("/")        
            low_today.append(float(Decimal(sub(r'[^\d.]', '', highlow_today[0]))))
            high_today.append(float(Decimal(sub(r'[^\d.]', '', highlow_today[1]))))
            
            #
            #highlow_52.append(data['summaryData']['FiftTwoWeekHighLow']['value'])
            highlow_52 = data['summaryData']['FiftTwoWeekHighLow']['value'].split("/")        
            low_52.append(float(Decimal(sub(r'[^\d.]', '', highlow_52[0]))))
            high_52.append(float(Decimal(sub(r'[^\d.]', '', highlow_52[1]))))
            
            #
            previous_close.append(float(Decimal(sub(r'[^\d.]', '', data['summaryData']['PreviousClose']['value']))))
            
            _pe.append(data['summaryData']['PERatio']['value'])
            _yield.append(data['summaryData']['Yield']['value'])
            
            #
            _eps.append(float(Decimal(sub(r'[^\d.]', '', data['summaryData']['EarningsPerShare']['value']))))

            #            
            _annualized_dividend.append(float(Decimal(sub(r'[^\d.]', '', data['summaryData']['AnnualizedDividend']['value']))))
            
        else:
            exchange.append("")
            industry.append("")
            sector.append("")        

            share_volume.append(0)
            trade_volume.append(0)
            market_cap.append(0)
            
            low_today.append(0.0)
            high_today.append(0.0)
            low_52.append(0.0)
            high_52.append(0.0)

            previous_close.append(0.0)
            _pe.append(0.0)
            _yield.append('0.0%')
            _eps.append(0.0)
            _annualized_dividend.append(0.0)

    dividend_df['exchange'] = exchange
    dividend_df['industry'] = industry
    dividend_df['sector'] = sector
    dividend_df['share_volume'] = share_volume
    dividend_df['trade_volume'] = trade_volume
    dividend_df['market_cap'] = market_cap
    dividend_df['highlow_today'] = highlow_today
    dividend_df['highlow_52'] = highlow_52
    dividend_df['previous_close'] = previous_close
    dividend_df['_pe'] = _pe
    dividend_df['_yield'] = _yield 
    dividend_df['_eps'] = _eps
    dividend_df['_annualized_dividend'] = _annualized_dividend

    return dividend_df

def save(df, model):
    df.to_csv(model)

def show():
    df = pd.read_csv('dividends_with_info.csv')
    print(df)

df = model(load('dividends.csv'))
save(df, 'dividends__info.csv')
show()





# def load():
#     dividend_df = pd.read_csv('dividends.csv')
    # print(dividend_df)
    # name = []
    # stock_type = []
    # exchange = []
    # industry = []
    # sector = [] 
    # share_volume = []
    # trade_volume = []
    # market_cap = []
    # highlow_today = []
    # highlow_52 = []
    # previous_close = []
    # _pe = []
    # _yield = []
    # _eps = []
    # _annualized_dividend = []


    # for index, row in dividend_df.iterrows():
    #     print(row['tick'])  
    #     # data = fetchInfo(row['tick'])
    #     # if len(data):
    #     #     name.append(data['companyName'])
    #     #     stock_type.append(data['stockType'])
    #     #     exchange.append(data['exchange'])
    #     # else:
    #     #     name.append("")
    #     #     stock_type.append("")
    #     #     exchange.append("")

    #     data = fetchDetail(row['tick'])
    #     if len(data):
    #         exchange.append(data['summaryData']['Exchange']['value'])
    #         industry.append(data['summaryData']['Sector']['value'])
    #         sector.append(data['summaryData']['Industry']['value'])    

    #         share_volume.append(data['summaryData']['ShareVolume']['value'])
    #         trade_volume.append(data['summaryData']['AverageVolume']['value'])
    #         market_cap.append(data['summaryData']['MarketCap']['value'])
    #         highlow_today.append(data['summaryData']['TodayHighLow']['value'])
    #         highlow_52.append(data['summaryData']['FiftTwoWeekHighLow']['value'])
    #         previous_close.append(data['summaryData']['PreviousClose']['value'])
    #         _pe.append(data['summaryData']['PERatio']['value'])
    #         _yield.append(data['summaryData']['Yield']['value'])
    #         _eps.append(data['summaryData']['EarningsPerShare']['value'])
    #         _annualized_dividend.append(data['summaryData']['AnnualizedDividend']['value'])


    #     else:
    #         exchange.append("")
    #         industry.append("")
    #         sector.append("")        

    #         share_volume.append("")
    #         trade_volume.append("")
    #         market_cap.append("")
    #         highlow_today.append("")
    #         highlow_52.append("")
    #         previous_close.append("")
    #         _pe.append("")
    #         _yield.append("")
    #         _eps.append("")
    #         _annualized_dividend.append("")




    # dividend_df['exchange'] = exchange
    # dividend_df['industry'] = industry
    # dividend_df['sector'] = sector
    # dividend_df['share_volume'] = share_volume
    # dividend_df['trade_volume'] = trade_volume
    # dividend_df['market_cap'] = market_cap
    # dividend_df['highlow_today'] = highlow_today
    # dividend_df['highlow_52'] = highlow_52
    # dividend_df['previous_close'] = previous_close
    # dividend_df['_pe'] = _pe
    # dividend_df['_yield'] = _yield 
    # dividend_df['_eps'] = _eps
    # dividend_df['_annualized_dividend'] = _annualized_dividend


    # dividend_df.to_csv('dividends_with_info.csv')
    # print(dividend_df)



# curl 'https://api.nasdaq.com/api/quote/AAPL/info?assetclass=stocks' \
#   -H 'authority: api.nasdaq.com' \
#   -H 'accept: application/json, text/plain, */*' \
#   -H 'accept-language: en-US,en;q=0.9,th;q=0.8' \
#   -H 'origin: https://www.nasdaq.com' \
#   -H 'referer: https://www.nasdaq.com/' \
#   -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-site' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36' \
#   --compressed
