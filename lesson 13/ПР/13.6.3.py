def reverse(a,b):
    n = ''
    c = ''
    for rev in reversed(a):
        n += rev

    for rev2 in reversed(b):
        c += rev2

    print('Первое число наоборот:', n)
    print('Второе число наоборот:', c)

    sum = int(c) + int(n)
    print('Сумма:', sum)
    print('Сумма наоборот: ', end='')
    for rev_sum12 in reversed(str(sum)):
        print(rev_sum12, end='')

a = input('Введите первое число: ')
b = input('Введите второе число: ')
reverse(a,b)
#print(summa(a, b))