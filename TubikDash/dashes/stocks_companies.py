# Import the yfinance. If you get module not found error the run !pip install yfianance from your Jupyter notebook
import yfinance as yf


import pandas as pd
tickers_list = ['AAPL', 'AMD', 'TSLA', 'NVDA', 'AMZN']

tic_list = yf.Tickers('aapl amd tsla nvda amzn')

aapl_div = pd.DataFrame(tic_list.tickers['AAPL'].dividends)
aapl_earn = pd.DataFrame(tic_list.tickers['AAPL'].earnings_dates)

amd_div = pd.DataFrame(tic_list.tickers['AMD'].dividends)
amd_earn = pd.DataFrame(tic_list.tickers['AMD'].earnings_dates)

tsla_div = pd.DataFrame(tic_list.tickers['TSLA'].dividends)
tsla_earn = pd.DataFrame(tic_list.tickers['TSLA'].earnings_dates)

nvda_div = pd.DataFrame(tic_list.tickers['NVDA'].dividends)
nvda_earn = pd.DataFrame(tic_list.tickers['NVDA'].earnings_dates)

amzn_div = pd.DataFrame(tic_list.tickers['AMZN'].dividends)
amzn_earn = pd.DataFrame(tic_list.tickers['AMZN'].earnings_dates)


def st_rt():
    pass

