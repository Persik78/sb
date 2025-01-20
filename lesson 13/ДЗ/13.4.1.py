def sumTax(tax, new_tax):
    all_tax = tax + new_tax
    if all_tax == tax:
        print('Результат: Бюджет не изменится')
    else:
        print('Результат: Бюджет увеличится')

tax = float(input('Введите бюджет страны: '))
new_tax = float(input('Новые поступления (налог): '))
sumTax(tax, new_tax)
