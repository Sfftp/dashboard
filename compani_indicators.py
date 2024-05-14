import requests
import pandas as pd


# Создаем список для хранения данных
data_appple = pd.read_csv('data/AAPL.csv')
data_amd = pd.read_csv('data/AMD.csv')
data_amzn = pd.read_csv('data/AMZN.csv')
data_nvda = pd.read_csv('data/NVDA.csv')
data_tsla = pd.read_csv('data/TSLA.csv')

df = data_tsla[['Date', 'Volume']]

df.to_csv('data/TSLA.csv', index=False)