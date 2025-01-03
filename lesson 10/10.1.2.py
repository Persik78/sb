number = int(input('Ввдеите значение N: '))
for row in range(number+1):
    for col in range(number+1):
        print(row + col, end = '\t')
    print()