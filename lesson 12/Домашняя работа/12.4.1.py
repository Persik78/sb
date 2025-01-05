def avg(a, b):
    if a >= b:
        print('a должна быть меньше b')
    else:
        count = 0
        sum = 0
        for avgC in range(a, b+1):
            sum += avgC
            count += 1
        avg = sum / count
        print(avg)

firstnumber = int(input('введите значение a: '))
secondnumber = int(input('введите значение b: '))
avg(firstnumber, secondnumber)