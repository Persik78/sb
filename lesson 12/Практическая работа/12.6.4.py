def reverse(N):
    count = 0
    NN = N
    while N != 0 and N >= 1:
        count += 1
        N //= 10
    print('Число наоборот: ', end='')
    for reverseNum in range(count):
        print(NN%10, end='')
        NN //= 10
    print()

while True:
    N = int(input('Введите число: '))
    if N == 0:
        print('Программа завершена!')
    else:
        reverse(N)