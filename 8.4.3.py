count_seconds = int(input('Кол-во секунд: '))
for wait in range(count_seconds // 2, 0, -1):
    print(wait * 2 - 1)
print('Я иду искать!')