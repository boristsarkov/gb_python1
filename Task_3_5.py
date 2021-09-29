from random import choice, seed, sample, random, shuffle
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n):
    """Функция генерирующая n количество шуток в случайном порядке"""
    end_list = []
    for num in range(n):
        list_nouns = choice(nouns)
        list_adverbs = choice(adverbs)
        list_adjectives = choice(adjectives)
        end_list.append(f'{list_nouns}, {list_adverbs}, {list_adjectives}')
    return end_list

print(get_jokes(3))

def get_jokes_new(n, repeat=True):
    """Функция генерирующая n количество шуток в случайном порядке и исключает повторы слов"""
    end_list = []
    if not repeat:
        for i in range(n):
            list_nouns = choice(nouns)
            list_adverbs = choice(adverbs)
            list_adjectives = choice(adjectives)
            end_list.append(f'{list_nouns}, {list_adverbs}, {list_adjectives}')
    else:
        if n > min(len(nouns), len(adverbs), len(adjectives)):
            return 'Больше шуток нет'
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        for i in range(n):
            end_list.append(f'{nouns[i]}, {adverbs[i]}, {adjectives[i]}')
    return end_list

print(get_jokes_new(3, True))

