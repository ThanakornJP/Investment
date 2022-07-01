import requests 
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from re import sub
from decimal import Decimal
import json

df = pd.read_csv('dividends.csv')
df = df.sort_values(by=['streak_end_date'], ascending=False)
df = df.sort_values(by=['num_streak','number_survive_years','number_survive_proof'], ascending=False)
print(df)
