# For data manipulation
import pandas as pd
from urllib.request import urlopen, Request

# To extract fundamental data
from bs4 import BeautifulSoup


def fundamental_metric(soup, metric):
    return soup.find(text = metric).find_next(class_='snapshot-td2').text

def get_fundamental_data(df):
    for symbol in df.index:
        try:
            url = ("http://finviz.com/quote.ashx?t=" + symbol.lower())
            req = Request(url=url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
            response = urlopen(req)
            soup = BeautifulSoup(response)
            for m in df.columns:
                df.loc[symbol,m] = fundamental_metric(soup,m)
        except Exception as e:
            print (symbol, 'not found')
    return df
