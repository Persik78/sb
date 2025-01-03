number = int(input('Введите размер матрицы: '))
for row in range(1, number + 1):
    for col in range(number, 0, -1):
        if row > col:
            print('2', end = '\t')
        elif row < col:
            print('0', end='\t')
        else:
            print('1', end = '\t')
    print()