import random

class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._number_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5

        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)
        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')
            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())



        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def __str__(self):
        return '-----{}----- \n {}'.format(self.player_type, "\n".join([" ".join(map(str, line)) \
                                                                                 for line in self._card]))



class LotoGame(LotoCard):
    def __init__(self, human, comp):
        self.human = human
        self.comp = comp

        super().__init__(self)

    def start(self):
        rand = random.sample(range(self._MAX_NUMBER + 1), k=90)
        i = 1
        while i < 90:
            print(f'\n {self.human} \n \n {self.comp}')
            rand_new = random.choice(rand)
            print(f'Боченок №{rand_new}')
            rand.remove(rand_new)
            balance = self._MAX_NUMBER - i
            print(f'Осталось боченков {balance}')
            for el in range(len(self._card)):
                if rand_new in self._card[el]:
                    idx = self._card[el].index(rand_new)
                    self._card[el][idx] = '-'
            i += 1
            y = input('Продолжэаем? y/n')
            if y == 'y':
                continue
            elif y == 'n':
                break

human = LotoCard('Игрок')
computer = LotoCard('Компьютер')
game = LotoGame(human, computer)

game.start()