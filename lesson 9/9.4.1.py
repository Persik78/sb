for board in range(1, 62):
    if board < 10 or board > 51:
        print('-', end = '')
    elif board == 11:
        print('-', end = '\n')
    elif board == 12 or board == 22 or board == 32 or board == 42:
        print('|', end = '')
    elif board == 21 or board == 31 or board == 41 or board == 51:
        print('|', end = '\n')
    elif 12 < board < 21 or 22 < board < 31 or 32 < board < 41 or 42 < board < 51:
        print('0', end = '')