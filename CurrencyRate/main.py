import datetime

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


def main():
    action = int(input('If You wount get values for range date enter - 1 else - 2 : '))
    if action == 2:
        day,month, year = [int(i) for i in input('Please enter date in format "d.m.y : "').split('.')]
        start_date = datetime.date(day=day, month=month, year=year)
        result = parse_by_date(start_date, save_to_json=True)
    else:
        start_day,start_month, start_year = [int(i) for i in input('Please enter start date in format "d.m.y" : ').split('.')]
        start_date = datetime.date(day=start_day, month=start_month, year=start_year)
        end_day,end_month, end_year = [int(i) for i in input('Please enter end date in format "d.m.y" : ').split('.')]
        end_date = datetime.date(day=end_day, month=end_month, year=end_year)
        result = parse_by_range_date(start_date=start_date, end_date=end_date, save_to_json=True,save_to_csv=True)

        graph = input('Add graph (+ or -)')
        if graph.strip() == '+':
            drow_graph(result,for_sale=True)

    return result

main()
