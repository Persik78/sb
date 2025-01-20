def danger_level(x):
    return x**3 - 3*x**2 - 12*x + 10

def find_safe_depth(tolerance):
    low, high = 0, 4
    while high - low > tolerance:
        mid = (low + high) / 2
        if danger_level(mid) > 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

def main():
    while True:
        try:
            tolerance = float(input("Введите максимально допустимый уровень опасности: "))
            if tolerance <= 0 or tolerance >= 4:
                raise ValueError("Уровень опасности должен быть больше 0 и меньше 4.")
            break
        except ValueError as e:
            print(e)

    safe_depth = find_safe_depth(tolerance)
    danger_at_safe_depth = danger_level(safe_depth)
    print(f"Приблизительная глубина безопасной кладки: {safe_depth:.9f} м")
    print(f"Уровень опасности на этой глубине: {danger_at_safe_depth:.9f}")

main()