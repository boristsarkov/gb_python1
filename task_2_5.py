# Создаем список цен
prices = [57.8, 46.31, 97, 29, 33.33, 99.99, 56.07, 24, 25.50, 100, 105.02]

for num in prices: # Проходимся по списку цен
    rubles = int(num) # Отделяем целое число
    penny = (num - rubles) * 100 # Отделяем дробную часть
    print(f' {rubles} руб.  {penny:02.0f} коп.') # Выводим список цен в нужном виде

# Создаем список цен
prices = [57.8, 46.31, 97, 29, 33.33, 99.99, 56.07, 24, 25.50, 100, 105.02]
print(id(prices)) # Проверяем id
prices.sort() # Сортируем список
print(id(prices)) # Проверяем что id остался тем же
for num in prices: # Проходимся по списку цен
    rubles = int(num) # Отделяем целое число
    penny = (num - rubles) * 100 # Отделяем дробную часть
    print(f' {rubles} руб. {penny:02.0f} коп.') # Выводим список цен в нужном виде

top5_prices = [] # Создаем пустой список для дальнейшей записи в него
prices = [57.8, 46.31, 97, 29, 33.33, 99.99, 56.07, 24, 25.50, 100, 105.02] # Создаем список цен
prices.sort(reverse=True) # Сортируем список в обратном порядке
for num in prices: # Проходимся по списку цен
    rubles = int(num) # Отделяем целое число
    penny = (num - rubles) * 100 # Отделяем дробную часть
    price = f'{rubles} руб. {penny:02.0f} коп.' # Присваиваем переменной вид для дальнейшего вывода на экран
    top5_prices.append(price) # Добавляем в конец списка полученные данные

end_price = ', '.join(top5_prices[::][:5]) # Склеиваем 5 первых элементов столбца в строку
print(end_price)
