def numeral_count(num):
    figure_for_num = 0
    while num != 0:
        figure_for_num += 1
        num //= 10
    return figure_for_num



count_task = int(input('Введите кол-во задач: '))
max_figure_for_num = 0
max_num = 0
for figure in range(count_task):
    num = int(input('Введите число: '))
    if max_figure_for_num < numeral_count(num):
        max_figure_for_num = numeral_count(num)
        max_num = num

print('Первая задача на обработку: ', max_num)

