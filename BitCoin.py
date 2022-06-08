import APIKey
import requests


headers = {
    'X-CMC_PRO_API_KEY' : APIKey.key,
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '4243f0f4-4276-4984-8539-5a2156f96bc7',
}

params = {
    'start' : '1',
    'limit' : '5',
    'convert' : 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json

coins = json['data']

for X in coins:
    print(X['symbol'], X['quote']['USD']['price'])