# Вариант преподавателя
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
empty_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
print(empty_list)



# Вариант мой до просмотра вебинара
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
empty_list = []
i = 0
for el in src:
    if src[i - 1] < src[i] and i != 0:
        empty_list.append(el)
    i += 1
end_time = time.perf_counter()
print(empty_list)



# Вариант получившийся после обращения к наставнику
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
empty_list = []
for el in range(1, len(src)):
    if src[el - 1] < src[el]:
        empty_list.append(src[el])
end_time = time.perf_counter()
print(empty_list)
