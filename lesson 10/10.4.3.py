size = int(input('Введите значение N: '))

for row in range(size+1):
    for col in range(row, size+1):
        print(col, end = '\t')
    print()