x = int(input('Введите количество мальчиков: '))
y = int(input('Введите количество девочек: '))
answer = ''
for iteration in range(0, x+y):
    if abs(x-y) > 2:
        print('Нет решения')
        break
