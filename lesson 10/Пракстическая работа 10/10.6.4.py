numbers = int(input('Введите кол-во чисел: '))

for numbers_count in range(numbers):
    number = int(input('Введите число: '))
    for simple_num in range(2, number):
        if number % simple_num == 0:
            numbers -= 1
            break
    print()
print('Кол-во простых чисел: ', numbers)
