import math


# функция для каждой операции
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль"
    return x / y


def power(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Ошибка: квадратный корень из отрицательного числа"
    return math.sqrt(x)


def factorial(x):
    if x < 0:
        return "Ошибка: факториал отрицательного числа"
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


# функция для получения и проверки чисел
def correct_value(value):
    while True:
        try:
            user_input = float(input(value))
            return user_input
        except ValueError:
            print("Ошибка: введите корректное числово")


# главная функция
def main():
    print("Добро пожаловать в инженерный калькулятор!")

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("11. Выход")

        choice = int(input("Введите номер операции: "))
        # выбор операции
        if choice == 11:
            print("До свидания!")
            break

        if choice < 1 or choice > 10:
            print("Ошибка: неверный выбор операции")
            continue
        # перебор операция для которых нужно только одно число
        if choice in [6, 7, 8, 9, 10]:
            num = correct_value("Введите число: ")
        # перебор операций для которых нужно два числа
        if choice in [1, 2, 3, 4, 5]:
            num1 = correct_value("Введите первое число: ")
            num2 = correct_value("Введите второе число: ")

        # выбор функции под выбранную операцию и вычисление результата
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        elif choice == 5:
            result = power(num1, num2)
        elif choice == 6:
            result = square_root(num)
        elif choice == 7:
            result = factorial(int(num))
        elif choice == 8:
            result = sin(num)
        elif choice == 9:
            result = cos(num)
        elif choice == 10:
            result = tan(num)

        print("Результат:", result)


# Запуск основной функции, если программа запущена как отдельный файл
if __name__ == "__main__":
    main()
