# Python Helper Toolkit: інтроспекція, дебаг і вбудовані функції

Практичний набір інструментів для дослідження об'єктів, дебагу коду та розуміння пам'яті Python — плюс каталог часто вживаних вбудованих функцій (`sum`, `zip`, `map`, `sorted`, модуль `random` тощо). Це довідник: читайте розділ, коли він потрібен саме зараз, а не як лекцію від початку до кінця.

## Інтроспекція — дослідження Python зсередини

Інтроспекція — це можливість програми досліджувати саму себе під час виконання: дізнатися тип об'єкта, список його методів, чи є два імені насправді одним і тим самим об'єктом у пам'яті.

### `dir(object)` — усі атрибути та методи об'єкта

```python
all_str_methods = dir("hello")
print(f"Рядок має {len(all_str_methods)} атрибутів/методів")

# Фільтруємо магічні методи (dunder) — показуємо тільки звичайні
normal_methods = [name for name in dir("hello") if not name.startswith("__")]
print("\nЗвичайні методи рядка:")
print(normal_methods)

# Те саме для списку
list_methods = [name for name in dir([]) if not name.startswith("__")]
print("\nМетоди списку:")
print(list_methods)
```

```text
Рядок має 81 атрибутів/методів

Звичайні методи рядка:
['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs',
 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii',
 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

Методи списку:
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
 'remove', 'reverse', 'sort']
```

### `help(object)` — вбудована документація

```python
help(str)
help(str.join)

words = ["Hello", "World"]
print(" ".join(words))
```

```text
Hello World
```

`help(str.join)` показує сигнатуру та документацію методу прямо в консолі — не потрібно шукати в інтернеті, щоб згадати порядок аргументів.

### `type(object)` — тип об'єкта

```python
print(type(42))
print(type(3.14))
print(type("hello"))
print(type([1, 2, 3]))
print(type(True))
```

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'bool'>
```

Щоб отримати лише ім'я типу, а не весь `<class '...'>`:

```python
print(type(42).__name__)
```

```text
int
```

### `isinstance(object, classinfo)` — правильний спосіб перевірки типу

```python
value = True

print(isinstance(value, bool))
print(isinstance(value, int))  # bool успадковує int
```

```text
True
True
```

`isinstance()` кращий за порівняння `type(x) == ...`, бо враховує наслідування класів:

```python
value = [1, 2, 3]

if isinstance(value, list):
    print("Це список — підрахуємо суму:", sum(value))
elif isinstance(value, str):
    print("Це рядок — перевернемо:", value[::-1])
elif isinstance(value, (int, float)):  # можна передати кортеж типів!
    print("Це число — зведемо в квадрат:", value ** 2)

print("\nПеревірка bool:")
print("type(True) == int:", type(True) == int)          # False
print("isinstance(True, int):", isinstance(True, int))  # True! bool успадковує int
```

```text
Це список — підрахуємо суму: 6

Перевірка bool:
type(True) == int: False
isinstance(True, int): True
```

`bool` — підклас `int` (`True == 1`, `False == 0`), тому `type(True) == int` дає `False` (типи не збігаються буквально), а `isinstance(True, int)` дає `True` (враховує спадкування). Якщо логіка залежить від типу вхідних даних — використовуйте `isinstance()`, а не пряме порівняння `type()`.

### `id(object)` і `is` — той самий об'єкт чи просто однакове значення?

```python
a = 5
b = 5

print("id(a):", id(a))
print("id(b):", id(b))
print("a is b:", a is b)
```

```text
id(a): 11759912
id(b): 11759912
a is b: True
```

`id()` повертає унікальний ідентифікатор об'єкта в пам'яті (для CPython — фактично адресу). Малі цілі числа Python кешує, тому `a` і `b` тут — буквально один об'єкт. `is` перевіряє саме це: чи `id()` збігається, а не просто чи значення однакові (для цього є `==`, див. нижче).

## Дебаг-інструменти

Debug — це контроль, а не хаос: замість вгадування, де саме код поводиться не так, підключаємо конкретні інструменти.

### `print()` як базовий інструмент

```python
x = 10
y = 3

print("DEBUG → x =", x)
print("DEBUG → y =", y)
print("DEBUG → x/y =", x / y)
```

```text
DEBUG → x = 10
DEBUG → y = 3
DEBUG → x/y = 3.3333333333333335
```

### f-string для читабельного дебагу

```python
name = "Victor"
age = 30

print(f"DEBUG → name={name}, age={age}")
```

```text
DEBUG → name=Victor, age=30
```

Компактніше за конкатенацію рядків і одразу видно, яке значення якій змінній відповідає.

### `assert` — швидка перевірка, що все працює правильно

`assert` — це спосіб сказати програмі: «Я впевнений, що ця умова має бути `True`. Якщо ні — значить у коді баг. Зупиняй програму.»

**Простий приклад:**

```python
x = 5
assert x > 0
print("Everything is OK")
```

```text
Everything is OK
```

Умова `5 > 0` — `True`, тому програма продовжує роботу і друкує рядок.

А якщо умова неправильна:

```python
x = -1
assert x > 0
```

```text
AssertionError
```

Програма миттєво зупиняється — саме там, де умова порушена, а не десь далі, де це стане незрозумілим побічним ефектом.

**Коли реально використовувати `assert`:**

| Ситуація | Чи підходить `assert`? |
|---|---|
| Перевірка математичної логіки | ✅ Так |
| Внутрішній стан об'єкта | ✅ Так |
| Перевірка API під час розробки | ✅ Так |
| Перевірка прав доступу | ❌ Ні |
| Перевірка вводу користувача | ❌ Ні |

!!! warning "assert — не для перевірки зовнішніх даних"
    `assert` можна вимкнути прапорцем `-O` при запуску Python, і він тоді просто зникає з коду. Для прав доступу чи вводу користувача, де перевірка обов'язково повинна спрацювати, використовуйте звичайні `if`/`raise`, а не `assert`.

**Приклад з реального коду:**

```python
def apply_discount(price, discount):
    new_price = price * (1 - discount)

    # внутрішня гарантія
    assert 0 <= new_price <= price, "Некоректний розрахунок знижки!"

    return new_price

apply_discount(100, 2.0)
```

```text
AssertionError: Некоректний розрахунок знижки!
```

`discount=2.0` означає «знижка 200%» — очевидна помилка виклику. Через неї `new_price` стає від'ємним (`100 * (1 - 2.0) = -100`), і `assert` ловить цю логічну помилку одразу, замість того щоб від'ємна ціна тихо поповзла далі програмою.

### `repr()` — технічне представлення

`repr()` (від *representation*) повертає «офіційне», технічне рядкове представлення об'єкта — на відміну від `str()`/`print()`, які показують дані так, щоб було зрозуміло людині, `repr()` показує так, щоб було зрозуміло програмісту: що саме зберігається в пам'яті.

**Золоте правило `repr()`:** в ідеалі рядок, який повертає `repr()`, має виглядати як валідний Python-код — якщо його скопіювати й виконати (чи передати в `eval()`), має вийти точна копія об'єкта. Якщо це недоцільно — заведено повертати корисну інформацію в кутових дужках `<...>`.

```python
text = "Hello\nWorld"

print("print():")
print(text)

print("\nrepr():")
print(repr(text))
```

```text
print():
Hello
World

repr():
'Hello\nWorld'
```

`print()` виводить реальний перенос рядка, `repr()` показує `\n` буквально — так видно, що насправді зберігається в рядку, а не як він виглядає на екрані.

### `__repr__` — свій `repr()` для власних класів

За замовчуванням об'єкт власного класу друкується непоказово — ім'я класу й адреса в пам'яті:

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

my_car = Car("червоний", 15000)
print(my_car)
```

```text
<__main__.Car object at 0x7fd733510b60>
```

Щоб виправити це, визначте магічний метод `__repr__(self)`:

```python
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        # Повертаємо рядок, який виглядає як код виклику класу
        return f"Car({self.color!r}, {self.mileage!r})"

my_car = Car("червоний", 15000)
print(repr(my_car))
```

```text
Car('червоний', 15000)
```

Модифікатор `!r` у f-рядку (`{self.color!r}`) наказує Python застосувати `repr()` до самої змінної — тому текст `червоний` виводиться разом із лапками, і рядок справді виглядає як валідний виклик `Car(...)`.

### `vars()` — внутрішні атрибути об'єкта

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Anna", 25)
print(vars(p))
```

```text
{'name': 'Anna', 'age': 25}
```

`vars()` повертає словник `__dict__` об'єкта — усі його атрибути екземпляра одразу, зручно для дебагу без ручного перелічування полів.

## Модель пам'яті: imutable, mutable, копії

Це ключ до розуміння того, чому одні зміни «поширюються всюди», а інші — ні.

### Immutable-приклад

```python
x = 10
print("id before:", id(x))

x = x + 1
print("id after:", id(x))
```

```text
id before: 11760072
id after: 11760104
```

`id` змінився — `x = x + 1` не змінює число «на місці», а створює новий об'єкт і переприв'язує до нього ім'я `x`.

### Mutable-приклад

```python
lst = [1, 2, 3]
print("id before:", id(lst))

lst.append(4)
print("id after:", id(lst))
```

```text
id before: 140562255662656
id after: 140562255662656
```

`id` не змінився — `append()` змінює той самий об'єкт-список у пам'яті, а не створює новий.

### `==` проти `is`

```python
a = [1, 2]
b = [1, 2]

print("a == b:", a == b)
print("a is b:", a is b)
```

```text
a == b: True
a is b: False
```

`==` порівнює **значення** (вміст однаковий), `is` порівнює **ідентичність** (це буквально один і той самий об'єкт у пам'яті). Тут `a` і `b` — два різні списки з однаковим вмістом.

### Поверхнева копія

```python
original = [1, 2, 3]
copy_list = original.copy()

print("original id:", id(original))
print("copy id:", id(copy_list))
```

```text
original id: 140562255636992
copy id: 140562255630144
```

`.copy()` створює новий об'єкт — зміни в `copy_list` більше не зачіпають `original`. Але для **вкладених** структур (список списків) поверхневої копії часто недостатньо — вкладені об'єкти всередині все одно спільні.

### Глибока копія

```python
import copy

nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)

print("nested id:", id(nested))
print("deep id:", id(deep))
```

```text
nested id: 140562257314560
deep id: 140562255629760
```

`copy.deepcopy()` рекурсивно копіює й усі вкладені об'єкти, тому навіть вкладені списки в `deep` повністю незалежні від `nested`.

### Експеримент з посиланнями

```python
a = [1, 2, 3]
b = a

b.append(4)

print("a:", a)
print("b:", b)
```

```text
a: [1, 2, 3, 4]
b: [1, 2, 3, 4]
```

`b = a` не створює копію — `b` це просто ще одне ім'я для того самого об'єкта, на який уже вказує `a`. Зміна через `b` видно й через `a`, бо це один список.

### Фінальна ментальна модель

1. Змінна — це ім'я.
2. Ім'я вказує на об'єкт.
3. Об'єкти живуть у пам'яті.
4. Є mutable та immutable типи — mutable можна змінити «на місці» (той самий `id`), immutable — ні (будь-яка «зміна» створює новий об'єкт).

```text
a ──────► [1, 2, 3, 4]
b ──────┘
```

Обидва імені `a` і `b` вказують на один список — саме тому зміна через одне ім'я видна й через інше.

## Часто вживані вбудовані функції

### Математичні та агрегатні

#### `sum(iterable, start=0)`

Обчислює суму всіх елементів послідовності. Використовується для підрахунку загальних сум — вартість товарів у кошику, загальна кількість балів.

```python
prices = [50, 75, 30, 95]
total = sum(prices)
print("Ціни:", prices)
print("Загальна сума:", total)

# з початковим значенням
total_with_bonus = sum(prices, 100)
print("Сума зі стартовим значенням 100:", total_with_bonus)
```

```text
Ціни: [50, 75, 30, 95]
Загальна сума: 250
Сума зі стартовим значенням 100: 350
```

#### `min(iterable)` та `max(iterable)`

Повертають найменший і найбільший елемент. Пошук найдешевшого товару, найвищого балу, крайніх точок.

```python
scores = [72, 88, 55, 99, 61, 43]
print("Бали студентів:", scores)
print("Найвищий бал:", max(scores))
print("Найнижчий бал:", min(scores))

# також працюють з кількома окремими аргументами
print("Максимум з трьох чисел:", max(10, 25, 17))

# і з рядками — за алфавітним порядком
print(min(["banana", "apple", "cherry"]))
```

```text
Бали студентів: [72, 88, 55, 99, 61, 43]
Найвищий бал: 99
Найнижчий бал: 43
Максимум з трьох чисел: 25
apple
```

#### `abs(x)`

Абсолютне значення (модуль) — число без знаку мінус. Коли важлива лише величина відстані чи різниці, а не напрямок.

```python
difference = abs(10 - 25)
print("Різниця між 10 та 25:", difference)

temperature_diff = abs(-15 - 3)
print("Різниця температур:", temperature_diff, "градусів")

print(abs(-100), abs(0), abs(3.14))
```

```text
Різниця між 10 та 25: 15
Різниця температур: 18 градусів
100 0 3.14
```

#### `round(x, n)`

Округлює `x` до `n` знаків після коми. Фінансові розрахунки, форматування виводу.

```python
pi = 3.14159265
print("Pi повністю:", pi)
print("Pi до 2 знаків:", round(pi, 2))
print("Pi до 4 знаків:", round(pi, 4))
print("Pi до цілого:", round(pi))

price = 19.999
print(f"Ціна після округлення: {round(price, 2)} грн")

print("round(2.5):", round(2.5), " round(3.5):", round(3.5))
```

```text
Pi повністю: 3.14159265
Pi до 2 знаків: 3.14
Pi до 4 знаків: 3.1416
Pi до цілого: 3
Ціна після округлення: 20.0 грн
round(2.5): 2  round(3.5): 4
```

!!! note "«Банківське округлення»"
    `round(2.5)` дає `2`, а не `3` — Python округлює `.5` до **найближчого парного** числа (banker's rounding), а не завжди вгору. Це навмисно зменшує систематичне зміщення при масових округленнях, але часто дивує новачків — тримайте це в голові для фінансових розрахунків.

### Послідовності та цикли

#### `len(s)`

Довжина об'єкта — кількість елементів списку чи символів рядка. Валідація довжини пароля, обмеження циклів, розмір структури.

```python
users = ["Alice", "Bob", "Charlie", "Diana"]
print("Список користувачів:", users)
print("Кількість користувачів:", len(users))

password = "SuperSecret123"
print(f"\nПароль '{password}' має {len(password)} символів")
if len(password) >= 8:
    print("✅ Пароль достатньо довгий")
else:
    print("❌ Пароль надто короткий")

# для словника len() рахує кількість пар ключ-значення
print(len({"a": 1, "b": 2}))
```

```text
Список користувачів: ['Alice', 'Bob', 'Charlie', 'Diana']
Кількість користувачів: 4

Пароль 'SuperSecret123' має 14 символів
✅ Пароль достатньо довгий
2
```

#### `range(start, stop, step)`

Генерує послідовність цілих чисел від `start` до `stop` (не включаючи `stop`) із кроком `step`. Незамінна для циклів `for`.

```python
print("range(5):", list(range(5)))
print("range(1, 6):", list(range(1, 6)))
print("range(1, 10, 2):", list(range(1, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))

print("\nТаблиця множення на 3:")
for i in range(1, 6):
    print(f"  3 × {i} = {3 * i}")
```

```text
range(5): [0, 1, 2, 3, 4]
range(1, 6): [1, 2, 3, 4, 5]
range(1, 10, 2): [1, 3, 5, 7, 9]
range(10, 0, -1): [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Таблиця множення на 3:
  3 × 1 = 3
  3 × 2 = 6
  3 × 3 = 9
  3 × 4 = 12
  3 × 5 = 15
```

#### `zip(*iterables)`

Об'єднує кілька послідовностей у пари/кортежі з однаковими індексами. Зупиняється на найкоротшій послідовності.

```python
names = ["Anna", "Oleg", "Maria"]
ages = [25, 30, 22]
cities = ["Київ", "Львів", "Харків"]

print("Інформація про користувачів:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age} років, {city}")

# швидке створення словника з двох списків
users_dict = dict(zip(names, ages))
print("\nСловник ім'я → вік:", users_dict)

# якщо списки різної довжини — zip зупиняється на коротшому
print(list(zip([1, 2, 3], [1, 2])))
```

```text
Інформація про користувачів:
  Anna, 25 років, Київ
  Oleg, 30 років, Львів
  Maria, 22 років, Харків

Словник ім'я → вік: {'Anna': 25, 'Oleg': 30, 'Maria': 22}
[(1, 1), (2, 2)]
```

#### `enumerate(iterable, start=0)`

Додає лічильник до ітерованого об'єкта — повертає пари `(індекс, значення)`. Коли в циклі потрібен і елемент, і його номер — без ручного лічильника.

```python
tasks = ["Прочитати теорію", "Зробити завдання", "Здати на перевірку"]

print("Список завдань:")
for index, task in enumerate(tasks, 1):  # нумерація з 1
    print(f"  {index}. {task}")

# порівняння: без enumerate (старий, гірший стиль)
print("\nБез enumerate (гірший спосіб):")
i = 0
for task in tasks:
    print(f"  {i}: {task}")
    i += 1
```

```text
Список завдань:
  1. Прочитати теорію
  2. Зробити завдання
  3. Здати на перевірку

Без enumerate (гірший спосіб):
  0: Прочитати теорію
  1: Зробити завдання
  2: Здати на перевірку
```

### Функціональне програмування

#### `map(function, iterable)`

Застосовує функцію до кожного елемента послідовності. Масова трансформація даних.

```python
str_numbers = ["1", "2", "3", "4", "5"]
print("Рядки:", str_numbers)

numbers = list(map(int, str_numbers))
print("Числа:", numbers)

squared = list(map(lambda x: x ** 2, numbers))
print("Квадрати:", squared)

words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print("Верхній регістр:", upper_words)

print(list(map(float, ["1.5", "2.7", "3.0"])))
```

```text
Рядки: ['1', '2', '3', '4', '5']
Числа: [1, 2, 3, 4, 5]
Квадрати: [1, 4, 9, 16, 25]
Верхній регістр: ['HELLO', 'WORLD', 'PYTHON']
[1.5, 2.7, 3.0]
```

#### `filter(function, iterable)`

Залишає лише елементи, для яких функція повертає `True`. Очищення/вибірка даних.

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Вихідний список:", nums)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Парні числа:", evens)

big_nums = list(filter(lambda x: x > 5, nums))
print("Числа > 5:", big_nums)

# None як функція-фільтр — перевіряє на True/False (непорожній рядок = True)
strings = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, strings))
print("Непорожні рядки:", non_empty)

print(list(filter(lambda x: x < 0, [-5, 3, -1, 7, -9, 2])))
```

```text
Вихідний список: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Парні числа: [2, 4, 6, 8, 10]
Числа > 5: [6, 7, 8, 9, 10]
Непорожні рядки: ['hello', 'world', 'python']
[-5, -1, -9]
```

### Модуль `random`

Для роботи з випадковими числами потрібно `import random`. Модуль базується на алгоритмі «Вихор Мерсенна» — генерує псевдовипадкові числа.

#### `random.randint(a, b)`

Випадкове ціле число в діапазоні `[a, b]` **включно**. Кидок кубика, ігрові механіки.

```python
import random

dice_roll = random.randint(1, 6)
print("Кидок кубика:", dice_roll)

print("5 кидків кубика:", [random.randint(1, 6) for _ in range(5)])
print("Випадкове число від 1 до 100:", random.randint(1, 100))
```

```text
Кидок кубика: <випадкове число від 1 до 6>
5 кидків кубика: [<...5 випадкових чисел від 1 до 6...>]
Випадкове число від 1 до 100: <випадкове число від 1 до 100>
```

Без `random.seed()` кожен запуск дає інші числа — саме тому конкретні значення тут не зафіксовані (див. `random.seed()` нижче про відтворюваність).

#### `random.choice(seq)`

Один випадковий елемент із непорожньої послідовності. Жеребкування, хід комп'ютера у грі.

```python
colors = ["червоний", "зелений", "синій", "жовтий"]
winner = random.choice(colors)
print("Випадковий колір:", winner)

# гра «Камінь, ножиці, папір» — хід комп'ютера
options = ["камінь", "ножиці", "папір"]
computer_move = random.choice(options)
print("Комп'ютер обрав:", computer_move)

# також працює з рядком!
random_letter = random.choice("ABCDEFGHIJK")
print("Випадкова літера:", random_letter)
```

#### `random.random()`

Число з плаваючою крапкою в діапазоні `[0.0, 1.0)`. Ймовірності, статистичне моделювання.

```python
chance = random.random()
print("Випадкова ймовірність:", chance)

# подія з 30% шансом
if random.random() < 0.30:
    print("⚡ Критичний удар!")
else:
    print("Звичайна атака")

# симуляція 10 підкидань монети
results = ["Орел" if random.random() < 0.5 else "Решка" for _ in range(10)]
print("10 підкидань монети:", results)
```

#### `random.uniform(a, b)`

Випадкове дійсне число між `a` та `b` (на відміну від `randint`, який дає лише цілі).

```python
temperature = random.uniform(15.5, 25.5)
print(f"Температура: {temperature:.2f}°C")

prices = [round(random.uniform(10.0, 99.99), 2) for _ in range(5)]
print("Випадкові ціни:", prices)

print("\nrandint(1, 10):", random.randint(1, 10), "← ціле число")
print("uniform(1, 10):", random.uniform(1, 10), "← дійсне число")
```

#### `random.shuffle(seq)`

Перемішує елементи списку **на місці** — змінює сам оригінальний список.

```python
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8"]
print("До тасування:", cards)

random.shuffle(cards)
print("Після тасування:", cards)
```

!!! warning "shuffle() змінює оригінал"
    Якщо потрібно зберегти оригінальний порядок — тасуйте копію, а не сам список:

    ```python
    original = [1, 2, 3, 4, 5]
    shuffled = original.copy()
    random.shuffle(shuffled)
    print("Оригінал:", original)
    print("Перемішаний:", shuffled)
    ```

#### `random.sample(population, k)`

Новий список із `k` **унікальних** елементів (без повторень) — на відміну від багаторазового `choice()`.

```python
lottery_balls = range(1, 50)  # кулі від 1 до 49
winning_numbers = random.sample(lottery_balls, 6)
print("Переможні числа лотереї:", sorted(winning_numbers))

students = ["Аня", "Богдан", "Василь", "Галя", "Дмитро", "Олена"]
selected = random.sample(students, 3)
print("\nВибрані студенти (без повторень):", selected)
```

Якщо `k > len(population)` — `random.sample()` підніме `ValueError` (недостатньо елементів для вибірки без повторень).

#### `random.randrange(start, stop, step)`

Випадкове ціле з `range(start, stop, step)` — тобто **не включаючи** `stop` (на відміну від `randint`, який включає обидва краї).

```python
even = random.randrange(0, 21, 2)         # тільки парні 0..20
print("Випадкове парне число (0-20):", even)

multiple_of_5 = random.randrange(0, 101, 5)
print("Кратне 5 від 0 до 100:", multiple_of_5)

print("\nrandint(1, 10):", random.randint(1, 10), "← включає 10")
print("randrange(1, 10):", random.randrange(1, 10), "← НЕ включає 10")
```

#### `random.seed(x)`

Фіксує початкове значення генератора псевдовипадкових чисел — при однаковому `seed` результати завжди однакові. Відтворюваність у експериментах і при дебазі.

```python
import random

random.seed(42)
print("З seed=42 (перший запуск):", [random.randint(1, 10) for _ in range(5)])

random.seed(42)
print("З seed=42 (другий запуск):", [random.randint(1, 10) for _ in range(5)])
```

```text
З seed=42 (перший запуск): [2, 1, 5, 4, 4]
З seed=42 (другий запуск): [2, 1, 5, 4, 4]
```

Обидва рядки однакові — `seed` гарантує повністю відтворювану послідовність при кожному запуску (доки версія Python та сама послідовність викликів не змінюються).

### `sorted()`, `any()`, `all()`

#### `sorted(iterable, key=None, reverse=False)`

Повертає **новий** відсортований список — оригінал не змінюється (на відміну від `.sort()`, який сортує список на місці).

```python
words = ["яблуко", "кіт", "ананас", "буря", "ліс"]
print("Оригінал:", words)
print("За алфавітом:", sorted(words))
print("За довжиною:", sorted(words, key=len))
print("Зворотньо:", sorted(words, reverse=True))
print("Оригінал не змінився:", words)  # ← sorted не змінює оригінал!

students = [
    {"name": "Аня", "score": 88},
    {"name": "Богдан", "score": 72},
    {"name": "Василь", "score": 95},
]
by_score = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nРейтинг студентів:")
for i, s in enumerate(by_score, 1):
    print(f"  {i}. {s['name']} — {s['score']} балів")
```

```text
Оригінал: ['яблуко', 'кіт', 'ананас', 'буря', 'ліс']
За алфавітом: ['ананас', 'буря', 'кіт', 'ліс', 'яблуко']
За довжиною: ['кіт', 'ліс', 'буря', 'яблуко', 'ананас']
Зворотньо: ['яблуко', 'ліс', 'кіт', 'буря', 'ананас']
Оригінал не змінився: ['яблуко', 'кіт', 'ананас', 'буря', 'ліс']

Рейтинг студентів:
  1. Василь — 95 балів
  2. Аня — 88 балів
  3. Богдан — 72 балів
```

#### `any(iterable)` та `all(iterable)`

- `any()` → `True`, якщо **хоча б один** елемент істинний.
- `all()` → `True`, якщо **всі** елементи істинні.

Заміна довгих циклів з перевірками, валідація даних.

```python
scores = [85, 72, 0, 91, 68]
print("Бали:", scores)

print("\nany():")
print("Хтось отримав 0?", any(s == 0 for s in scores))
print("Є хтось з 100?", any(s == 100 for s in scores))

print("\nall():")
print("Всі набрали > 50?", all(s > 50 for s in scores))
print("Всі набрали >= 0?", all(s >= 0 for s in scores))

# перевірка паролів
passwords = ["abc123", "Pass1!", "secure"]
has_digit = [any(c.isdigit() for c in p) for p in passwords]
print("\nПаролі з цифрами:", list(zip(passwords, has_digit)))
```

```text
Бали: [85, 72, 0, 91, 68]

any():
Хтось отримав 0? True
Є хтось з 100? False

all():
Всі набрали > 50? False
Всі набрали >= 0? True

Паролі з цифрами: [('abc123', True), ('Pass1!', True), ('secure', False)]
```

## Практичні завдання

Спробуйте розв'язати самостійно, використовуючи функції з цієї сторінки:

1. Є список оцінок `[45, 78, 92, 55, 88, 71, 33, 96]`. Знайдіть середній бал, найвищий і найнижчий результат.
2. Зі списку імен `["Аня", "Богдан", "Аліна", "Андрій", "Катя"]` відфільтруйте тільки ті, що починаються на «А».
3. Симулюйте 100 кидків монети і порахуйте, скільки разів випав «Орел» і скільки «Решка».

## Шпаргалка — швидка довідка

| Функція | Що робить | Приклад |
|---|---|---|
| `sum(lst)` | Сума елементів | `sum([1,2,3])` → `6` |
| `min(lst)` | Мінімум | `min([3,1,2])` → `1` |
| `max(lst)` | Максимум | `max([3,1,2])` → `3` |
| `abs(x)` | Абсолютне значення | `abs(-5)` → `5` |
| `round(x, n)` | Округлення | `round(3.14159, 2)` → `3.14` |
| `len(s)` | Довжина | `len([1,2,3])` → `3` |
| `range(a,b,s)` | Послідовність чисел | `list(range(0,6,2))` → `[0,2,4]` |
| `zip(a, b)` | Об'єднати списки | `zip([1,2],["a","b"])` |
| `enumerate(lst)` | Індекс + елемент | `enumerate(["a","b"])` |
| `map(f, lst)` | Трансформація | `map(int, ["1","2"])` |
| `filter(f, lst)` | Фільтрація | `filter(lambda x: x>0, lst)` |
| `sorted(lst)` | Сортування | `sorted([3,1,2])` → `[1,2,3]` |
| `any(lst)` | Хоча б один `True` | `any([0, 0, 1])` → `True` |
| `all(lst)` | Всі `True` | `all([1, 1, 0])` → `False` |
| `type(x)` | Тип об'єкта | `type(42)` → `int` |
| `isinstance(x, T)` | Перевірка типу | `isinstance(42, int)` → `True` |
| `dir(x)` | Методи об'єкта | `dir([])` → список методів |
| `id(x)` | Ідентифікатор об'єкта в пам'яті | `id(x)` |
| `random.randint(a,b)` | Ціле число `[a,b]` | `randint(1,6)` → `4` |
| `random.choice(lst)` | Один випадковий елемент | `choice(["a","b","c"])` |
| `random.random()` | Число `[0.0, 1.0)` | `random()` → `0.73...` |
| `random.uniform(a,b)` | Дійсне число `[a,b]` | `uniform(1,10)` |
| `random.shuffle(lst)` | Перемішати список (на місці) | `shuffle([1,2,3,4])` |
| `random.sample(lst,k)` | `k` унікальних елементів | `sample(range(50), 6)` |
| `random.randrange(a,b,s)` | Ціле з `range`, без `b` | `randrange(0,21,2)` |
| `random.seed(x)` | Фіксувати результат | `seed(42)` |
