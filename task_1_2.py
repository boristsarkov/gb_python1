# Урок №1 Задание №2
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





