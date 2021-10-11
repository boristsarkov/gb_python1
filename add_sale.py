import sys

price = sys.argv[1]
with open('bakery.csv', 'a', encoding='utf-8') as open_f:
    open_f.write(price + '\n')