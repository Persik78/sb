from numpy.core.defchararray import lower


def count_letters(text):
    count_figure = 0
    count_letter = 0
    K = input('Введите какую цифру искать: ')
    N = input('Введите какую букву искать: ')
    for figure in text:
        if figure == K:
            count_figure += 1
    for letter in text:
        if letter == N or letter == lower(N):
            count_letter += 1
    print('Количество цифр', K, ':', count_figure)
    print('Количество букв', N, ':', count_letter)



text = input('Введите текст: ')
count_letters(text)

