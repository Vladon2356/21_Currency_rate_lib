import datetime

import requests
from bs4 import BeautifulSoup

URL = ''
HEADERS = {'': '', '': ''}
soup = BeautifulSoup()


def get_values_for_date_from_api(date):
    format_data = '%d.%m.%Y'
    date = datetime.date.strftime(date, format_data)
    url_pb = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    url_mb = 'https://api.monobank.ua/bank/currency'
    response_pb = requests.get(url=url_pb).json()
    response_mb = requests.get(url=url_mb).json()
    return {'Monobank': response_mb, 'Privat24': response_pb}


def get_values_for_range_date_from_api(start_date, end_date):
    format_data = '%d.%m.%Y'
    pv24 = dict()
    for i in range((end_date - start_date).days + 1):
        date = datetime.date.strftime(start_date + datetime.timedelta(days=i),format_data)
        print(date)
        url_pb = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
        pv24[date] = requests.get(url=url_pb).json()
    url_mb = 'https://api.monobank.ua/bank/currency'
    response_mb = requests.get(url=url_mb)
    return {'Monobank': response_mb.json(), 'Privat24': pv24}

