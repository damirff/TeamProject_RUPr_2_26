
print("Добро пожаловать в калькулятор!")
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Нельзя делить на ноль!")
    return a / b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def main():
    operations = {
        "1": ("Сложение", add),
        "2": ("Вычитание", subtract),
        "3": ("Умножение", multiply),
        "4": ("Деление", divide),
        "5": ("Возведение в степень", power)
    }

    while True:
        print("\n--- Простой калькулятор ---")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("0. Выход")

        choice = input("Выберите операцию: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        if choice not in operations:
            print("Неверный выбор, попробуйте снова.")
            continue

        _, func = operations[choice]
        num1 = get_number("Введите первое число: ")
        num2 = get_number("Введите второе число: ")

        try:
            result = func(num1, num2)
            print(f"Результат: {result}")
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main()
