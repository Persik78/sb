num = int(input('Введите число: '))
for row in range(1, num+1):
    for col in range(row):
        print(row, end = '\t')
    print()