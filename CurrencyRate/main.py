import datetime
from datetime import date
import matplotlib.pyplot as plt

from CurrencyRate.parse_response import parse_by_range_date, parse_by_date


def create_dict_for_drow_graph(result):
    res = dict()
    for date in result['Privat24']:
        for currency in result['Privat24'][date]:
            res[currency] = dict()
    for date in result['Privat24']:
        for currency in result['Privat24'][date]:
            try:
                res[currency][date] = {
                    'buyRate': result['Privat24'][date][currency]['purchaseRate'],
                    'saleRate': result['Privat24'][date][currency]['saleRate'],
                }
            except KeyError:
                res[currency][date] = {
                    'buyRate': result['Privat24'][date][currency]['purchaseRateNB'],
                    'saleRate': result['Privat24'][date][currency]['saleRateNB'],
                }
    return res


def drow_graph(result, for_sale: bool):
    currency_date = create_dict_for_drow_graph(result)
    for currency in currency_date:
        x = []
        y = []
        for date in currency_date[currency]:
            day, month, year = [int(i) for i in date.split('.')]
            d = datetime.date(day=day, month=month, year=year)
            x.append(d.strftime('%d.%m'))
            if for_sale:
                y.append(currency_date[currency][date]['saleRate'])
            else:
                y.append(currency_date[currency][date]['buyRate'])
        plt.plot(x, y)
        plt.xlabel('date')
        plt.ylabel('value')

        plt.title(f'Graph for {currency}')
        plt.show()


def main(start_date: date,
         end_date: date = 0,
         to_csv: bool = False,
         to_json: bool = False,
         add_graph: bool = False,
         path_where_save :str = ''):
    if end_date == 0:
        result = parse_by_date(start_date, save_to_json=to_json, save_to_csv=to_csv)
    else:
        result = parse_by_range_date(start_date=start_date, end_date=end_date, save_to_json=to_json, save_to_csv=to_csv)

        if add_graph:
            drow_graph(result, for_sale=True)
    return result
