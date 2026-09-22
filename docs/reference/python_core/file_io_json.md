# Довідник: File I/O та JSON

Короткий довідник по роботі з файлами та серіалізацією JSON у Python. Повний, поступово побудований конспект із наскрізним сценарієм (звіт ресторану → `report.json`) — [Урок 14. Файли I/O, менеджери контексту, JSON](../../modules/m1/lesson_14.md).

## `open()` — режими файлів

```python
open(filename, mode, encoding="utf-8")
```

| Режим | Призначення | Якщо файл є | Якщо файлу немає |
|-------|-------------|-------------|------------------|
| `r`   | Читання (default) | Відкриває | `FileNotFoundError` |
| `w`   | Запис | **Стирає вміст!** | Створює новий |
| `a`   | Дописування в кінець | Дописує | Створює новий |
| `r+`  | Читання + запис | Відкриває | `FileNotFoundError` |

## Context Manager — `with open(...) as f:`

```python
# ✅ ЗАВЖДИ використовуй 'with' — гарантує закриття файлу
with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Дані\n")
# f.close() викликається автоматично тут

# ❌ НЕ РОБИ ТАК — ризик Resource Leak:
f = open("file.txt", "w")
f.write("Дані")
f.close()   # ← може не досягтись, якщо станеться помилка раніше!
```

Детальніше про те, чому ручне закриття ненадійне (і як воно пов'язане з обробкою винятків) — [Урок 14 → `with open(...)` — навіщо](../../modules/m1/lesson_14.md).

## Читання файлів

```python
# Весь вміст одразу (увага: не для гігабайтних файлів!)
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Один рядок
with open("file.txt", "r", encoding="utf-8") as f:
    line = f.readline()

# ✅ Рядок за рядком (лінивий — ефективно для великих файлів)
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# Управління курсором
f.tell()     # поточна позиція в байтах
f.seek(0)    # перемотати на початок
```

## Запис файлів

```python
# Тільки рядки! Конвертуй числа через str()
# .write() НЕ додає \n автоматично!

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Рядок перший\n")   # ← \n обов'язковий
    f.write(str(42) + "\n")     # ← int → str

# Дописати в кінець (не стираючи):
with open("file.txt", "a", encoding="utf-8") as f:
    f.write("Новий рядок\n")
```

## JSON — серіалізація та десеріалізація

### Відповідність типів Python ↔ JSON

| Python | JSON |
|--------|------|
| `dict` | `{}` object |
| `list`, `tuple` | `[]` array |
| `str` | `"string"` |
| `int`, `float` | `number` |
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| `datetime` | ❌ — треба `.isoformat()` |

### Основні функції

```python
import json

# Серіалізація Python → JSON
json_str = json.dumps(obj)                          # → рядок
json.dump(obj, file, ensure_ascii=False, indent=4)   # → файл

# Десеріалізація JSON → Python
obj = json.loads(json_str)   # з рядка
obj = json.load(file)        # з файлу
```

### Повний цикл save/load

```python
import json

data = {"name": "Alice", "scores": [95, 87, 92]}

# Зберегти
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

# Завантажити
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)   # loaded — знову dict!
```

### Обмеження

```python
# ❌ Tuple як ключ → TypeError
json.dumps({("Alice", "Smith"): 150})   # TypeError!

# ✅ Рядковий ключ
json.dumps({"Alice Smith": 150})        # OK

# ❌ str() — НЕ є JSON!
f.write(str(my_dict))    # одинарні лапки → JSONDecodeError при load!
json.dump(my_dict, f)    # ← правильно
```

Ще одне типове джерело `TypeError` — числові типи `pandas`/`numpy` (`numpy.int64`, `numpy.float64`): `json` серіалізує лише вбудовані типи Python, тому такі значення явно приводять через `float()`/`int()` перед записом (детальніше й на реальному прикладі — [Урок 14](../../modules/m1/lesson_14.md)).

## Параметри `json.dump()` / `json.dumps()` та `json.load()` / `json.loads()`

```python
json.dumps(obj,
    indent=4,              # відступи для читабельності (None = компактно)
    ensure_ascii=False,    # дозволити не-ASCII символи (кирилиця, emoji)
    sort_keys=True,        # сортувати ключі за алфавітом
    separators=(',', ':')  # компактний режим (без пробілів)
)

json.loads(s,
    object_hook=None,      # функція для кастомної десеріалізації об'єктів
    parse_float=None,      # кастомний парсер float (напр. decimal.Decimal)
    parse_int=None,        # кастомний парсер int
)
# При невалідному JSON → json.JSONDecodeError
```

## `json.tool` — CLI для валідації та форматування

```bash
# Валідація та pretty-print JSON з командного рядка
echo '{"json": "obj"}' | python -m json.tool
# {
#     "json": "obj"
# }

# Сортування ключів
python -m json.tool --sort-keys data.json

# Невалідний JSON → повідомлення про помилку
echo '{1.2:3.4}' | python -m json.tool
# Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
```

`json.tool` запускається як модуль (`python -m json.tool`), а не імпортується — це зручний спосіб перевірити JSON просто в терміналі, без написання Python-скрипта.

## Форматування виводу — f-strings

```python
# Вирівнювання
f"{name:<15}"    # лівий край, 15 символів
f"{value:>10}"   # правий край, 10 символів
f"{text:^20}"    # центр, 20 символів

# Числа
f"{price:.2f}"   # 2 знаки після крапки
f"{big:,}"       # роздільник тисяч: 1,000,000
f"{n:05d}"       # ціле, заповнення нулями, ширина 5: 00042

# Приклад таблиці
for name, balance in data:
    print(f"| {name:<15} | ${balance:>10.2f} |")
```

## Типові помилки (Cheat Sheet)

| Помилка | Причина | Виправлення |
|---------|---------|-------------|
| `FileNotFoundError` | Відкриття неіснуючого файлу через `r` | Перевір шлях або використай `try`/`except` — див. [Довідник: Exceptions](exceptions.md) |
| `TypeError: write() argument must be str` | Спроба записати `int`/`list` напряму | `f.write(str(value))` |
| `JSONDecodeError` | `str(dict)` замість `json.dump()` | Використай `json.dump()` для запису |
| `TypeError: keys must be str` | Tuple/int як ключ JSON-словника | Конвертуй ключ у рядок |
| Файл не закрився при краші | `open()` без `with` | Завжди `with open(...) as f:` |
| Другий `.read()` порожній | File Pointer вже в кінці | `f.seek(0)` або відкрити файл знову |
