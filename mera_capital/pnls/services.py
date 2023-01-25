import os
import requests

from django.shortcuts import render
from dotenv import load_dotenv


# только для токена, чтобы не рисковать основными секретными данными
load_dotenv('./.env')

# основные переменные среды
load_dotenv('../.env')

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token():
    '''Получение токена для запросов к API.'''
    url = 'https://test.deribit.com/api/v2/public/auth'
    params = {
        'client_id': f'{CLIENT_ID}',
        'client_secret': f'{CLIENT_SECRET}',
        'grant_type': 'client_credentials'
    }
    response = requests.get(url, params=params)
    return response.json().get('result').get('access_token')

def get_balance():
    '''Получение баланса в биткоинах.'''
    TOKEN = os.getenv('TOKEN')
    url = 'https://test.deribit.com/api/v2/private/get_account_summary'
    auth = {'Authorization': f'Bearer {TOKEN}'}
    params = {
        'currency': 'BTC',
        'extended': 'true'
    }
    response = requests.get(url, headers=auth, params=params)
    return response.json().get('result').get('balance')

def get_dollar_rate():
    '''Получаение курса доллара относительно биткоина.'''
    url = 'https://test.deribit.com/api/v2/public/get_index_price?index_name=btc_usd'
    return(requests.get(url).json().get('result').get('index_price'))
