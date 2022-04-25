import datetime
import csv
import json

from CurrencyRate.get_data import get_values_for_date_from_api, get_values_for_range_date_from_api
from CurrencyRate.exceptions import ApiNotResponse

def save_to_json_file(currency_rate, start_date, end_date=0):
    if end_date != 0:
        out_file = open(f"currency_rate_from_{start_date}_to_{end_date}.json", "w")
    else:
        out_file = open(f"currency_rate_for_{start_date}.json", "w")
    json.dump(currency_rate, out_file)
    out_file.close()
    print('Done')

def save_to_csv_file(currency_rate, start_date, end_date=0):
    mb_rate = currency_rate['Monobank']
    pb_rate = currency_rate['Privat24']
    if end_date != 0:
        filename = f'currency_rate_from_{start_date}_to_{end_date}.csv'
    else:
        filename = f'currency_rate_for_{date}.csv'
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Date', 'Bank', 'Currency', 'rateSell', 'rateBuy']
        )
        print(mb_rate)
        for currency in mb_rate:
            print(currency, mb_rate[currency])
            try:
                writer.writerow(
                    [datetime.date.today().strftime('%d.%m.%Y'), 'Monobank', currency, mb_rate[currency]['rateSell'], mb_rate[currency]['rateBuy']]
                )
            except KeyError:
                writer.writerow(
                    [datetime.date.today().strftime('%d.%m.%Y'), 'Monobank', currency, mb_rate[currency]['rateCross'], mb_rate[currency]['rateCross']]
                )
        for date in pb_rate:
            rate = pb_rate[date]
            for currency_ticker in rate:
                try:
                    rateSell = rate[currency_ticker]['saleRate']
                    rateBuy = rate[currency_ticker]['purchaseRate']
                    writer.writerow(
                        [date, 'Privat24', currency_ticker, rateSell, rateBuy]
                    )
                except KeyError:
                    rateSell = rate[currency_ticker]['saleRateNB']
                    rateBuy = rate[currency_ticker]['purchaseRateNB']
                    writer.writerow(
                        [date, 'Privat24', currency_ticker, rateSell, rateBuy]
                    )
    print('Done')

def parse_by_date(date, save_to_json: bool = False, save_to_csv: bool = False):
    response = get_values_for_date_from_api(date)
    rate_pb = {}
    try:
        for currency in response["Privat24"]['exchangeRate']:
            currency_ticker = currency['currency']

            try:
                currency_ticker = currency['currency']
                rate[currency_ticker] = {
                    'saleRate': currency['saleRate'],
                    'purchaseRate': currency['purchaseRate'],
                    'saleRateNB': currency['saleRateNB'],
                    'purchaseRateNB': currency['purchaseRateNB'],
                }
            except KeyError:
                rate[currency_ticker] = {
                    'saleRateNB': currency['saleRateNB'],
                    'purchaseRateNB': currency['purchaseRateNB'],
                }
        result_pb = {str(date): rate}
        rate_mb = {}
        usd = response["Monobank"][0]
        eur = response["Monobank"][1]
        gbp = response["Monobank"][3]
        for key in ["currencyCodeA", "date"]:
            del usd[key]
            del eur[key]
            del gbp[key]
        rate_mb['USD'] = usd
        rate_mb['EUR'] = eur
        rate_mb['GBP'] = gbp

    except KeyError:
        raise ApiNotResponse('Api not response, please try later')

    result = {'Monobank': rate_mb, 'Privat24': rate_pb}
    if save_to_csv:
        save_to_csv_file(currency_rate=result,start_date=date)
    if save_to_json:
        save_to_json_file(currency_rate=result,start_date=date)
    return result


def parse_by_range_date(start_date, end_date, save_to_json: bool = False, save_to_csv: bool=False):
    response = get_values_for_range_date_from_api(start_date, end_date)
    rate_pb = {}
    for date in response['Privat24']:
        try:
            rate = {}
            for currency in response["Privat24"][date]['exchangeRate']:
                try:
                    currency_ticker = currency['currency']
                except KeyError:
                    continue
                try:
                    rate[currency_ticker] = {
                        'saleRate': currency['saleRate'],
                        'purchaseRate': currency['purchaseRate'],
                        'saleRateNB': currency['saleRateNB'],
                        'purchaseRateNB': currency['purchaseRateNB'],
                    }
                except KeyError:
                    rate[currency_ticker] = {
                        'saleRateNB': currency['saleRateNB'],
                        'purchaseRateNB': currency['purchaseRateNB'],
                    }
            rate_pb[date] = rate
            rate_mb = {}
            usd = response["Monobank"][0]
            eur = response["Monobank"][1]
            gbp = response["Monobank"][3]
            for key in ["currencyCodeA", "date"]:
                del usd[key]
                del eur[key]
                del gbp[key]
            rate_mb['USD'] = usd
            rate_mb['EUR'] = eur
            rate_mb['GBP'] = gbp

        except KeyError:
            raise ApiNotResponse('Api not response, please try later')

    result = {'Monobank': rate_mb, 'Privat24': rate_pb}

    if save_to_csv:
        save_to_csv_file(currency_rate=result,start_date=start_date, end_date=end_date)
    if save_to_json:
        save_to_json_file(currency_rate=result,start_date=start_date, end_date=end_date)
    return result


day = datetime.date(year=2022, month=2, day=13)
# print(parse_by_date(date=day, save_to_csv=True, save_to_json=True))