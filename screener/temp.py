

tickers = ['ibm']
# xlsWriter = pd.ExcelWriter('dividend report')

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

response = requests.get('https://api.nasdaq.com/api/quote/AAPL/dividends', params=params, headers=headers)
response_json = response.json()
#print(response_json)
#print()
print(response_json.keys())
#print(response_json['message'])
#print(response_json['status'])
#print(response_json['data'])
print()
response_json_data = response_json['data']
print(response_json_data.keys())
print(response_json_data['dividends'].keys())
print(response_json_data['dividends']['headers'])
# print(response_json_data['dividends']['rows'])

#dates = [datetime.strptime(d, "%m-%d-%Y") for d in date_strs]

#df = pd.DataFrame()
l = []
dividends = response_json_data['dividends']['rows']
for index, dividend in enumerate(dividends[:-1]):
    d = datetime.strptime(dividend['exOrEffDate'],  "%m/%d/%Y")
    d_tmr = datetime.strptime(dividends[index+1]['exOrEffDate'],  "%m/%d/%Y") 

    num_months = abs((d_tmr.year - d.year) * 12 + (d_tmr.month - d.month))
    if num_months > 4: break   
    l.append({'date':d.strftime("%m/%d/%Y"),'payout_period': num_months,'amount': float(Decimal(sub(r'[^\d.]', '', dividend['amount']))) })

print(l)
print(len(l)/4)


    # num_months = abs((dates[index+1].year - d.year) * 12 + (dates[index+1].month - d.month))
    # ds.append(num_months)
    # if num_months > 5: break   

    



    #print(pd.to_datetime(dividend['exOrEffDate']).dt.year + " " + dividend['amount'])
