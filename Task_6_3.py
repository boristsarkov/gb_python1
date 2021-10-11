from itertools import zip_longest
import json
empty_dict = {}
with open('users.csv', encoding='utf-8') as open_f_us:
    with open('hobby.csv', encoding='utf-8') as open_f_hob:
        sum_line_us = sum(1 for line in open_f_us)
        sum_line_hob = sum(1 for line in open_f_hob)
        if sum_line_us < sum_line_hob:
            exit(1)
        open_f_us.seek(0)
        open_f_hob.seek(0)
        for line_us, line_us_hob in zip_longest(open_f_us, open_f_hob):
            empty_dict[line_us.strip()] = line_us_hob.strip() if line_us_hob is not None else line_us_hob

with open('Task_6_3.json', 'w', encoding='utf-8') as open_f:
    json.dump(empty_dict, open_f, ensure_ascii=False)
print(empty_dict)


