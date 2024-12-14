count_chair = int(input('Сколько стульев? '))
chair_sum = 0
for count in range(1, count_chair + 1, 5):
    print('Номер стула: ', count)
    chair_sum += count
print('Сумма номеров: ', chair_sum)