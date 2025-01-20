def pendulum(start, amplitude):
    count = 0
    while start > amplitude:
        count += 1
        start -= start * 8.4 / 100
    return count

start =float(input('Введите начальную амплитуду: '))
amplitude = float(input('Введите амплитуду остановки: '))
print('Маятник считается остановившимся через', pendulum(start, amplitude), 'колебаний')