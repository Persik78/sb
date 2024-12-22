num = int(input())
for row in range(num, 0, -1):   #1, num+1
    for col in range(num, 0, -1):   #num, 0, -1
        if col < row:
            print('-', end='')
        else:
            print(col, end = '')
    for col2 in range(1, num+1):   #num, 0, -1
        if col2 < row:
            print('-', end='')
        else:
            print(col2, end = '')
    print()
