a = 8
b = 10

while True:
    print('Марсоход находится на позиции', a,',',b, end = '')
    question = input(', введите команду: ')
    if question == 'A' and a > 0:
        a -= 1
    elif question == 'W' and b < 20:
        b += 1
    elif question == 'D' and a < 15:
        a += 1
    elif question == 'S' and b > 0:
        b -= 1

