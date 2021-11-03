import yfinance as yf
import requests
import time
from bs4 import BeautifulSoup as bs


class Crypto:
    def __init__(self, log):
        if log[0] == '':
            del log[0]
            self.time = log[0]
            self.open = log[1]
            self.high = log[2]
            self.low = log[3]
            self.close = log[4]
            self.volume = log[5]



'''
-----------------------------------
Geting the appropriate stocks: START
-----------------------------------
'''


def find_all(a_str, sub):  # Fonction pour trouver chaque position des voyelles
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return

        index = a_str.find('"', start + 2 + len(sub))
        crypt = a_str[start + 2 + len(sub):index]
        yield crypt
        start += len(sub)


session = requests.Session()
# Getting the html source
html = session.get("https://api.cryptorank.io/v0/coins?specialFilter=topGainersFor24h&limit=50")

# create a new soup
soup = str(bs(html.text, features="lxml"))

cryptos_list = list(find_all(soup, '"symbol"'))  # Finding all stocks in the top 50 growing cryptos/stocks
# print(cryptos_list)

'''
-----------------------------------
Geting the appropriate stocks: END
-----------------------------------
'''

'''
-----------------------------------
Making a list out of the stock data: START
-----------------------------------
'''

# Choosing the Stock
msft = yf.Ticker("MSFT")

'''
-----------------------------------
Making a list out of the stock data: START
-----------------------------------
'''

print("------------------------------")
print("------------------------------")


def zeroX(n):
    result = ""
    if (n < 10):
        result += "0"
    result += str(n)
    return result


def dump_Pandas_Timestamp(ts):
    result = ""
    # result += str(ts.year) + "-" + zeroX(ts.month) + "-" + zeroX(ts.day)
    result += " " + zeroX(ts.hour) + ":" + zeroX(ts.minute) + ":" + zeroX(ts.second)
    return result


def dump_Pandas_DataFrame(DF):
    result = ""
    for indexItem in DF.index:
        ts = dump_Pandas_Timestamp(indexItem)
        fields = ""
        first = 1
        for colname in DF.columns:
            fields += ("" if first else ", ") + colname + " = " + str(DF[colname][indexItem])
            first = 0
        result += ts + " " + fields + "\n"
    return result


# get historical market data
hist = msft.history(period="1d", interval="5m", actions=False)
fixed_hist = dump_Pandas_DataFrame(hist).splitlines()

'''
-----------------------------------
Making a list out of the stock data: END
-----------------------------------
'''

# item = fixed_hist[0]
#
# item = item.replace(" = ", "=").replace(",", "").split(" ")
# if item[0] == "":
#     del item[0]
# print(item)
