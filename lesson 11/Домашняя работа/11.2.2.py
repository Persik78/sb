age = int(input('Сколько лет? '))
temperatyra = float(input('Какая температура? '))

win = round((age * 1.5) * temperatyra, 2)

print('Нужно подарить: ', win)