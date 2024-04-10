# Программа для сравнения 3 чисел и нахождения максимального и минимального числа
def find_max_min(num1, num2, num3):
    # Находим максимальное число
    if num1 >= num2 and num1 >= num3:
        max_num = num1
    elif num2 >= num1 and num2 >= num3:
        max_num = num2
    else:
        max_num = num3

    # Находим минимальное число
    if num1 <= num2 and num1 <= num3:
        min_num = num1
    elif num2 <= num1 and num2 <= num3:
        min_num = num2
    else:
        min_num = num3

    return max_num, min_num


# Ввод трех чисел
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Вызов функции и вывод результатов
max_number, min_number = find_max_min(num1, num2, num3)
print(f"Максимальное число: {max_number}")
print(f"Минимальное число: {min_number}")