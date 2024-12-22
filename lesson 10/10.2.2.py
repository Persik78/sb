number = int(input('Введите размер матрицы: '))
for row in range(1, number + 1):
    for col in range(1, number + 1):
        if col % 3 == 0:
            print(col, end = '\t')
        else:
            print(row, end = '\t')
    print()