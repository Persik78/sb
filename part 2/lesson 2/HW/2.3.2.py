S = list(input('Введите строку: '))
index_symbol = int(input('Номер символа: '))

print('Символ слева:', S[index_symbol-2])
print('Символ сcghfdf:', S[index_symbol])

if S[index_symbol-2] == S[index_symbol-1] and S[index_symbol] == S[index_symbol-1]:
    print('Есть два таких же.')
elif S[index_symbol-2] == S[index_symbol-1] or S[index_symbol] == S[index_symbol-1]:
    print('Есть ровно один такой же символ.')
else:
    print('Таких же символов нет.')