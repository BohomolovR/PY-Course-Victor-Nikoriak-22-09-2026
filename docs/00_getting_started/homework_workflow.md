# Здача домашніх робіт

## ❗ Не працюємо в `main`

Уся робота над домашнім завданням відбувається в окремій гілці твого fork.

## Кроки

### 1. Створи гілку

```bash
git checkout -b homework-01
```

### 2. Виконай завдання

Редагуй файли або notebook.

### 3. Commit

```bash
git add .
git commit -m "Homework 01"
```

### 4. Push

```bash
git push origin homework-01
```

### 5️⃣ Здай домашню роботу через Pull Request

👉 Детальна покрокова інструкція зі скриншотами кожного кроку — [Pull Request](github/pull_request.md).

1️⃣ Відкрий репозиторій на GitHub.

2️⃣ GitHub часто автоматично покаже кнопку **Compare & pull request**. Якщо ні — натисни **New pull request**.

3️⃣ Обери гілки:

```
base: main
compare: homework-01
```

Тобто `homework-01 → main`.

4️⃣ Натисни **Create pull request**.

## ✅ Отримання фідбеку

Після створення Pull Request:

- викладач перегляне код
- залишить коментарі
- запропонує покращення

Якщо потрібно внести зміни — просто:

```bash
git add .
git commit -m "fix review comments"
git push
```

Pull Request оновиться автоматично.

📖 Детальніше про структуру репозиторію: [Архітектура репозиторію](../../architecture.md)

## 📏 Правила

- ✅ 1 домашка = 1 гілка
- ✅ нормальні commit messages
- ✅ оновлювати `main` перед заняттям (див. [Fork і Clone → перед кожним заняттям](github/fork_and_clone.md))
- ❌ не працювати в `main`
- ❌ не merge PR самостійно
- ❌ не видаляти матеріали курсу
