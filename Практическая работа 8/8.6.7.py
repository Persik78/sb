n = int(input('Введите число n: '))
step = 1
sum = 0
if n < 0:
    step = -step

for iteration in range(0, n, step):
    elem = (-1) ** iteration * (1 / (2**iteration))
    sum += elem
    print(iteration, elem)

print('Сумма: ', sum)