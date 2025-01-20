def summa_n(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print('Сумма от 1 до', n, '=', sum)
    return sum

number = int(input('Введите число: '))
summa_n(summa_n(number))