import math

number = float(input('Введите число: '))

print('Округление вниз: ', math.floor(number))
print('Округление вверх: ', math.ceil(number))
print('Модуль числа: ', abs(number))
print('Извлечение квадратного корня: ', math.sqrt(number))
print('Возводит экспоненту в степень, равную числу: ', math.exp(number))
print('Считает натуральный логарифм числа: ', math.log(number))
print('Считает логарифм числа по основанию 2: ', math.log(number, 2))
print('Считает логарифм числа по основанию 10: ', math.log(number, 10))
print('Косинус: ', math.cos(number), 'Синус: ', math.sin(number))

if number > 0 and number.is_integer():
    print('Факториал числа', int(number), ': ', math.factorial(int(number)))
