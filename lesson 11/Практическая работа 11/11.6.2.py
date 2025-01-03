import math

numbers_count = int(input('Сколько будет чисел? '))
for n in range(numbers_count):
    number = float(input('Введите число: '))
    if number > 0:
        number = math.ceil(number)
        log = math.log(number)
        print('x =', number, 'log(x) =', log)
    elif number < 0:
        number = math.floor(number)
        exp = math.exp(number)
        print('x =', number, 'exp(x) =', exp)
    else:
        print('0? Ты еблан?')


