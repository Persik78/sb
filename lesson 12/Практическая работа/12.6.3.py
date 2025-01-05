def summ(N):
    summa = 0
    while N != 0 and N >= 1:
        summa += N % 10
        N //= 10
    print(summa)

def max(N):
    maxFigure = 0
    while N != 0 and N >= 1:
        if N % 10 > maxFigure:
            maxFigure = N % 10
        N //= 10
    print(maxFigure)

def min(N):
    minFigure = 9
    while N != 0 and N >= 1:
        if N % 10 < minFigure:
            minFigure = N % 10
        N //= 10
    print(minFigure)

while True:
    N = int(input('Введите число: '))
    action = int(input('1 - Сумма его цифр, 2 - максимальная цфира, 3 минимальная цифра: '))
    if action == 1:
        summ(N)
    elif action == 2:
        max(N)
    elif action == 3:
        min(N)
    else:
        print('Такого действия несуществует.')