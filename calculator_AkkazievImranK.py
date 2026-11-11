print("Простой калькулятор")
print("Поддерживаемые операции: +, -, *, /")

while True:
    try:
        first = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        second = float(input("Введите второе число: "))

        if operation == '+':
            result = first + second
        elif operation == '-':
            result = first - second
        elif operation == '*':
            result = first * second
        elif operation == '/':
            if second == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = first / second
        else:
            print("Ошибка: неверная операция!")
            continue

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: введите число!")

    again = input("Хотите продолжить? (y/n): ").strip().lower()
    if again != 'y':
        print("До свидания!")
        break
