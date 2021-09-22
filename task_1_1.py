Урок №1 Задание №1
duration = int(input('Введите число которое Вы хотите конвертировать: '))
seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 3600 % 24
days = duration // 86400 % 60
if minutes == 0:
    print(seconds, 'секунд')
elif hours == 0:
    print('{} минут {} секунд'.format(minutes, seconds))
elif days == 0:
    print('{} часов {} минут {} секунд'.format(hours, minutes, seconds))
else:
    print('{} дней {} часов {} минут {} секунд'.format(days, hours, minutes, seconds))

    

    
    
Задание №2
cubes = [x**3 for x in range(1001) if x % 2 != 0]
my_numbers_sum = 0
my_numbers_sum_list = []
total_7 = 0 # Переменна суммы чисел делящихся на 7
total_17 = 0 # Переменная суммы чисел делящихся на 7 после прибавки 17

# проход по списку
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    # Вычисление суммы чисел
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    # Условие деления на 7 без остатка
    if my_numbers_sum % 7 == 0:
       my_numbers_sum_list.append(my_numbers_sum)

# сумма чисел кубов делящихся без остатка на 7
for i in range(len(my_numbers_sum_list)):
    total_7 = total_7 + my_numbers_sum_list[i]
print('Сумма кубов чисел делящихся на 7 =', total_7)

# Список кубов + 17
cubes = [(x**3)+17 for x in range(100) if x % 2 == 0]
my_numbers_sum = 0
my_numbers_sum_list_even_numbers = []

# проход по списку
for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])

    # Вычисление суммы чисел
    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]

    # Условие деления на 7 без остатка
    if my_numbers_sum % 7 == 0:
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)

# сумма чисел кубов делящихся без остатка на 7
for i in range(len(my_numbers_sum_list_even_numbers)):
    total_17 = total_17 + my_numbers_sum_list_even_numbers[i]
print('Сумма кубов чисел делящихся на 7 после прибавки числа 17 =', total_17)




Задание №3
# Создаем диапазон целых чисел
for i in range(100):
    new_str = str(i + 1)
    new_list = list(new_str)
    # Ставим при котором последнее число каждого элемента в списке = 1 и не = 11
    if int(new_list[-1]) == 1 and i + 1 != 11:
        print('{} процент'.format(i + 1))
    # Под условие где сравниваем последнюю цифру элементов списка которые больше 1 и меньше либо равно 4
    elif int(new_list[-1]) > 1 and int(new_list[-1]) <= 4:
        # Проверяем условие где число в списке больше 10 и меньше либо равно 14
        if  i + 1 > 10 and i + 1 <= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))


