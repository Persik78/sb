def main():
    first_n = int(input("Введите первое число: "))
    if first_n < 100:
        print("В первом числе меньше трех цифр или оно меньше нуля")
        main()
    else:
        second_n = int(input("Введите второе число: "))
        if second_n < 1000:
            print("В втором числе меньше четырех цифр или оно меньше нуля")
            main()
        else:
            first = change_number(count_numbers(first_n), first_n)
            second = change_number(count_numbers(second_n), second_n)
            print('Изменённое первое число:', first, '\nИзменённое второе число:', second, '\nСумма чисел:', first + second)

def count_numbers(num):
    num_count = 0
    temp = num
    while temp > 0:
        num_count += 1
        temp = temp // 10
    return num_count

def change_number(count_num, num):
    last_digit = num % 10
    first_digit = num // 10 ** (count_num - 1)
    between_digits = num % 10 ** (count_num - 1) // 10
    num = last_digit * 10 ** (count_num - 1) + between_digits * 10 + first_digit
    return num

main()