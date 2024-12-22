number = int(input('введите значение N: '))
for row in range(1, number + 1):
    for col in range(1, number + 1):
        if row % 2 == 0:
            print(row, end = '')
        else:
            print(col, end = '')
    print()