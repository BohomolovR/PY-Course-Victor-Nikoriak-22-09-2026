# Task 1


# AI log: not used


def numbers():
    while True:
        try:
            a = int(input("Введите число a:"))
            b = int(input("Введите число b:"))
            result = a**2 / b
        except ValueError:
            print("Введите число!!")
        except ZeroDivisionError:
            print("Нельзя делить на ноль введите новое число!!!")
        else:
            return result



print(numbers())