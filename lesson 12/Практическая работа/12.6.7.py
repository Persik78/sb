import random

# Здесь будет игра «Камень, ножницы, бумага»
def rock_paper_scissors():
    a = random.randint(1,3)
    print(a)
    choiceInt = 0
    while True:
        choice = input('Камень, ножницы или бумага? ')
        if choice == 'Камень' or choice == 'камень':
            choiceInt = 1
            break
        elif choice == 'Ножницы' or choice == 'ножницы':
            choiceInt = 2
            break
        elif choice == 'Бумага' or choice == 'бумага':
            choiceInt = 3
            break
        else:
            print('говно, переделвыай')
    if choiceInt == a:
        print('Ничья')
        mainMenu()
    elif (choiceInt == 1 and a == 2) or (choiceInt == 2 and a == 3) or (choiceInt == 3 and a == 1):
        print('Поздравляю красава!')
        mainMenu()
    else:
        print('Лох!!! Пидр!!!')
        mainMenu()

def guess_the_number():
  # Здесь будет игра «Угадай число»
    a = random.randint(1, 99)
    while True:
        figure = int(input('введите число: '))
        if figure == a:
            print('Молодец! Угадал!')
            mainMenu()
        else:
            if figure > a:
                print('Введенное число больше')
            else:
                print('Введенное число меньше')
            print("Лох! Пидр!")

def mainMenu():
  # Здесь главное меню игры
    choice = int(input('Выбери: 1 - Камень, ножницы, бумага, 2 - Угадай число: '))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print('Написал хуйню')
        mainMenu()




mainMenu()