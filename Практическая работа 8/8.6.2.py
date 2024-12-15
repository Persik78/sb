debetors = int(input('Кол-во должников: '))
arrears = 0
for debetor in range(0, debetors, 5):
    print('Задолжник с номером: ', debetor)
    arrear = int(input('Сколько должны? : '))
    arrears += arrear
print('Общая сумма долга: ', arrears)