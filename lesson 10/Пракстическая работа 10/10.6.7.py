levels = int(input("Введите количество уровней пирамиды: "))
current_odd_number = 1

for i in range(levels):
    space_count = levels - i
    print('  ' * space_count, end='')

    for j in range(i + 1):
        print(current_odd_number, end='  ')
        current_odd_number += 2

    print()