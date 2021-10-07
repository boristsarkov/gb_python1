def num_gen(n):
    gen = (num for num in range(1, n + 1, 2))
    for i in gen:
        yield i

generator = num_gen(100)


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print('*' * 20)

# Задача со *

gen = (num for num in range(1, 101, 2))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

