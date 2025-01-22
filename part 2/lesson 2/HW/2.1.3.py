count_worker = int(input('Кол-во сотрудников в офисе: '))
ID_worker = []
for _ in range(count_worker):
    ID = int(input('ID сотрудника: '))
    ID_worker.append(ID)

while True:
    b = 0
    search_ID = int(input('Какой ID ищем? '))
    for i in ID_worker:
        if i == search_ID:
            b = 1
    if b == 1:
        print('Сотрудник на месте!')
    else:
        print('Сотрудник не работает!')