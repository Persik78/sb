awake = int(input('Во сколько встал? '))
water = 0
call_sum = 0
for ne_sput in range(awake, 23, 3):
    print('Время: ', ne_sput)
    call = int(input('Сколько съел? '))
    call_sum += call
    water += 1
print('Воды выпито: ', water)
print('Каллроий съедено: ', call_sum)
