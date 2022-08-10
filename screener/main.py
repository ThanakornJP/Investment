import pandas as pd
import ticker as tk
import dividend as dvd

#tk.reload()
dvd.reload()
nasdaq_dividends = pd.read_csv('dividends.nasdaq.csv')   
print(nasdaq_dividends.loc[ nasdaq_dividends['tick'] == 'EVLMC'])
