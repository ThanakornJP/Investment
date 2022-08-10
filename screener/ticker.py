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
import csv

def model(model):
    if model is None: 
        return None 
    else:
        symbols = set( symbol for symbol in model[0].values.tolist())
        del_set = set()
        sav_set = set()
        my_list = ['W','R','P','Q']
        for symbol in symbols:
            if len(symbol) > 4 and symbol[-1] in my_list:
                del_set.add(symbol)
            else:
                sav_set.add(symbol)
        return sav_set


def load(exchange):
    if exchange == 'snp':
        return pd.DataFrame(si.tickers_sp500())    
    elif exchange == 'nasdaq':
        return pd.DataFrame(si.tickers_nasdaq())
    else:
        return None


def save(df, model):
    with open(model, 'w') as f:
        for tick in df:    
            f.write(tick)
            f.write('\n')

def reload():
    save(model(load('snp')),'tick.snp.csv')
    save(model(load('nasdaq')),'tick.nasdaq.csv')


# def getTickers():
#     df1 = pd.DataFrame(si.tickers_sp500())
#     df2 = pd.DataFrame(si.tickers_nasdaq())
#     print('all S&P500')
#     print(df1)
#     print('all NASDAQ')
#     print(df2)

#     sym1 = set( symbol for symbol in df1[0].values.tolist())
#     sym2 = set( symbol for symbol in df2[0].values.tolist())
#     symbols = set.union(sym1,sym2)
#     del_set = set()
#     sav_set = set()
#     my_list = ['W','R','P','Q']
#     for symbol in symbols:
#         if len(symbol) > 4 and symbol[-1] in my_list:
#             del_set.add(symbol)
#         else:
#             sav_set.add(symbol)

#     print(f'Removed {len(del_set)} unqualified stock')
#     print('All qualified S&P and NASDAQ')
#     print(sav_set)
    
#     with open('ticker.txt', 'w') as f:
#         for tick in sav_set:    
#             f.write(tick)
#             f.write('\n')
        
# getTickers()
