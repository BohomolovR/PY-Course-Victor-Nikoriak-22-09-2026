# Ноутбуки в Google Colab

Google Colab запускає Jupyter-ноутбуки просто в браузері: нічого встановлювати не треба, потрібен лише Google-акаунт.

## Як відкрити ноутбук уроку

**Спосіб 1 — кнопка.** У першій клітинці кожного ноутбука (і поруч із посиланнями на ноутбуки в книзі) є кнопка [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](#). Натисни її, і ноутбук відкриється в Colab.

**Спосіб 2 — адреса вручну.** Відкрий ноутбук на GitHub і в адресі заміни `https://github.com/` на `https://colab.research.google.com/github/`:

```text
https://github.com/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_03_variables_and_data_types/note_lesson_variables.ipynb
https://colab.research.google.com/github/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_03_variables_and_data_types/note_lesson_variables.ipynb
```

**Спосіб 3 — із самого Colab.** File → Open notebook → вкладка **GitHub** → введи `NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026` → обери файл.

Уроки лежать у `module_N/lessons/lesson_NN_<тема>/`, де `NN` — номер уроку за програмою курсу.

## Збережи свою копію

Ноутбук, відкритий із репозиторію курсу, **не зберігає твоїх змін**. Щоб працювати з ним:

- **File → Save a copy in Drive** — копія з'явиться на твоєму Google Drive (папка «Colab Notebooks»). Далі працюй у ній.
- Якщо викладач оновив урок, твоя копія на Drive сама не оновиться. Відкрий ноутбук заново кнопкою Colab.

## Здача домашки з Colab

Домашні роботи здаються через Pull Request із гілки твого fork (див. [Здача домашніх робіт](homework_workflow.md)). Щоб зберегти ноутбук із Colab одразу у свій fork:

1. File → **Save a copy in GitHub**.
2. Repository: **твій fork** (`<твій-логін>/PY-Course-Victor-Nikoriak-22-09-2026`), а не репозиторій викладача.
3. Branch: гілка домашки (наприклад, `homework-03`). Спершу створи її на GitHub або локально.
4. File path: **повний шлях** до файлу, який вказано в завданні, а не лише ім'я файлу.
5. Далі на GitHub відкрий Pull Request `homework-03 → main`.

## Ноутбуки, яким потрібні сусідні файли

Деякі уроки імпортують `.py`-файли або читають дані з тієї ж папки. Наприклад, урок 14 читає `contacts.json` та `orders.csv`. У Colab є лише сам ноутбук, тому додай на його початок клітинку:

```python
!git clone --depth 1 https://github.com/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026.git course
%cd course/module_1/lessons/lesson_14_file_io_json
```

Шлях після `%cd` — це папка уроку, який ти відкрив.

## Помилка «Could not find … .ipynb»

Кнопка Colab зберігає повний шлях до файлу в репозиторії. Ця помилка означає, що за цим шляхом файлу немає: ноутбук перенесли, або кнопка веде на старий репозиторій курсу. Відкрий ноутбук через книгу курсу або вручну (спосіб 2) і повідом викладача.

## Для викладача: як не зламати посилання

- **Джерело правди — репозиторій на GitHub.** Кнопку Colab (перша клітинка з `id: view-in-github`) і `metadata.lms` генерує скрипт. Вручну їх не редагуй.
- **Зберігаєш зміни з Colab:** File → Save a copy in GitHub → репозиторій `NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026`, гілка `main`. У полі **File path** вкажи повний шлях, наприклад `module_1/lessons/lesson_07_functions/note_lesson_07_functions.ipynb`. За замовчуванням Colab підставляє лише ім'я файлу, і тоді ноутбук потрапляє в корінь репозиторію: саме так посилання зламалися після переїзду зі старого курсу. Галочку «Include a link to Colaboratory» не знімай.
- **Додав, переніс або перейменував ноутбук** — запусти:

    ```bash
    python tools/sync_notebook_metadata.py
    ```

    Скрипт оновить кнопку Colab, `metadata.lms` (потік, модуль, номер і назву уроку, шлях), перетворить відносні посилання на абсолютні (у Colab відносні не працюють) і розставить кнопки Colab у книзі поруч із посиланнями на ноутбуки. GitHub Actions на кожен push і PR запускає `python tools/sync_notebook_metadata.py --check` і падає, якщо щось розсинхронізовано.
- **Номери й назви уроків** беруться з `tools/lessons_v5.json` (програма v5.0), модулі — з `course.json`.
