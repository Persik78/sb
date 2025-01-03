people_count = int(input('Введите кол-во людей в очереди: '))

for hour in range(people_count+1):
    print('Идет час: ', hour)
    for num in range(hour, people_count):
        print('Номер в очереди: ', num)
    print()

print('Очередь обслуженна!')