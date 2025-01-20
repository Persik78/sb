def floattt(N):
    print('Формат плавающей точки: x =', end=' ')
    count_figure = 0
    for stringa in reversed(N):
        if stringa == '.':
            break
        else:
            count_figure += 1
    N = float(N)
    if N.is_integer():
        print(N / 10**(count_figure - 1), '* 10 **', count_figure - 1)
    else:
        print(N * 10**(count_figure - 1), '* 10 **', -count_figure + 1)

while True:
    N = input('введите число больше 0: ')

    if float(N) > 0:
        floattt(N)
    else:
        print('Хуйню ввел бразе, иди траву потрогай')