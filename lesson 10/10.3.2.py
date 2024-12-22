for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end = '')
        elif row + 29 == col: #and row < 9: #- чтобы обочины были выше горизонтальной линии
            print('\\', end = '')
        elif -row + 19 == col: #and row < 9: #- чтобы обочины были выше горизонтальной линии
            print('/', end = '')
        elif col == 24:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()