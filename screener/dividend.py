import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from re import sub
from decimal import Decimal
import json
import math

def getDividends(ticker):
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
        response = requests.get('https://api.nasdaq.com/api/quote/' + ticker + '/dividends', params=params, headers=headers)
        response_json = response.json()
        #print(response_json)
        #print()
        #print(response_json.keys())
        #print(response_json['message'])
        #print(response_json['status'])
        #print(response_json['data'])
        #print()
        response_json_data = response_json['data']
        

        #print(response_json_data.keys())
        #print(response_json_data['dividends'].keys())
        #print(response_json_data['dividends']['headers'])
        # print(response_json_data['dividends']['rows'])
        
        dividends = response_json_data['dividends']['rows']
        if dividends is not None:        
            return dividends
        else:
            return []
    except TypeError:
        return []

def load(model):    
    with open(model, 'r') as f:
        return f.readlines()

def model(tickers):
    dividend_table = {
        'tick':[], 
        'num_streak':[], 
        'streak_start_date':[],
        'streak_end_date':[],
        'payout_period':[],
        'lastest_amount':[],
        'incremental_percentage':[],        
        'number_survive_proof':[],
        'latest_survive_streak':[],
        'number_survive_years':[]
    }

    recession = [1953,1958,1960,1970,1973,1980,1990,2001,2008,2020]

    for ticker in tickers:
        dividends = getDividends(ticker.strip())    
        
        if len(dividends) < 1:        
            print("Skip " + ticker.strip() + "!")
        else:
            print("Analyzing " + ticker.strip() + " ....")
            d_lines = { 'date':[],'year':[], 'payout_period':[],'amount':[],'incremental_percentage': [] }
            
            # survive_years = from the 1st time they paid off up until now
            survive_years = 0
            if dividends[-1]['exOrEffDate'] != "N/A":
                survive_years = int(datetime.now().year) - int(datetime.strptime(dividends[-1]['exOrEffDate'],  "%m/%d/%Y").year)

            #for index, dividend in enumerate(dividends[:-1]):               
            for index, dividend in enumerate(dividends):                 
                if dividend['exOrEffDate'] == "N/A" or  dividend['amount'] == "": continue 
                    
                d = datetime.strptime(dividend['exOrEffDate'],  "%m/%d/%Y")                
                amount = float(Decimal(sub(r'[^\d.]', '', dividend['amount'])))

                if index == len(dividends)-1:                                    
                    previous_d = d
                    previous_amount = amount
                else:
                    if dividends[index+1]['exOrEffDate'] == "N/A" or dividends[index+1]['amount'] == "": 
                        previous_d = d
                        previous_amount = amount
                    else:
                        previous_d = datetime.strptime(dividends[index+1]['exOrEffDate'],  "%m/%d/%Y") 
                        previous_amount = float(Decimal(sub(r'[^\d.]', '', dividends[index+1]['amount'])))        

                if amount == 0 or previous_amount == 0: continue

                inc_step = (amount * 100 / previous_amount) - 100
                num_months = abs((previous_d.year - d.year) * 12 + (previous_d.month - d.month))
                # print('no month : ' + str(num_months))
                if num_months > 4: break   

                d_lines['date'].append(d.strftime("%m/%d/%Y"))
                d_lines['year'].append(int(d.strftime("%Y")))
                d_lines['payout_period'].append(num_months)
                d_lines['amount'].append(amount)
                d_lines['incremental_percentage'].append(inc_step)


            if len(d_lines['date']) > 0:
                dividend_table['tick'].append(ticker.strip())
                dividend_table['streak_end_date'].append(datetime.strptime(dividends[0]['exOrEffDate'],  "%m/%d/%Y").strftime("%m/%d/%Y"))     
                
                # convert
                if dividends[0]['amount'].replace('$','') == '':
                    dividend_table['lastest_amount'].append(0.0)
                else:
                    dividend_table['lastest_amount'].append(float(Decimal(sub(r'[^\d.]', '', dividends[0]['amount']))))

                dividend_table['streak_start_date'].append(d_lines['date'][-1]) 
                dividend_table['num_streak'].append(len(d_lines['date']))
                dividend_table['incremental_percentage'].append(max(d_lines['incremental_percentage']))
                dividend_table['payout_period'].append(sum(d_lines['payout_period'])/len(d_lines['payout_period']))
                            
                # how many recessive year they paid off
                recession_proof = set(d_lines['year']) & set(recession)                                
                dividend_table['number_survive_proof'].append(len(recession_proof))

                #print('recession_survive ... ')   
                first_year_payout = min(d_lines['year'])                
                recession_survive = 0                
                # for index, r_year in enumerate(recession):
                #     if first_year_payout < r_year:
                #         recession_survive = len(recession) - index                                         
                #         break        

                #dividend_table['no_survive'].append(recession_survive)

                # when is the latest streak they paid off during recession
                dividend_table['latest_survive_streak'].append(first_year_payout)

                # how many years they've gone thru 
                dividend_table['number_survive_years'].append(survive_years)                

            d_lines = {}
            # print(dividend_table)
        
    return pd.DataFrame(dividend_table)

def save(df, model):
    # df.to_csv('dividends_with_info.csv')
    df.to_csv(model)


def reload():
    # --- NASDAQ ---
    df1 = model(load('tick.nasdaq.csv.1'))
    df2 = model(load('tick.nasdaq.csv.2'))
    df3 = model(load('tick.nasdaq.csv.3'))
    df4 = model(load('tick.nasdaq.csv.4'))
    df = pd.concat([df1, df2, df3, df4], ignore_index=True)
    save(df,'dividends.nasdaq.csv')

    # --- S&P 500 ---
    #df = model(load('tick.snp.csv'))
    #save(df,'dividends.snp.csv')


# def getTickers(index):
#     #lines = object()
#     with open('ticker.txt.'+ str(index), 'r') as f:
#         return f.readlines()

# def decode(lines):
#     dividend_table = {
#         'tick':[], 
#         'num_streak':[], 
#         'streak_start_date':[],
#         'streak_end_date':[],
#         'payout_period':[],
#         'lastest_amount':[],
#         'incremental_percentage':[],        
#         'number_survive_proof':[],
#         'latest_survive_streak':[],
#         'number_survive_years':[]
#     }

#     recession = [1953,1958,1960,1970,1973,1980,1990,2001,2008,2020]

#     for line in lines:
#         dividends = getDividends(line.strip())    
        
#         if len(dividends) < 1:        
#             print("Skip " + line.strip() + "!")
#         else:
#             print("Analyzing " + line.strip() + " ....")
#             d_lines = { 'date':[],'year':[], 'payout_period':[],'amount':[],'incremental_percentage': [] }
            
#             # survive_years = from the 1st time they paid off up until now
#             survive_years = 0
#             if dividends[-1]['exOrEffDate'] != "N/A":
#                 survive_years = int(datetime.now().year) - int(datetime.strptime(dividends[-1]['exOrEffDate'],  "%m/%d/%Y").year)

#             #for index, dividend in enumerate(dividends[:-1]):               
#             for index, dividend in enumerate(dividends):                 
#                 if dividend['exOrEffDate'] == "N/A" or  dividend['amount'] == "": continue 
                    
#                 d = datetime.strptime(dividend['exOrEffDate'],  "%m/%d/%Y")                
#                 amount = float(Decimal(sub(r'[^\d.]', '', dividend['amount'])))

#                 if index == len(dividends)-1:                                    
#                     previous_d = d
#                     previous_amount = amount
#                 else:
#                     if dividends[index+1]['exOrEffDate'] == "N/A" or dividends[index+1]['amount'] == "": 
#                         previous_d = d
#                         previous_amount = amount
#                     else:
#                         previous_d = datetime.strptime(dividends[index+1]['exOrEffDate'],  "%m/%d/%Y") 
#                         previous_amount = float(Decimal(sub(r'[^\d.]', '', dividends[index+1]['amount'])))        

#                 if amount == 0 or previous_amount == 0: continue

#                 inc_step = (amount * 100 / previous_amount) - 100
#                 num_months = abs((previous_d.year - d.year) * 12 + (previous_d.month - d.month))
#                 # print('no month : ' + str(num_months))
#                 if num_months > 4: break   

#                 d_lines['date'].append(d.strftime("%m/%d/%Y"))
#                 d_lines['year'].append(int(d.strftime("%Y")))
#                 d_lines['payout_period'].append(num_months)
#                 d_lines['amount'].append(amount)
#                 d_lines['incremental_percentage'].append(inc_step)


#             if len(d_lines['date']) > 0:
#                 dividend_table['tick'].append(line.strip())
#                 dividend_table['streak_end_date'].append(datetime.strptime(dividends[0]['exOrEffDate'],  "%m/%d/%Y").strftime("%m/%d/%Y")) 
#                 dividend_table['lastest_amount'].append(dividends[0]['amount'])
#                 dividend_table['streak_start_date'].append(d_lines['date'][-1]) 
#                 dividend_table['num_streak'].append(len(d_lines['date']))
#                 dividend_table['incremental_percentage'].append(max(d_lines['incremental_percentage']))
#                 dividend_table['payout_period'].append(sum(d_lines['payout_period'])/len(d_lines['payout_period']))
                            
#                 # how many recessive year they paid off
#                 recession_proof = set(d_lines['year']) & set(recession)                                
#                 dividend_table['number_survive_proof'].append(len(recession_proof))

#                 #print('recession_survive ... ')   
#                 first_year_payout = min(d_lines['year'])                
#                 recession_survive = 0                
#                 # for index, r_year in enumerate(recession):
#                 #     if first_year_payout < r_year:
#                 #         recession_survive = len(recession) - index                                         
#                 #         break        

#                 #dividend_table['no_survive'].append(recession_survive)

#                 # when is the latest streak they paid off during recession
#                 dividend_table['latest_survive_streak'].append(first_year_payout)

#                 # how many years they've gone thru 
#                 dividend_table['number_survive_years'].append(survive_years)                

#             d_lines = {}
#             # print(dividend_table)
        
#     df = pd.DataFrame(dividend_table)
#     return df
    
# def loadData():
#     df1 = decode(getTickers(1))
#     df2 = decode(getTickers(2))
#     df3 = decode(getTickers(3))
#     df4 = decode(getTickers(4))
#     df5 = decode(getTickers(5))
#     df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
#     print(df)
#     df.to_csv('dividends.csv')

# loadData()

#--------------------------------