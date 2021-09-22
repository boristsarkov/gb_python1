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
<<<<<<< HEAD

=======
>>>>>>> 29e56035beda8f17c93ac5e660f4ceed190fb31b
