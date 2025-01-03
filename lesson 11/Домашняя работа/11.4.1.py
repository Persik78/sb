import math

a = int(input('Введите 1 сторону треугольника: '))
b = int(input('Введите 2 сторону треугольника: '))
c = int(input('Введите 3 сторону треугольника: '))

p = (a+b+c) / 2

S = math.sqrt(p * (p-a)*(p-b)*(p-c))

print(S)