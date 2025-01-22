dogs_count = int(input('Введите кол-во собак: '))
dogs_list = []

for i_dog in range(dogs_count):
    print('Введите кол-во очков', i_dog + 1, 'собаки: ', end='')
    num = int(input())
    dogs_list.append(num)

max = dogs_list[0]
min = dogs_list[0]
i_max = 0
i_min = 0

for i in range(dogs_count):
    if max < dogs_list[i]:
        max = dogs_list[i]
        i_max = i

    if min > dogs_list[i]:
        min = dogs_list[i]
        i_min = i

for i in range(dogs_count):
    if i == i_max:
        dogs_list[i] = min

    if i == i_min:
        dogs_list[i] = max

print(dogs_list)