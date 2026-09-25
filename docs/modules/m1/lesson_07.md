# Урок 7. Функції

Організація рішення через декомпозицію.

Що на ньому відбувається:

- визначення функцій, параметри й значення за замовчуванням, `return`;
- декомпозиція задачі на функції; патерни predicate/transformer/reducer;
- центральний кейс уроку — рефакторинг робочого, але монолітного Minesweeper-скрипта (написаного на уроці 6 через словники й цикли) у чисті функції: `create_bombs`, `count_around`, `create_board` — природний перехід Investigate → Modify → Create циклу RETRIEVE→…→TRANSFER;
- сумісність результату до й після рефакторингу перевірена в ноутбуці виконанням із фіксованим seed.

**Ноутбук заняття:** [`note_lesson_07_functions.ipynb`](https://github.com/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_07_functions/note_lesson_07_functions.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_07_functions/note_lesson_07_functions.ipynb)

👉 Повний довідник — [Функції та функціональне програмування](../../reference/python_core/functions.md) (замикання, декоратори, `*args`/`**kwargs`, `map`/`filter`/`reduce`) і [Простори імен / LEGB](../../reference/python_core/namespaces_legb.md).
