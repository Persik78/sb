def NOD(a, b):
    minNum = 0
    maxNum = 0
    NOD = 0
    if a > b or a == b:
        minNum = b
        maxNum = a
    else:
        minNum = a
        maxNum = b
    if maxNum % minNum == 0:
        print('НОД: ', minNum)
    else:
        for i in range(1, minNum):
           if minNum % i == 0 and maxNum % i == 0:
               NOD = i
        print('НОД: ',NOD)


    #for i in range(minNum+1):




a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
NOD(a, b)
