def maximum_of_two(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return b

def maximum_of_three(c):
     if maximum_of_two(a, b) < c:
         return c
     elif maximum_of_two(a, b) > c:
         return maximum_of_two(a, b)
     else:
         return c

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(maximum_of_two(a, b))
c = int(input('Введите третье число: '))
print(maximum_of_three(c))