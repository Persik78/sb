import math

def myDistance(x, y):
    distance = math.sqrt(x**2 + y**2)
    print(distance)

def ourDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2- x1) ** 2 + (y2 - y1) ** 2)
    print(distance)

question = int(input('1 - посчитать расстояние до точки, 2 - посчитать расстояние между двумя точками '))

if question == 1:
    x = float(input('введите координаты икс: '))
    y = float(input('введите координаты игрек: '))
    myDistance(x, y)
elif question == 2:
    x1 = float(input('введите координаты икс 1: '))
    y1 = float(input('введите координаты игрек 1: '))
    x2 = float(input('введите координаты икс 2: '))
    y2 = float(input('введите координаты игрек 2: '))
    ourDistance(x1, y1, x2, y2)
else:
    print('некорректные данные')