# Урок 15. Git & GitHub: від використання workflow до розуміння системи

Тип: Урок. Організація рішення — робочий процес, контроль версій (інструментальний урок, не суто програмна задача).

Це **не** перше знайомство з Git — воно вже відбулося на уроці 1, і студент до цього моменту вже кілька разів здавав домашні роботи через `commit → push → Pull Request` (горизонтальний трек, §1.4 `migration_plan.md`). Тут відбувається перехід від «Git як інструмент» («я знаю, які команди виконувати») до «Git як система» («я розумію, що насправді відбувається»):

```text
working tree → staging area → local repository → commit graph → branches → remote → push / pull → merge → Pull Request
```

Плюс: конфлікти, `.gitignore`, хороші commit-повідомлення, README проєкту, структура репозиторію. «Портфоліо» тут — **не** урок особистого брендингу, а мінімальна професійна база: зрозумілий README, адекватна структура, `.gitignore`, залежності, нормальна історія коммітів, кілька проєктів на показ.

## Що на ньому відбувається

- **RETRIEVE** — без підглядання: які команди йдуть від «код написано» до «PR відкрито», що показує `git status`, чим `origin` відрізняється від `upstream`.
- **CONCEPT** — три реальних місця, де побували твої файли (working tree → staging area → local repository) і навіщо staging area взагалі потрібна окремим кроком; commit graph; branch як рухомий вказівник, а не копія файлів; `origin`/`upstream` як звичайні іменовані посилання; `push`/`pull` (= `fetch` + `merge`); merge (fast-forward проти справжнього three-way merge); і головне — **merge conflict**: чому він виникає, як читати маркери `<<<<<<<`/`=======`/`>>>>>>>`, як розв'язати (4 кроки) і як безпечно скасувати (`git merge --abort`) — цієї теми раніше в курсі не було.
- **CREATE** — дві практичні вправи в терміналі: (1) створення **власного** (не fork) репозиторію на GitHub — новий матеріал, якого раніше не було в курсі; (2) навмисне створення і розв'язання merge conflict на маленькому підготовленому прикладі, щоб уперше зустріти конфлікт у контрольованих умовах, а не в паніці посеред реальної домашньої роботи.
- **TRANSFER** — приведення одного з попередніх проєктів курсу до мінімального «портфоліо-вигляду» (README, `.gitignore`, чиста історія комітів) за конкретним чеклистом, перевіреним двома невеликими Python-функціями просто в ноутбуці.

**Ноутбук заняття:** [`note_lesson_15_git_github_system.ipynb`](https://github.com/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_15_git_github_system/note_lesson_15_git_github_system.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/NikoriakViktot/PY-Course-Victor-Nikoriak-22-09-2026/blob/main/module_1/lessons/lesson_15_git_github_system/note_lesson_15_git_github_system.ipynb)

👉 Практичні інструкції — вже написана студентська документація, тут не переказується: [«Як користуватися» → GitHub](../../00_getting_started/github/README.md) (SSH-ключі, Fork і Clone, Pull Request, [Як створити свій репозиторій](../../00_getting_started/github/create_repository.md)) і [Git шпаргалка](../../git-cheatsheet.md) (команди, базові діаграми — цей урок іде на рівень глибше за неї).
