import re

name_domain = {'name': None, 'domain': None}
MAIL = re.compile(r'([a-z0-9-_\.]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found = MAIL.findall(email)
    if found:
        name, domain = found[0]
    else:
        raise ValueError(f'wrong email: {email}')
    name_domain['name'] = name
    name_domain['domain'] = domain

    return name_domain

print(email_parse('borman-dallas@yandex.ru'))
print(email_parse('borman-dallas@yandexru'))
