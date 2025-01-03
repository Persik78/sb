height = int(input('Введите высоту пирамидки? '))
for row in range(1, height + 1):
    for col in range(1, height * 2 + 1):
        if col != height - row + 1:
            print(' ', end = '')
        else:
            print('#' * (row * 2 - 1), end = '')
    print()
