firstNumber = float(input('Введите первое число: '))
secondNumber = float(input('Введите второе число: '))

sumRaz = (firstNumber + secondNumber + abs(firstNumber - secondNumber)) / 2

print(round(sumRaz, 1))