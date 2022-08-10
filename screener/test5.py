from bs4 import BeautifulSoup
import requests


# r = requests.get("https://finance.yahoo.com/quote/RGCO?p=RGCO").text
# soup = BeautifulSoup(r,'html.parser').text
# print(soup)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                  "(KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

html = requests.get('https://finance.yahoo.com/quote/RGCO?p=RGCO', headers=headers)
print(html)
soup = BeautifulSoup(html.text, 'lxml')
#print(soup.title)

for item in soup.find_all():
    if "data-test" in item.attrs:
        if item["data-test"] == "MARKET_CAP-value":  
            print(item.text)

#<td class="Ta(end) Fw(600) Lh(14px)" data-test="MARKET_CAP-value">194.36M</td>