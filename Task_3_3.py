def thesaurus(*names):
end_dict = dict()
    for i in names:
        end_dict.setdefault(i[0], [])
        end_dict[i[0]].append(i)
    return end_dict


print(thesaurus('Илья', 'Владимир', 'Василий', 'Николай', 'Иван'))
