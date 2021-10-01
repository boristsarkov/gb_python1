import utils




currency = input('Введите код валюты. Наример USD: ')



print(utils.currency_rates(currency))
print(utils.currency_rates('EUR'))
print(utils.currency_rates('CNY'))
print(utils.currency_rates('USD'))



