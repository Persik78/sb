word = input('Введите слово: ')
reverse_word = ''

for reverse in word:
    reverse_word = reverse + reverse_word
    print(reverse_word)

if word == reverse_word:
    print('Да, это палиндром!')
else:
    print('Нет, это не палиндром!')