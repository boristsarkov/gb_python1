class Cell:
    def __init__(self, number):
        self.number = number

    def make_order(self, rows):
        return '\n'.join(['*' * rows for i in range(self.number // rows)]) + '\n' + '*' * (self.number % rows)

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return 'Сумма клеток = ' + str(self.number + other.numbers)

    def __sub__(self, other):
        return self.number - other.numbers if self.number - other.numbers > 0 \
            else 'Ячеек меньше либо равно - вычитание невозможно'

    def __mul__(self, other):
        return 'Умножение клеток =' + str(self.number * other.numbers)

    def __truediv__(self, other):
        return 'Деление клеток = ' + str(self.number / other.numbers)


cell_1 = Cell(20)
cell_2 = Cell(40)
print(cell_1)
print(cell_2.make_order(11))
