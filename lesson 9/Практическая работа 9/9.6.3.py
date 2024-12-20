rows = int(input('Введите кол-во рядов: '))
chairs = int(input('Введите кол-во стульев: '))
meters = int(input('Введите кол-во метров между рядами: '))

print('\nСцена\n')

for maket in range(rows):
    print('=' * chairs, end = ' ')
    print('*' * meters, end = ' ')
    print('=' * chairs, end='\n')