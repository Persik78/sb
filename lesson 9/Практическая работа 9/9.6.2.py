text = input('введите текст: ')
count = 1
for count_text in text:
    if count_text == '*' :
        print('Символ «*» стоит на позиции ', count)
    count += 1