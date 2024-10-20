import requests as r
import json as j
API_URL = 'https://economia.awesomeapi.com.br/json/last/'
def get_currency_format(n):
    string = f'{n:_.4f}'
    string = string.replace('.',',').replace('_','.')
    return string    
def create_url(currency):
    global API_URL
    right_format = f'{currency}-BRL'
    return API_URL+right_format
def get_currencies():
    a = r.get('https://api.frankfurter.app/currencies')
    currencies = j.loads(a.content)
    return list(currencies.keys())+['BTC']
def get_last_bid(currency):
    url = create_url(currency)
    info = r.get(url).json()[f'{currency}BRL']
    value = get_currency_format(float(info['bid']))
    return value