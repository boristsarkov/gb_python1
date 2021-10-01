import requests
import decimal
import datetime


def currency_rates(curr):
    curr = curr.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if curr not in response:
        return None


    rubles = response[response.find('<Value>', response.find(curr)) + 7:response.find('</Value>', response.find(curr))]
    date_val = resp.headers['Date']
    return f'{decimal.Decimal(rubles.replace(",", ".")):.2f}, {date_val}'



