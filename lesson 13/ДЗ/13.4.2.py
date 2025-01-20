from decimal import Decimal


def eqv(a, b, c):
    if a+b == c:
        return True
    else:
        return False

a = Decimal(input('Введите первое число: '))
b = Decimal(input('Введите второе число: '))
c = Decimal(input('Введите третье число: '))
print(eqv(a, b, c))