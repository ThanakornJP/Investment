import pandas as pd
import requests

api_key = '62ad732d92c4b1.07282612'

# SINGLE FILTER
mktcap_url = f'https://eodhistoricaldata.com/api/screener?api_token={api_key}&sort=market_capitalization.desc&filters=[["market_capitalization",">",100000000000]]&limit=10'

mktcap = requests.get(mktcap_url).json()

mktcap_df = pd.DataFrame(mktcap['data']).drop(
    [
        'sector', 'industry','refund_1d', 
        'refund_1d_p','refund_5d', 'refund_5d_p'
    ], axis = 1)

mktcap_df