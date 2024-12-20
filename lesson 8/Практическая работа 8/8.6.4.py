a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if a > b:
    b -= 1
    d = -1
elif a < b:
    b += 1
    d = 1
avg_sum = 0
count = 0
for avg in range(a, b, d):
    if avg % c == 0:
        print(avg)
        avg_sum += avg
        count += 1
print(avg_sum/count)
print(count, avg_sum)