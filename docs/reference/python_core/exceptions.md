# Довідник: Exceptions & Error Handling

Короткий довідник по обробці винятків у Python. Повний, поступово побудований конспект із наскрізним сценарієм — [Урок 13. Виключення](../../modules/m1/lesson_13.md).

## Синтаксис

```python
try:
    result = risky()
except ValueError as e:        # конкретний тип + об'єкт помилки
    handle(e)
except (KeyError, IndexError): # кілька типів разом
    handle_missing()
except ZeroDivisionError:
    handle_zero()
else:                          # тільки якщо try пройшов без помилок
    use(result)
finally:                       # завжди — очищення ресурсів
    cleanup()
```

## Шість головних винятків

| Виняток | Коли виникає | Типовий приклад |
|---------|-------------|-----------------|
| `ValueError` | Правильний тип, некоректне значення | `int("abc")` |
| `TypeError` | Несумісні типи в операції | `"x" + 5` |
| `ZeroDivisionError` | Ділення на нуль | `10 / 0` |
| `IndexError` | Індекс списку поза межами | `lst[99]` (3 елементи) |
| `KeyError` | Ключ відсутній у словнику | `d["missing"]` |
| `FileNotFoundError` | Файл не знайдено | `open("ghost.txt")` |

## `raise` — генерація власного винятку

```python
def validate_age(age: int) -> int:
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(e)   # Вік не може бути від'ємним
```

## Поширення помилок (Stack Unwinding)

```text
function_a()  ← try/except тут
    └── function_b()  ← немає обробника
            └── function_c()  ← 💥 виняток тут

Виняток піднімається: C → B → A → перехоплено ✅
```

Якщо ніхто не перехопить — програма падає з Traceback.

## EAFP проти LBYL

```python
# LBYL (не рекомендується в Python)
if key in my_dict:
    value = my_dict[key]

# EAFP (Python-стиль ✅)
try:
    value = my_dict[key]
except KeyError:
    handle_missing()
```

## Антипатерн: «голий» `except`

```python
# ❌ ПОГАНО — ховає всі баги, включно з опечатками
try:
    do_something()
except:
    pass

# ✅ ПРАВИЛЬНО — явно вказуємо, що перехоплюємо
try:
    do_something()
except ValueError:
    handle_value_error()
```

## Ієрархія винятків (спрощено)

```text
BaseException
├── KeyboardInterrupt   ← Ctrl+C
├── SystemExit          ← sys.exit()
└── Exception           ← усі звичайні помилки
    ├── ValueError
    ├── TypeError
    ├── ZeroDivisionError
    ├── IndexError
    ├── KeyError
    ├── FileNotFoundError
    └── ...
```

!!! warning
    Ніколи не ловіть `BaseException` або голий `except` — це перехоплює навіть `KeyboardInterrupt` та `SystemExit`.

## Далі

Контекстні менеджери (`with`), які гарантують `finally`-подібне закриття ресурсу навіть при винятку, розкриті в [Довідник: File I/O та JSON](file_io_json.md) і в [Уроці 14](../../modules/m1/lesson_14.md).
