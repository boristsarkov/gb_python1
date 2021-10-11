import sys

numbers = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as open_f:
    if len(numbers) > 1:
        start_indx = int(numbers[0])
        end_indx = int(numbers[1])
    elif len(numbers) == 0:
        start_indx = 0
        end_indx = sum(1 for line in open_f)
        open_f.seek(0)
    else:
        start_indx = int(numbers[0])
        end_indx = sum(1 for line in open_f)
        open_f.seek(0)

    for i, line in enumerate(open_f):
        if start_indx <= i +1 <= end_indx:
            print(line.strip())