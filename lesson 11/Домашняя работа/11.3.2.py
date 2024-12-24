while True:
    print('Введите местоположение фигуры')
    x = float(input('По горизонтали: '))
    y = float(input('По вертикали: '))

    if x < 0 or y < 0 or x > 0.8 or y > 0.8:
        print('Хуйню написал, такого быть не может')
        continue
    else:
        xSquare = int(x * 10)
        ySquare = int(y * 10)

        print('Фигура находится в клетке (',xSquare,', ',ySquare,')')

