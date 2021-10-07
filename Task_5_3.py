tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

klas_tut = ((row1, row2) for row1, row2, in zip(tutors, klasses))

print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))

print('-' * 50)

import itertools

klas_tut = ((row1, row2) for row1, row2, in itertools.zip_longest(tutors, klasses))

print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))
print(next(klas_tut))

