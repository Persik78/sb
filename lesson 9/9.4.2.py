number = int(input('Введите первое число: '))
step = int(input('Введите шаг: '))
sum = 0
print('\nIP-адрес: ', end = ' ')
for generate in range(3):
    print(number, end = '.')
    sum += number
    number += step
print(sum)