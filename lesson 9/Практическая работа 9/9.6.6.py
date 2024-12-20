text = input('Введите строку :')
milk = 0
count = 1
for count_sloila in text:
    if count_sloila == 'b':
        milk += 2 * count
    count += 1
print('Всего будет молока :', milk)