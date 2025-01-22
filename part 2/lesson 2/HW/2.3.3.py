word_list = []
counts = [0, 0, 0]

for i in range(3):
    print('Введите', i+1, end='')
    word = input(' слово: ')
    word_list.append(word)

text = input('Слово из текста: ')
while text != 'end':
    for i in range(3):
        if word_list[i] == text:
            counts[i] += 1
    text = input('Слово из текста: ')

print('Подсчёт слов в тексте')
for i in range(3):
    print(word_list[i],':', counts[i])