stipendia = int(input('Введите стипендию: '))
rashod = int(input('Введите расходы на проживание: '))
count = 0
procent = 0
for month in range(1, 11, 1):
    if month != 1:
        procent = rashod * 3 / 100
        rashod += procent
    count += rashod - stipendia
    print('месяц траты ', rashod, ' не хватает ', count)
print('Нужно попросить у родителей ', count, ' рублей')