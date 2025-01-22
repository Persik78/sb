S = list(input('Введите строку: '))

new_S = []
count = 0
count_replace = 0
print('Исправленная строка: ', end='')
for i in S:
    if i == ':':
        S[count] = ';'
        count_replace += 1
    print(S[count], end='')
    count += 1

print('\nКол-во замен:', count_replace)