for row in range(20):
    for col in range(30):
        if row == 0 or row == 19:
            print('-', end = '')
        elif col == 0 or col == 29:
            print('|', end = '')
        else:
            print(' ', end = '')
    print()