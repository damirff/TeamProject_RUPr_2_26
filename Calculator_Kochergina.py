class Calculator:
    def __init__(self):
        self.history = []
        self.max_history = 5

    def calculate(self, expression: str) -> float:
        # Убираем пробелы, оставляем только разрешённые символы
        allowed = set("0123456789+-*/(). ")
        if any(ch not in allowed for ch in expression):
            raise ValueError("В выражении есть недопустимые символы.")

        # eval в контролируемых условиях: только арифметические операции
        try:
            result = eval(expression, {"__builtins__": {}}, {})
        except ZeroDivisionError:
            raise ZeroDivisionError("Деление на ноль.")
        except Exception as e:
            raise ValueError(f"Ошибка в выражении: {e}")

        return float(result)

    def add_to_history(self, expr: str, result: float):
        self.history.append(f"{expr} = {result}")
        if len(self.history) > self.max_history:
            self.history.pop(0)

    def show_history(self):
        if not self.history:
            print("История пуста.")
            return
        print("\n--- История вычислений ---")
        for line in self.history:
            print(line)
        print("--------------------------\n")


def main():
    calc = Calculator()
    print("Команды: 'h' — показать историю, 'q' — выйти.\n")

    while True:
        user_input = input("Введите выражение: ").strip()

        if user_input.lower() == "q":
            print("До свидания!")
            break
        elif user_input.lower() == "h":
            calc.show_history()
            continue
        elif not user_input:
            continue

        try:
            result = calc.calculate(user_input)
            print(f"Результат: {result}\n")
            calc.add_to_history(user_input, result)
        except ValueError as ve:
            print(f"Ошибка ввода: {ve}\n")
        except ZeroDivisionError as ze:
            print(f"Математическая ошибка: {ze}\n")


if __name__ == "__main__":
    main()
