# Встановлення Git

Git — це система контролю версій, через яку ми:

- отримуємо матеріали курсу
- здаємо домашні завдання
- отримуємо фідбек

Все, що стосується самого GitHub (акаунт, SSH, fork, Pull Request) — в окремому розділі [GitHub](github/README.md). Тут — лише встановлення Git.

## 🪟 Windows

🔗 Офіційна сторінка: https://git-scm.com/install/windows
🔗 Пряме завантаження: https://github.com/git-for-windows/git/releases/latest

Завантаж `Git for Windows/x64 Setup`. Під час встановлення просто натискай **Next** (налаштування за замовчуванням).

## 🍎 macOS

🔗 Інструкція: https://git-scm.com/install/mac

Відкрий Terminal:

```bash
xcode-select --install
```

## 🐧 Linux

🔗 Інструкція: https://git-scm.com/install/linux

```bash
# Ubuntu / Debian
sudo apt update
sudo apt install git

# Fedora
sudo dnf install git

# Arch
sudo pacman -S git
```

## ✅ Перевірка встановлення

```bash
git --version
```

Очікуваний результат: `git version 2.xx.x`

## ✅ Перше налаштування Git (один раз)

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

⚠️ Email має співпадати з тим, що вказаний на GitHub.
