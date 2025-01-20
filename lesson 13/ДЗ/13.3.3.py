def floattt(N):
    a = N
    count = 0
    print('Формат плавающей точки: x =', end=' ')
    while True:
        if N > 0:
            count += 1
            N //= 10
            #print(N)
        else:
            break
    for floater in range(count-1):
        a /= 10
    print(a, '* 10 **', count-1)

N = int(input('введите число больше 10: '))
if N > 10:
    floattt(N)
else:
    print('Хуйню ввел бразе, иди траву потрогай')