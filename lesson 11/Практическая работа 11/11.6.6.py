while True:
    print('Введите местоположение коня')
    x = float(input('По горизонтали: '))
    y = float(input('По вертикали: '))

    print('Введите местоположение точки на доске:')
    x2 = float(input('По горизонтали: '))
    y2 = float(input('По вертикали: '))

    if x < 0 or y < 0 or x > 0.8 or y > 0.8 or x2 < 0 or y2 < 0 or x2 > 0.8 or y2 > 0.8:
        print('Хуйню написал, такого быть не может')
        continue
    else:
        xSquare = int(x * 10)
        ySquare = int(y * 10)
        x2Square = int(x2 * 10)
        y2Square = int(y2 * 10)
        print('Конь в клетке (',xSquare,', ',ySquare,'). Точка в клетке (',x2Square,', ',y2Square,')')

    if (abs(xSquare-x2Square) == 1 and abs(ySquare-y2Square) == 2) or (abs(xSquare-x2Square) == 2 and abs(ySquare-y2Square) == 1):
        print('Да, конь может ходить в эту точку.')
    else:
        print('Не может')
