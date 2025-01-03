import math

distance = int(input('Введите расстояние: '))
angle = int(input('Введите угол: '))

x = round(distance * math.cos(angle), 2)
y = round(distance * math.sin(angle), 2)

print('Новое место положение: ', x, y)