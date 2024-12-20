text = input('Введите текст: ')
count = 0
for symbol in text:
    if symbol == ' ':
        count = 0
        continue
    count += 1
print('Самое длинное слово, ', count)
