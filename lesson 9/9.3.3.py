text = input('Введите текст: ')
small = 0
big = 0
for symbol in text:
    if symbol == 'Ы':
        big += 1
    elif symbol == 'ы':
        small += 1
print('Больших букв Ы: ', big)
print('Маленьких букв Ы: ', small)