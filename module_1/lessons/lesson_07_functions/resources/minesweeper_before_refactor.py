"""Позиція 6 (дані + dict/loops) — версія Minesweeper ДО рефакторингу у функції.

Це стартова точка PRIMM-вправи Уроку 7 («Функції»). Вся логіка тут навмисно
записана як плаский код на верхньому рівні модуля — без жодної функції.
`resources/07_minesweeper_teacher_solution.py` (в data/Модуль 1. Python core/Code
snippets/) показує ту саму гру, розкладену на функції create_bombs/count_around/
create_board/print_board/read_move/show_bombs.

Дані навмисно представлені так само, як і в teacher-solution (bombs — множина
кортежів (row, col), дошка hidden — список списків), щоб рефакторинг на Уроці 7
був вправою на ДЕКОМПОЗИЦІЮ, а не одночасно ще й на зміну структури даних.

Зверни увагу під час читання: змінні `row`/`col` використовуються і в циклі
друку дошки, і в циклі читання ходу гравця — і це прекрасно ілюструє, навіщо
взагалі потрібні функції: кожен блок логіки "тягне" за собою свої власні імена
змінних у спільний простір імен модуля.
"""

import random

SIZE = 8
BOMBS = 10

# 1) генеруємо позиції бомб — множина кортежів (row, col)
bombs = set()
while len(bombs) < BOMBS:
    bombs.add((random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)))

# 2) створюємо приховану дошку — список списків, усі клітинки "."
hidden = [["." for col in range(SIZE)] for row in range(SIZE)]

opened = 0

while opened < SIZE * SIZE - BOMBS:
    # друкуємо дошку (з номерами рядків і колонок)
    header = "  "
    for col in range(len(hidden)):
        header += " " + str(col)
    print(header)
    for row in range(len(hidden)):
        line = str(row) + " "
        for cell in hidden[row]:
            line += " " + cell
        print(line)

    # читаємо хід, поки не введуть коректні координати
    while True:
        answer = input("Row and column, for example 3 5: ").split()
        if len(answer) != 2 or not answer[0].isdigit() or not answer[1].isdigit():
            print("Type two numbers from 0 to", SIZE - 1)
        elif int(answer[0]) >= SIZE or int(answer[1]) >= SIZE:
            print("This cell is outside the board")
        else:
            row, col = int(answer[0]), int(answer[1])
            break

    if hidden[row][col] != ".":
        print("This cell is already open")
        continue
    if (row, col) in bombs:
        print("Boom! Game over.")
        break

    # рахуємо бомби навколо клітинки
    around = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (row + dr, col + dc) in bombs:
                around += 1

    hidden[row][col] = str(around)
    opened += 1
else:
    print("You win!")

# показати всі бомби наприкінці
for row, col in bombs:
    hidden[row][col] = "*"

header = "  "
for col in range(len(hidden)):
    header += " " + str(col)
print(header)
for row in range(len(hidden)):
    line = str(row) + " "
    for cell in hidden[row]:
        line += " " + cell
    print(line)
