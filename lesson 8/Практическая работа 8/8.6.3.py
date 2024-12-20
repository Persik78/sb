reverse_timer = int(input('Сколько секунд греем? '))
for timer in range(reverse_timer, -1, -1):
    completion = int(input('0/1? 0 - Net, 1 - Da '))
    if completion == 1:
        print('Ваша еда готова, можете забрать')
        break
    elif completion != 0:
        print('Хуйня')
    if timer == 0:
        print('Ваша еда готова, осторожно горячo!')
    else:
        print('Осталось секунд: ', timer)
