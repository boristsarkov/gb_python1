x = input('Введите число на английском прописью: ')
numbers = {'one': 'один',
           'two': 'два',
           'three': 'три',
           'four': 'четыре',
           'five': 'пять',
           'six': 'шесть',
           'seven': 'семь',
           'eight': 'восемь',
           'nine': 'девять',
           'ten': 'десять'}


def num_trsanslate(x):
    return numbers.get(x)


print(num_trsanslate(x))
