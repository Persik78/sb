crypt = input('Введите зашифрованное слово: ')
uncrypt_word = ''
uncrypt_word_2 = ''
count_symbol = 1

for count in crypt:
    if count_symbol % 2 == 1:
        uncrypt_word += count
    else:
        uncrypt_word_2 = count + uncrypt_word_2
    count_symbol += 1

print(uncrypt_word + uncrypt_word_2)

