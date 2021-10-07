src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
empty_list = []
[empty_list.append(num) for num in src if num not in empty_list]

print(empty_list)
