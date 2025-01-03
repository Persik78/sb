weight = float(input('Какой вес? '))
height = float(input('Какой рост? '))

index = weight / height ** 2

if index < 18.5:
    print('Недобор')
elif index < 25:
    print('Все норм')
elif index < 30:
    print('Избыток')
else:
    print('Жирный епт')