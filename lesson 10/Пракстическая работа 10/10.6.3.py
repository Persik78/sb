horizon = int(input('Введите ширину: '))
vertical = int(input('Введите длину: '))
for row in range(horizon):
    for col in range(vertical):
        if row == 0 or row == horizon - 1:
            print('-', end = '')
        elif col == 0 or col == vertical - 1:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()