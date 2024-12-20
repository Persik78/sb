wrong_answer = 0
for students in range(5):
    answer = input('Кто написал Евгения Онегина? ')
    if answer == 'Пушкин' or answer == 'пушкин':
        print('Верно!')
        break
    print('Неправильно! Два!')
    wrong_answer += 1
print('Всего двоек:', wrong_answer)