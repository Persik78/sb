start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
for dot in range(end, start-1, step):
    y = dot**3 + (2 * dot**2) - (4 * dot) + 1
    print('В точке ', dot, 'функция равна ', y)