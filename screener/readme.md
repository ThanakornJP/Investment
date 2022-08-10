
1. get all nasdaq's tick names
2. get all snp's tick names
   

# 1. main.py - entry point 
...


# 2. ticker.py
load tick for further analysis

- load(string:exchange):DataFrame - get all tickers 
- model(DataFrame:model):set - used to load executable tickers in the list 
- reload() - save nasdaq and snp into tick.nasdaq.csv and tick.snp.csv
- save(DataFrame:model,string:filename) - save ticker into file.csv

# 3. dividend.py
filter only consecutive earnable companies

- reload() - save nasdaq and snp into dividends.csv
.
------------------------------------------------

1. A-Basket update
   1. get all stock at least 25-year founded 
   2. get all dividends 
   3. get number of payouts per year
   4. get current dividend
   5. get current price
   6. calculate annualized =  current dividend * number of payouts per year



--- 
1. get all ticks
2. filter all ticks by available dividend information (remove non-dividendable company)
3. augment information
   1. demographic - industry, market cap, volume, yield, pe, eps, annualized dividend
   2. bebaviour
      1. today high, low, 
      2. 52wk high, low 