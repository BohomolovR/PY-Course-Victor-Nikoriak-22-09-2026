# Task 4

# AI log: not used

def _add(a, b):
    return a + b


def _sub(a, b):
    return a - b


def _mul(a, b):
    return a * b


def _div(a, b):
    if b != 0:
        return a / b
    raise ZeroDivisionError("На ноль делить нельзя")


def _squ(a, b):
    return a ** b


def operation_mapper(operation):
    if operation == "+":
        return _add
    elif operation == "-":
        return _sub
    elif operation == "*":
        return _mul
    elif operation == "/":
        return _div
    elif operation == "**":
        return _squ
    else:
        raise ValueError(f"{operation!r}-такой операции нет")


print(operation_mapper("/")(1, 0))  # выводит 2
print(operation_mapper("%")(1, 3))

# Деление на ноль должен обрабатывать вызывающий код,
# потому что operation_manager только возвращает функцию,
# а ошибка возникает позже, при ее вызове
