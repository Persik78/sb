import math

x = float(input('Введите положительное действительно число: '))

first = int(round(x - int(x), 1) * 10)

print('Первая цифра после запятой: ', first)