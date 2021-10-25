class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.mtrx])

    def __add__(self, other):
        answer = ' '
        if len(self.mtrx) == len(other.mtrx):
            for line_1, line_2 in zip(self.mtrx, other.mtrx):
                if len(line_1) != len(line_2):
                    return 'problem'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'

        else:
            return 'problem'
        return answer

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[9, 10], [11, 12], [14, 15], [16, 17]])
print(matrix_1)
print()
print(matrix_2)