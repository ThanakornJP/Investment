import requests 
import json
import pandas as pd
from datetime import datetime
from re import sub
from decimal import Decimal


def load(model):
    # return pd.read_csv('dividends.csv')    
    return pd.read_csv(model)        

def model(df):
    return df

def save(df, model):
    # df.to_csv('dividends_with_info.csv')
    df.to_csv(model)


df = model(load('dividends.csv'))
save(df, 'dividends_with_info.csv')
print(df)