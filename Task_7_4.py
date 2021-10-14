import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
empty_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    empty_dict[i] = 0

for file in files:
    empty_dict[10 ** len(str(file))] +=1


print(empty_dict)