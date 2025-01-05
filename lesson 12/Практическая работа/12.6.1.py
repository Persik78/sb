def summa_n(n):
    if n < 1:
        print('N положительное')
    else:
        sum = 0
        for num in range(1, n+1):
            sum += num
        print('Я знаю, что сумма чисел от 1 до', n, 'равна', sum)

n = int(input('введите значение N: '))
summa_n(n)