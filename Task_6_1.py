with open('nginx_logs.txt') as open_f:
    empty_list = []
    for line in open_f:
        spl = line.split()
        empty_list.append((spl[0], spl[5].replace('"', ''), spl[6]))

print(empty_list)