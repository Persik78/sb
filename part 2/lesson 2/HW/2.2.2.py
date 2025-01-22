N = int(input('Введите кол-во чисел: '))
number_list = []

for i_num in range(N):
    print('Введите', i_num + 1, 'число: ', end='')
    num = int(input())
    number_list.append(num)

divider = int(input('Введите делитель: '))
sum = 0

for number in range(N):
    if number_list[number] % divider == 0:
        print('Индекс числа', number_list[number],':', number)
        sum += number
print('Сумма индексов:', sum)