count = int(input('Введите кол-во чисел в последовательности: '))
numeralCount = 0
for num in range(1, count + 1):
    print('Введите', num, 'число: ', end = '')
    number = int(input())
    while number > 0:
        if (number % 10) > 5:
            numeralCount += 1
        number //= 10
print('Кол-во цифр больше 5 в последовательности: ', numeralCount)