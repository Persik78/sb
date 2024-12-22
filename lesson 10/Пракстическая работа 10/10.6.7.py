levels = int(input("Введите количество уровней пирамиды: "))
current_odd_number = 1

for i in range(levels):
    print(' ' * (levels - i - 1), end='')

    for j in range(i + 1):
        print(current_odd_number, end=' ')
        current_odd_number += 2

    print()