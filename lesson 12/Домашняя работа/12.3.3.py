def is_prime(n):
    if n <= 1:
        print('Непростое', n)
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print('Непростое', n)
            return False
    print('Простое', n)
    return True

n = int(input('Введите кол-во чисел в последовательности: '))

for num in range(n+1):
    is_prime(num)
