# Дан список
main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# Создаем пустой список для дальнейшей записи в него изменений 
empry_list = []
# Проходимся по списку
for num in main_list:
    if num.isdigit():# Проверям наличие цифр
        empry_list.extend(['"', f'{int(num):02}', '"']) # добавляем элемент в пустой список в нужном формате
    elif (num.startswith('+')) or (num.startswith('-') and num[1:].isdigit()): # проверяем по списку есть ли + или -
        empry_list.extend(['"', f'{num[0]}{int(num):02}', '"']) # добавляем элемент в пустой список в нужном формате
    else:
        empry_list.append(num) # во всех не отработанных случаях добавляем данные в конец списка
exit_string = ' '.join(empry_list)
print(exit_string)
