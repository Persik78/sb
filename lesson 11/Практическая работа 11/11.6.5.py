import math

radius = float(input('Введите предпологаемый радиус: '))
earth = 1.08321 * 10 ** 12
v = (4/3) * math.pi * radius**3

if earth > v:
    print('Объём планеты Земля больше в ', round(earth / v, 3), 'раз')
elif earth < v:
    vv = round(v / earth, 3)
    print('Объём планеты Земля меньше в (1/', round(earth / v, 3), ') =', vv, 'раз')
else:
    print('равны')