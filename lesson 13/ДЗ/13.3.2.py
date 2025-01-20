def countPlusToN(N):
    x = 1
    count = 0
    while True:
        if x < 2:
            x += N
            count += 1
        else:
            break
    print('Кол-во прибавлений:', count)

N = float(input('Введите число в эксп. форме: '))
countPlusToN(N)