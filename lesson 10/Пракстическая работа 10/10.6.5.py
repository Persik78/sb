numbers = int(input('Введите кол-во чисел: '))
max_sum = 0
max_number = 0

for num in range(numbers):
    number = int(input('Введите число: '))
    numbeer = number
    sum = 0
    while True:
        if number > 0:
            sum += number % 10
            number //= 10
        elif sum > max_sum:
            max_sum = sum
            max_number = numbeer
        else:
            break

print(max_number, max_sum)