def devide(a):
    count_devide = 0
    while True:
        if a != 0:
            print('Деление', a, end=' ')
            a /= 2
            count_devide += 1
            print('на 2, =', a)
        else:
            print('Кол-во делений на 2:', count_devide)
            break

num = int(input('введите число: '))
devide(num)